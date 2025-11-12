/**
 * Professional SAA-C03 Practice Exam JavaScript
 * Enhanced with horizontal navigation and professional UX
 */

class ProfessionalSAAExam {
    constructor(questions) {
        this.questions = questions;
        this.currentQuestion = 0;
        this.answers = {};
        this.flaggedQuestions = new Set();
        this.timeLeft = 130 * 60;
        this.timerInterval = null;
        this.isPaused = false;
        this.startTime = Date.now();
        this.autoSaveInterval = null;
        
        this.init();
    }
    
    init() {
        this.loadSavedState();
        this.generateHorizontalNavigation();
        this.displayQuestion(this.currentQuestion);
        this.updateTimerDisplay(); // Set initial timer display
        this.startTimer();
        this.startAutoSave();
        this.updateProgress();
        this.bindKeyboardShortcuts();
    }
    
    // Auto-save functionality
    startAutoSave() {
        this.autoSaveInterval = setInterval(() => {
            this.saveState();
        }, 30000);
    }
    
    saveState() {
        const state = {
            currentQuestion: this.currentQuestion,
            answers: this.answers,
            flaggedQuestions: Array.from(this.flaggedQuestions),
            timeLeft: this.timeLeft,
            timestamp: Date.now()
        };
        localStorage.setItem('saa_professional_exam_state', JSON.stringify(state));
    }
    
    loadSavedState() {
        // Clear any old saved state to ensure fresh timer start
        localStorage.removeItem('saa_professional_exam_state');
        
        // Always start with fresh state for now
        this.currentQuestion = 0;
        this.answers = {};
        this.flaggedQuestions = new Set();
        this.timeLeft = 130 * 60; // Always start with 130 minutes
    }
    
    // Enhanced timer with professional styling
    startTimer() {
        this.timerInterval = setInterval(() => {
            if (!this.isPaused) {
                this.timeLeft--;
                this.updateTimerDisplay();
                
                if (this.timeLeft === 30 * 60) {
                    this.showProfessionalNotification('⚠️ 30 minutes remaining', 'warning');
                }
                
                if (this.timeLeft === 10 * 60) {
                    this.showProfessionalNotification('🚨 10 minutes remaining', 'danger');
                }
                
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
        
        document.getElementById('timerDisplay').textContent = timeString;
        document.getElementById('timeRemaining').textContent = timeString;
        
        // Professional color coding
        const timerElement = document.getElementById('timerDisplay');
        if (this.timeLeft < 10 * 60) {
            timerElement.style.color = '#e74c3c';
        } else if (this.timeLeft < 30 * 60) {
            timerElement.style.color = '#f39c12';
        } else {
            timerElement.style.color = '#ff9900';
        }
    }
    
    showProfessionalNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 24px;
            background: ${type === 'danger' ? '#e74c3c' : type === 'warning' ? '#f39c12' : '#4a90e2'};
            color: white;
            padding: 16px 24px;
            border-radius: 12px;
            font-weight: 600;
            z-index: 1001;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            transform: translateX(100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }, 4000);
    }
    
    // Professional sidebar navigation
    generateHorizontalNavigation() {
        const navGrid = document.getElementById('questionNavGrid');
        navGrid.innerHTML = '';
        
        for (let i = 0; i < this.questions.length; i++) {
            const btn = document.createElement('button');
            btn.className = 'nav-question-btn';
            btn.textContent = i + 1;
            btn.onclick = () => this.goToQuestion(i);
            btn.setAttribute('aria-label', `Go to question ${i + 1}`);
            btn.title = `Question ${i + 1}`;
            navGrid.appendChild(btn);
        }
        
        this.updateNavigationState();
    }
    
    updateNavigationState() {
        const navBtns = document.querySelectorAll('.nav-question-btn');
        navBtns.forEach((btn, index) => {
            btn.className = 'nav-question-btn';
            
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
    
    // Professional question display
    displayQuestion(questionIndex) {
        const question = this.questions[questionIndex];
        const container = document.getElementById('questionContent');
        
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        const inputType = isMultiple ? 'checkbox' : 'radio';
        
        container.innerHTML = `
            <div class="question-header-section">
                <div class="question-meta">
                    <div class="question-number-display">Question ${questionIndex + 1}</div>
                    <div class="question-domain-badge">${question.domain}</div>
                </div>
                <div class="question-actions">
                    <button class="action-button ${this.flaggedQuestions.has(questionIndex) ? 'flagged' : ''}" 
                            onclick="professionalExam.toggleFlag(${questionIndex})">
                        🚩 ${this.flaggedQuestions.has(questionIndex) ? 'Unflag' : 'Flag for Review'}
                    </button>
                </div>
            </div>
            
            <div class="question-text-content">
                ${question.text}
                ${isMultiple ? '<div style="background: #e8f4fd; padding: 12px 16px; border-radius: 8px; margin-top: 16px; font-weight: 600; color: #4a90e2;"><strong>📝 Note:</strong> This question may have multiple correct answers. Select all that apply.</div>' : ''}
            </div>
            
            <div class="options-section">
                ${Object.entries(question.options).map(([letter, text]) => `
                    <div class="option-item ${this.isOptionSelected(questionIndex, letter) ? 'selected' : ''}" 
                         onclick="professionalExam.selectOption(${questionIndex}, '${letter}')">
                        <div class="option-content-wrapper">
                            <input type="${inputType}" 
                                   class="option-input-element"
                                   name="q${questionIndex}" 
                                   value="${letter}" 
                                   ${this.isOptionSelected(questionIndex, letter) ? 'checked' : ''}
                                   onchange="professionalExam.handleOptionChange(${questionIndex}, '${letter}', this.checked)">
                            <div class="option-text-content">
                                <span class="option-letter-label">${letter}.</span>
                                ${text}
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        
        this.updateNavigationState();
        this.updateProgress();
        this.updateNavigationButtons();
        
        // Smooth scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    updateNavigationButtons() {
        const prevBtn = document.getElementById('prevButton');
        const nextBtn = document.getElementById('nextButton');
        const submitBtn = document.getElementById('submitButton');
        
        prevBtn.disabled = this.currentQuestion === 0;
        
        if (this.currentQuestion === this.questions.length - 1) {
            nextBtn.style.display = 'none';
            submitBtn.style.display = 'flex';
        } else {
            nextBtn.style.display = 'flex';
            submitBtn.style.display = 'none';
        }
    }
    
    // Answer handling with professional feedback
    selectOption(questionIndex, optionLetter) {
        const question = this.questions[questionIndex];
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        
        if (isMultiple) {
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
            this.answers[questionIndex] = optionLetter;
        }
        
        this.displayQuestion(questionIndex);
        this.saveState();
    }
    
    handleOptionChange(questionIndex, optionLetter, checked) {
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
        this.updateProgress();
        this.saveState();
    }
    
    // Professional progress tracking
    updateProgress() {
        const answered = Object.keys(this.answers).length;
        const total = this.questions.length;
        const flagged = this.flaggedQuestions.size;
        const percentage = (answered / total) * 100;
        
        document.getElementById('progressText').textContent = `Progress: ${answered} of ${total} answered`;
        document.getElementById('flaggedCount').textContent = `Flagged: ${flagged}`;
        document.getElementById('progressBarFill').style.width = `${percentage}%`;
    }
    
    // Enhanced keyboard shortcuts
    bindKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
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
                        const optionLetter = String.fromCharCode(64 + parseInt(e.key));
                        if (this.questions[this.currentQuestion].options[optionLetter]) {
                            this.selectOption(this.currentQuestion, optionLetter);
                        }
                        break;
                    case ' ':
                        e.preventDefault();
                        this.toggleTimer();
                        break;
                }
            }
        });
    }
    
    toggleTimer() {
        this.isPaused = !this.isPaused;
        const btn = document.getElementById('pauseButton');
        btn.textContent = this.isPaused ? 'Resume' : 'Pause';
    }
    
    // Professional review functionality
    showReview() {
        const unanswered = [];
        const flagged = Array.from(this.flaggedQuestions);
        
        for (let i = 0; i < this.questions.length; i++) {
            if (this.answers[i] === undefined) {
                unanswered.push(i + 1);
            }
        }
        
        const reviewModal = document.createElement('div');
        reviewModal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
        `;
        
        reviewModal.innerHTML = `
            <div style="background: white; padding: 32px; border-radius: 16px; max-width: 500px; width: 90%;">
                <h2 style="color: #232f3e; margin-bottom: 24px;">📊 Exam Review</h2>
                <div style="margin-bottom: 20px;">
                    <strong>Progress Summary:</strong><br>
                    Answered: ${Object.keys(this.answers).length}/${this.questions.length}<br>
                    Flagged: ${flagged.length}<br>
                    Unanswered: ${unanswered.length}
                </div>
                ${unanswered.length > 0 ? `<div style="margin-bottom: 20px; color: #f39c12;"><strong>Unanswered:</strong> ${unanswered.join(', ')}</div>` : ''}
                ${flagged.length > 0 ? `<div style="margin-bottom: 20px; color: #f39c12;"><strong>Flagged:</strong> ${flagged.map(i => i + 1).join(', ')}</div>` : ''}
                <div style="display: flex; gap: 12px; justify-content: flex-end;">
                    <button onclick="this.parentElement.parentElement.parentElement.remove()" 
                            style="background: #6c757d; color: white; border: none; padding: 12px 24px; border-radius: 24px; cursor: pointer;">
                        Close
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(reviewModal);
    }
    
    // Professional exam submission
    submitExam(autoSubmit = false) {
        const unanswered = this.questions.length - Object.keys(this.answers).length;
        
        if (!autoSubmit && unanswered > 0) {
            const confirmModal = document.createElement('div');
            confirmModal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.8);
                z-index: 2000;
                display: flex;
                align-items: center;
                justify-content: center;
            `;
            
            confirmModal.innerHTML = `
                <div style="background: white; padding: 32px; border-radius: 16px; max-width: 400px; width: 90%; text-align: center;">
                    <h3 style="color: #232f3e; margin-bottom: 16px;">⚠️ Submit Exam?</h3>
                    <p style="margin-bottom: 24px;">You have ${unanswered} unanswered questions. Are you sure you want to submit?</p>
                    <div style="display: flex; gap: 12px; justify-content: center;">
                        <button onclick="this.parentElement.parentElement.parentElement.remove()" 
                                style="background: #6c757d; color: white; border: none; padding: 12px 24px; border-radius: 24px; cursor: pointer;">
                            Cancel
                        </button>
                        <button onclick="this.parentElement.parentElement.parentElement.remove(); professionalExam.finalSubmit();" 
                                style="background: #e74c3c; color: white; border: none; padding: 12px 24px; border-radius: 24px; cursor: pointer;">
                            Submit Anyway
                        </button>
                    </div>
                </div>
            `;
            
            document.body.appendChild(confirmModal);
            return;
        }
        
        this.finalSubmit();
    }
    
    finalSubmit() {
        clearInterval(this.timerInterval);
        clearInterval(this.autoSaveInterval);
        
        this.calculateResults();
        localStorage.removeItem('saa_professional_exam_state');
    }
    
    calculateResults() {
        let correct = 0;
        let domainStats = {};
        
        const domains = ['Design Secure Architectures', 'Design Resilient Architectures', 
                        'Design High-Performing Architectures', 'Design Cost-Optimized Architectures', 'General'];
        domains.forEach(domain => {
            domainStats[domain] = { correct: 0, total: 0 };
        });
        
        this.questions.forEach((question, index) => {
            const userAnswer = this.answers[index];
            const correctAnswer = question.correct;
            
            domainStats[question.domain].total++;
            
            if (userAnswer !== undefined) {
                let isCorrect = false;
                
                if (Array.isArray(userAnswer)) {
                    const correctAnswers = correctAnswer.split(',').map(a => a.trim());
                    isCorrect = correctAnswers.length === userAnswer.length && 
                               correctAnswers.every(a => userAnswer.includes(a));
                } else {
                    isCorrect = userAnswer === correctAnswer;
                }
                
                if (isCorrect) {
                    correct++;
                    domainStats[question.domain].correct++;
                }
            }
        });
        
        this.displayProfessionalResults(correct, domainStats);
    }
    
    displayProfessionalResults(correct, domainStats) {
        const score = Math.round((correct / this.questions.length) * 1000);
        const percentage = Math.round((correct / this.questions.length) * 100);
        const timeUsed = Math.round((Date.now() - this.startTime) / 60000);
        
        document.querySelector('.main-layout').style.display = 'none';
        document.querySelector('.progress-section').style.display = 'none';
        
        const resultsSection = document.getElementById('resultsSection');
        resultsSection.style.display = 'block';
        
        let domainHTML = '';
        Object.entries(domainStats).forEach(([domain, stats]) => {
            if (stats.total > 0) {
                const domainPercentage = Math.round((stats.correct / stats.total) * 100);
                const domainClass = domainPercentage >= 70 ? 'score-pass' : 'score-fail';
                domainHTML += `
                    <div class="result-card">
                        <div class="card-header">${domain.replace('Design ', '')}</div>
                        <div class="${domainClass}" style="font-size: 1.8em; font-weight: 700;">
                            ${stats.correct}/${stats.total} (${domainPercentage}%)
                        </div>
                        <div style="margin-top: 8px; color: #6c757d;">
                            ${domainPercentage >= 70 ? '✅ Strong performance' : '📚 Needs improvement'}
                        </div>
                    </div>
                `;
            }
        });
        
        resultsSection.innerHTML = `
            <div class="results-container">
                <div class="results-hero">
                    <h1 style="color: #232f3e; margin-bottom: 16px;">🎯 Exam Complete!</h1>
                    <div class="results-score ${score >= 720 ? 'score-pass' : 'score-fail'}">
                        ${score}/1000
                    </div>
                    <div style="font-size: 1.2em; color: #6c757d; margin-bottom: 16px;">
                        ${percentage}% Correct (${correct}/${this.questions.length})
                    </div>
                    <div class="results-message ${score >= 720 ? 'score-pass' : 'score-fail'}">
                        ${score >= 720 ? '🎉 CONGRATULATIONS! YOU PASSED!' : '📚 Keep studying! You need 720 to pass'}
                    </div>
                    <div style="color: #6c757d; margin-top: 16px;">
                        Time Used: ${timeUsed} minutes
                    </div>
                </div>
                
                <div class="results-grid">
                    <div class="result-card">
                        <div class="card-header">📊 Overall Performance</div>
                        <div style="font-size: 1.1em; line-height: 1.8;">
                            <div>Final Score: <strong>${score}/1000</strong></div>
                            <div>Percentage: <strong>${percentage}%</strong></div>
                            <div>Correct Answers: <strong>${correct}/${this.questions.length}</strong></div>
                            <div>Time Used: <strong>${timeUsed} minutes</strong></div>
                            <div>Pass Threshold: <strong>720/1000 (72%)</strong></div>
                        </div>
                    </div>
                    
                    ${domainHTML}
                </div>
                
                <div style="text-align: center; margin: 40px 0;">
                    <button onclick="location.reload()" 
                            style="background: #4a90e2; color: white; border: none; padding: 16px 32px; border-radius: 28px; font-weight: 600; cursor: pointer; margin-right: 16px;">
                        Take Another Exam
                    </button>
                    <button onclick="window.print()" 
                            style="background: #16a085; color: white; border: none; padding: 16px 32px; border-radius: 28px; font-weight: 600; cursor: pointer;">
                        Print Results
                    </button>
                </div>
            </div>
        `;
        
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Global functions
let professionalExam;

function toggleTimer() {
    professionalExam.toggleTimer();
}

function showReview() {
    professionalExam.showReview();
}

function nextQuestion() {
    professionalExam.nextQuestion();
}

function previousQuestion() {
    professionalExam.previousQuestion();
}

function submitExam() {
    professionalExam.submitExam();
}

// Initialize exam
document.addEventListener('DOMContentLoaded', function() {
    professionalExam = new ProfessionalSAAExam(window.examQuestions || []);
});
