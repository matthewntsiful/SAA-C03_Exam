/**
 * Enhanced SAA-C03 Practice Exam JavaScript
 * Implements industry best practices for online certification exams
 */

class SAAPracticeExam {
    constructor(questions) {
        this.questions = questions;
        this.currentQuestion = 0;
        this.answers = {};
        this.flaggedQuestions = new Set();
        this.timeLeft = 130 * 60; // 130 minutes in seconds
        this.timerInterval = null;
        this.isPaused = false;
        this.startTime = Date.now();
        this.autoSaveInterval = null;
        
        this.init();
    }
    
    init() {
        this.loadSavedState();
        this.generateQuestionNavigation();
        this.displayQuestion(this.currentQuestion);
        this.startTimer();
        this.startAutoSave();
        this.updateProgress();
        this.bindKeyboardShortcuts();
    }
    
    // Auto-save functionality
    startAutoSave() {
        this.autoSaveInterval = setInterval(() => {
            this.saveState();
        }, 30000); // Save every 30 seconds
    }
    
    saveState() {
        const state = {
            currentQuestion: this.currentQuestion,
            answers: this.answers,
            flaggedQuestions: Array.from(this.flaggedQuestions),
            timeLeft: this.timeLeft,
            timestamp: Date.now()
        };
        localStorage.setItem('saa_exam_state', JSON.stringify(state));
    }
    
    loadSavedState() {
        const saved = localStorage.getItem('saa_exam_state');
        if (saved) {
            const state = JSON.parse(saved);
            // Only load if saved within last 4 hours
            if (Date.now() - state.timestamp < 4 * 60 * 60 * 1000) {
                this.currentQuestion = state.currentQuestion || 0;
                this.answers = state.answers || {};
                this.flaggedQuestions = new Set(state.flaggedQuestions || []);
                this.timeLeft = state.timeLeft || 130 * 60;
            }
        }
    }
    
    // Timer functionality
    startTimer() {
        this.timerInterval = setInterval(() => {
            if (!this.isPaused) {
                this.timeLeft--;
                this.updateTimerDisplay();
                
                // Warning at 30 minutes
                if (this.timeLeft === 30 * 60) {
                    this.showTimeWarning('30 minutes remaining!');
                }
                
                // Warning at 10 minutes
                if (this.timeLeft === 10 * 60) {
                    this.showTimeWarning('10 minutes remaining!');
                }
                
                // Auto-submit when time expires
                if (this.timeLeft <= 0) {
                    this.submitExam(true);
                }
            }
        }, 1000);
    }
    
    updateTimerDisplay() {
        const minutes = Math.floor(this.timeLeft / 60);
        const seconds = this.timeLeft % 60;
        const timeString = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        document.getElementById('timer').textContent = timeString;
        document.getElementById('timeRemaining').textContent = timeString;
        
        // Change color based on time remaining
        const timerElement = document.getElementById('timer');
        if (this.timeLeft < 10 * 60) {
            timerElement.style.color = '#dc3545';
        } else if (this.timeLeft < 30 * 60) {
            timerElement.style.color = '#ffc107';
        }
    }
    
    toggleTimer() {
        this.isPaused = !this.isPaused;
        const btn = document.getElementById('pauseBtn');
        btn.textContent = this.isPaused ? 'Resume' : 'Pause';
    }
    
    showTimeWarning(message) {
        // Create toast notification
        const toast = document.createElement('div');
        toast.className = 'time-warning-toast';
        toast.textContent = message;
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #ffc107;
            color: #000;
            padding: 15px 25px;
            border-radius: 8px;
            font-weight: bold;
            z-index: 1000;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        `;
        
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 5000);
    }
    
    // Question navigation
    generateQuestionNavigation() {
        const nav = document.getElementById('questionNav');
        nav.innerHTML = '';
        
        for (let i = 0; i < this.questions.length; i++) {
            const btn = document.createElement('button');
            btn.className = 'nav-btn';
            btn.textContent = i + 1;
            btn.onclick = () => this.goToQuestion(i);
            btn.setAttribute('aria-label', `Go to question ${i + 1}`);
            nav.appendChild(btn);
        }
        
        this.updateNavigationState();
    }
    
    updateNavigationState() {
        const navBtns = document.querySelectorAll('.nav-btn');
        navBtns.forEach((btn, index) => {
            btn.className = 'nav-btn';
            
            if (index === this.currentQuestion) {
                btn.classList.add('current');
            }
            
            if (this.answers[index] !== undefined) {
                btn.classList.add('answered');
            }
            
            if (this.flaggedQuestions.has(index)) {
                btn.classList.add('flagged');
            }
        });
    }
    
    // Question display
    displayQuestion(questionIndex) {
        const question = this.questions[questionIndex];
        const container = document.getElementById('questionContainer');
        
        // Determine if multiple choice
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        const inputType = isMultiple ? 'checkbox' : 'radio';
        
        container.innerHTML = `
            <div class="question-header">
                <div class="question-info">
                    <div class="question-number">Question ${questionIndex + 1} of ${this.questions.length}</div>
                    <div class="question-domain">${question.domain}</div>
                </div>
                <div class="question-actions">
                    <button class="flag-btn ${this.flaggedQuestions.has(questionIndex) ? 'flagged' : ''}" 
                            onclick="exam.toggleFlag(${questionIndex})">
                        🚩 ${this.flaggedQuestions.has(questionIndex) ? 'Unflag' : 'Flag'}
                    </button>
                </div>
            </div>
            
            <div class="question-text">
                ${question.text}
                ${isMultiple ? '<p><strong>Note:</strong> This question may have multiple correct answers.</p>' : ''}
            </div>
            
            <div class="options-container">
                ${Object.entries(question.options).map(([letter, text]) => `
                    <div class="option ${this.isOptionSelected(questionIndex, letter) ? 'selected' : ''}" 
                         onclick="exam.selectOption(${questionIndex}, '${letter}')">
                        <div class="option-content">
                            <input type="${inputType}" 
                                   name="q${questionIndex}" 
                                   value="${letter}" 
                                   ${this.isOptionSelected(questionIndex, letter) ? 'checked' : ''}
                                   onchange="exam.handleOptionChange(${questionIndex}, '${letter}', this.checked)">
                            <div class="option-text">
                                <span class="option-letter">${letter}.</span>
                                ${text}
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
            
            <div class="question-navigation">
                <button class="nav-button" 
                        onclick="exam.previousQuestion()" 
                        ${questionIndex === 0 ? 'disabled' : ''}>
                    ← Previous
                </button>
                
                <div style="display: flex; gap: 15px;">
                    ${questionIndex === this.questions.length - 1 ? 
                        '<button class="nav-button submit-btn" onclick="exam.submitExam()">Submit Exam</button>' :
                        '<button class="nav-button" onclick="exam.nextQuestion()">Next →</button>'
                    }
                </div>
            </div>
        `;
        
        this.updateNavigationState();
        this.updateProgress();
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    // Answer handling
    selectOption(questionIndex, optionLetter) {
        const question = this.questions[questionIndex];
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        
        if (isMultiple) {
            // Handle multiple selection
            if (!this.answers[questionIndex]) {
                this.answers[questionIndex] = [];
            }
            
            const currentAnswers = this.answers[questionIndex];
            const index = currentAnswers.indexOf(optionLetter);
            
            if (index > -1) {
                currentAnswers.splice(index, 1);
            } else {
                currentAnswers.push(optionLetter);
            }
            
            if (currentAnswers.length === 0) {
                delete this.answers[questionIndex];
            }
        } else {
            // Handle single selection
            this.answers[questionIndex] = optionLetter;
        }
        
        this.displayQuestion(questionIndex);
        this.saveState();
    }
    
    handleOptionChange(questionIndex, optionLetter, checked) {
        // This handles direct input changes
        const question = this.questions[questionIndex];
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        
        if (isMultiple) {
            if (!this.answers[questionIndex]) {
                this.answers[questionIndex] = [];
            }
            
            const currentAnswers = this.answers[questionIndex];
            const index = currentAnswers.indexOf(optionLetter);
            
            if (checked && index === -1) {
                currentAnswers.push(optionLetter);
            } else if (!checked && index > -1) {
                currentAnswers.splice(index, 1);
            }
            
            if (currentAnswers.length === 0) {
                delete this.answers[questionIndex];
            }
        } else {
            if (checked) {
                this.answers[questionIndex] = optionLetter;
            }
        }
        
        this.updateNavigationState();
        this.updateProgress();
        this.saveState();
    }
    
    isOptionSelected(questionIndex, optionLetter) {
        const answer = this.answers[questionIndex];
        if (Array.isArray(answer)) {
            return answer.includes(optionLetter);
        }
        return answer === optionLetter;
    }
    
    // Navigation methods
    goToQuestion(questionIndex) {
        this.currentQuestion = questionIndex;
        this.displayQuestion(questionIndex);
    }
    
    nextQuestion() {
        if (this.currentQuestion < this.questions.length - 1) {
            this.currentQuestion++;
            this.displayQuestion(this.currentQuestion);
        }
    }
    
    previousQuestion() {
        if (this.currentQuestion > 0) {
            this.currentQuestion--;
            this.displayQuestion(this.currentQuestion);
        }
    }
    
    // Flag functionality
    toggleFlag(questionIndex) {
        if (this.flaggedQuestions.has(questionIndex)) {
            this.flaggedQuestions.delete(questionIndex);
        } else {
            this.flaggedQuestions.add(questionIndex);
        }
        
        this.displayQuestion(questionIndex);
        this.saveState();
    }
    
    // Progress tracking
    updateProgress() {
        const answered = Object.keys(this.answers).length;
        const total = this.questions.length;
        const percentage = (answered / total) * 100;
        
        document.getElementById('progressText').textContent = `${answered} of ${total} answered`;
        document.getElementById('progressFill').style.width = `${percentage}%`;
    }
    
    // Keyboard shortcuts
    bindKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Only if not in input field
            if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
                switch(e.key) {
                    case 'ArrowLeft':
                        e.preventDefault();
                        this.previousQuestion();
                        break;
                    case 'ArrowRight':
                        e.preventDefault();
                        this.nextQuestion();
                        break;
                    case 'f':
                    case 'F':
                        e.preventDefault();
                        this.toggleFlag(this.currentQuestion);
                        break;
                    case '1':
                    case '2':
                    case '3':
                    case '4':
                    case '5':
                        e.preventDefault();
                        const optionLetter = String.fromCharCode(64 + parseInt(e.key)); // Convert 1-5 to A-E
                        if (this.questions[this.currentQuestion].options[optionLetter]) {
                            this.selectOption(this.currentQuestion, optionLetter);
                        }
                        break;
                }
            }
        });
    }
    
    // Review functionality
    showReview() {
        const unanswered = [];
        const flagged = Array.from(this.flaggedQuestions);
        
        for (let i = 0; i < this.questions.length; i++) {
            if (this.answers[i] === undefined) {
                unanswered.push(i + 1);
            }
        }
        
        let message = 'Exam Review:\\n\\n';
        message += `Answered: ${Object.keys(this.answers).length}/${this.questions.length}\\n`;
        message += `Flagged: ${flagged.length}\\n`;
        message += `Unanswered: ${unanswered.length}\\n\\n`;
        
        if (unanswered.length > 0) {
            message += `Unanswered questions: ${unanswered.join(', ')}\\n`;
        }
        
        if (flagged.length > 0) {
            message += `Flagged questions: ${flagged.map(i => i + 1).join(', ')}\\n`;
        }
        
        alert(message);
    }
    
    // Exam submission
    submitExam(autoSubmit = false) {
        const unanswered = this.questions.length - Object.keys(this.answers).length;
        
        if (!autoSubmit && unanswered > 0) {
            const confirm = window.confirm(
                `You have ${unanswered} unanswered questions. Are you sure you want to submit?`
            );
            if (!confirm) return;
        }
        
        clearInterval(this.timerInterval);
        clearInterval(this.autoSaveInterval);
        
        this.calculateResults();
        localStorage.removeItem('saa_exam_state');
    }
    
    calculateResults() {
        let correct = 0;
        let domainStats = {};
        let reviewHTML = '';
        
        // Initialize domain stats
        const domains = ['Design Secure Architectures', 'Design Resilient Architectures', 
                        'Design High-Performing Architectures', 'Design Cost-Optimized Architectures', 'General'];
        domains.forEach(domain => {
            domainStats[domain] = { correct: 0, total: 0 };
        });
        
        // Calculate scores
        this.questions.forEach((question, index) => {
            const userAnswer = this.answers[index];
            const correctAnswer = question.correct;
            
            domainStats[question.domain].total++;
            
            let isCorrect = false;
            let status = 'unanswered';
            let answerText = '';
            
            if (userAnswer !== undefined) {
                if (Array.isArray(userAnswer)) {
                    // Multiple choice - check if arrays match
                    const correctAnswers = correctAnswer.split(',').map(a => a.trim());
                    isCorrect = correctAnswers.length === userAnswer.length && 
                               correctAnswers.every(a => userAnswer.includes(a));
                } else {
                    // Single choice
                    isCorrect = userAnswer === correctAnswer;
                }
                
                if (isCorrect) {
                    correct++;
                    status = 'correct';
                    domainStats[question.domain].correct++;
                    answerText = `<div class="correct-answer">✓ Correct: ${correctAnswer}</div>`;
                } else {
                    status = 'incorrect';
                    const userAnswerText = Array.isArray(userAnswer) ? userAnswer.join(', ') : userAnswer;
                    answerText = `
                        <div class="your-answer">✗ Your answer: ${userAnswerText}</div>
                        <div class="correct-answer">✓ Correct answer: ${correctAnswer}</div>
                    `;
                }
            } else {
                answerText = `
                    <div class="correct-answer">✓ Correct answer: ${correctAnswer}</div>
                    <div style="color: #856404;">⚠ Not answered</div>
                `;
            }
            
            reviewHTML += `
                <div class="review-item ${status}">
                    <div class="review-question">Question ${index + 1}: ${question.text.substring(0, 100)}...</div>
                    <div class="review-answers">${answerText}</div>
                    <div style="font-size: 0.8em; color: #6c757d; margin-top: 5px;">Domain: ${question.domain}</div>
                </div>
            `;
        });
        
        this.displayResults(correct, domainStats, reviewHTML);
    }
    
    displayResults(correct, domainStats, reviewHTML) {
        const score = Math.round((correct / this.questions.length) * 1000);
        const percentage = Math.round((correct / this.questions.length) * 100);
        const timeUsed = Math.round((Date.now() - this.startTime) / 60000);
        
        // Hide question container and show results
        document.getElementById('questionContainer').style.display = 'none';
        const resultsContainer = document.getElementById('resultsContainer');
        resultsContainer.style.display = 'block';
        
        // Generate domain statistics HTML
        let domainHTML = '';
        Object.entries(domainStats).forEach(([domain, stats]) => {
            if (stats.total > 0) {
                const domainPercentage = Math.round((stats.correct / stats.total) * 100);
                const domainClass = domainPercentage >= 70 ? 'score-pass' : 'score-fail';
                domainHTML += `
                    <div class="result-card">
                        <div class="card-title">${domain.replace('Design ', '')}</div>
                        <div class="${domainClass}" style="font-size: 1.5em; font-weight: bold;">
                            ${stats.correct}/${stats.total} (${domainPercentage}%)
                        </div>
                    </div>
                `;
            }
        });
        
        resultsContainer.innerHTML = `
            <div class="results-header">
                <h1>Exam Complete!</h1>
                <div class="final-score ${score >= 720 ? 'score-pass' : 'score-fail'}">
                    ${score}/1000 (${percentage}%)
                </div>
                <div style="font-size: 1.2em; margin: 20px 0;">
                    ${score >= 720 ? '🎉 CONGRATULATIONS! YOU PASSED!' : '📚 Keep studying! You need 720 to pass'}
                </div>
                <div style="color: #6c757d;">
                    Time Used: ${timeUsed} minutes | Correct: ${correct}/${this.questions.length}
                </div>
            </div>
            
            <div class="results-grid">
                <div class="result-card">
                    <div class="card-title">📊 Overall Performance</div>
                    <div>Score: ${score}/1000</div>
                    <div>Percentage: ${percentage}%</div>
                    <div>Correct: ${correct}/${this.questions.length}</div>
                    <div>Time Used: ${timeUsed} minutes</div>
                </div>
                
                ${domainHTML}
            </div>
            
            <div class="result-card" style="margin-top: 30px;">
                <div class="card-title">📝 Question Review</div>
                <div style="max-height: 400px; overflow-y: auto; margin-top: 15px;">
                    ${reviewHTML}
                </div>
            </div>
            
            <div style="text-align: center; margin: 40px 0;">
                <button class="nav-button" onclick="location.reload()">Take Another Exam</button>
                <button class="nav-button" onclick="window.print()" style="margin-left: 15px;">Print Results</button>
            </div>
        `;
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Global functions for HTML onclick handlers
let exam;

function toggleTimer() {
    exam.toggleTimer();
}

function showReview() {
    exam.showReview();
}

// Initialize exam when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Questions will be injected here by the Python generator
    exam = new SAAPracticeExam(window.examQuestions || []);
});

// Add CSS for review items
const additionalCSS = `
    .review-item {
        margin: 10px 0;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #ddd;
    }
    .review-item.correct {
        background: #d4edda;
        border-left-color: #28a745;
    }
    .review-item.incorrect {
        background: #f8d7da;
        border-left-color: #dc3545;
    }
    .review-item.unanswered {
        background: #fff3cd;
        border-left-color: #ffc107;
    }
    .review-question {
        font-weight: bold;
        margin-bottom: 8px;
    }
    .correct-answer {
        color: #28a745;
        font-weight: bold;
    }
    .your-answer {
        color: #dc3545;
        font-weight: bold;
    }
`;

// Inject additional CSS
const style = document.createElement('style');
style.textContent = additionalCSS;
document.head.appendChild(style);
