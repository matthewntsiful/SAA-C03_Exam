/**
 * Enhanced SAA-C03 Practice Exam System
 * Incorporates all professional improvements and features
 */

class EnhancedSAAExam {
    constructor(questions) {
        this.questions = questions;
        this.currentQuestion = 0;
        this.answers = {};
        this.flaggedQuestions = new Set();
        this.bookmarkedQuestions = new Set();
        this.confidenceLevels = {};
        this.questionNotes = {};
        this.strikethroughOptions = {};
        this.timePerQuestion = {};
        this.timeLeft = 130 * 60;
        this.timerInterval = null;
        this.isPaused = false;
        this.startTime = Date.now();
        this.autoSaveInterval = null;
        this.examMode = 'practice'; // 'practice' or 'simulator'
        this.darkMode = false;
        this.fontSize = 'medium';
        this.achievements = new Set();
        this.studyStreak = 0;
        this.performanceHistory = [];
        
        this.init();
    }
    
    init() {
        this.loadUserPreferences();
        this.loadPerformanceHistory();
        this.generateEnhancedNavigation();
        this.displayQuestion(this.currentQuestion);
        this.updateTimerDisplay();
        this.startTimer();
        this.startAutoSave();
        this.updateProgress();
        this.bindKeyboardShortcuts();
        this.initializeAccessibility();
        this.trackQuestionStartTime();
    }
    
    // Enhanced Auto-save with more data
    startAutoSave() {
        this.autoSaveInterval = setInterval(() => {
            this.saveComprehensiveState();
        }, 15000); // Save every 15 seconds
    }
    
    saveComprehensiveState() {
        const state = {
            currentQuestion: this.currentQuestion,
            answers: this.answers,
            flaggedQuestions: Array.from(this.flaggedQuestions),
            bookmarkedQuestions: Array.from(this.bookmarkedQuestions),
            confidenceLevels: this.confidenceLevels,
            questionNotes: this.questionNotes,
            strikethroughOptions: this.strikethroughOptions,
            timePerQuestion: this.timePerQuestion,
            timeLeft: this.timeLeft,
            examMode: this.examMode,
            timestamp: Date.now()
        };
        localStorage.setItem('saa_enhanced_exam_state', JSON.stringify(state));
    }
    
    loadUserPreferences() {
        const prefs = localStorage.getItem('saa_user_preferences');
        if (prefs) {
            const preferences = JSON.parse(prefs);
            this.darkMode = preferences.darkMode || false;
            this.fontSize = preferences.fontSize || 'medium';
            this.examMode = preferences.examMode || 'practice';
            this.applyUserPreferences();
        }
    }
    
    applyUserPreferences() {
        document.body.classList.toggle('dark-mode', this.darkMode);
        document.body.classList.remove('font-small', 'font-medium', 'font-large');
        document.body.classList.add(`font-${this.fontSize}`);
    }
    
    loadPerformanceHistory() {
        const history = localStorage.getItem('saa_performance_history');
        if (history) {
            this.performanceHistory = JSON.parse(history);
        }
    }
    
    // Enhanced Navigation with all features
    generateEnhancedNavigation() {
        const navGrid = document.getElementById('questionNavGrid');
        navGrid.innerHTML = '';
        
        for (let i = 0; i < this.questions.length; i++) {
            const btn = document.createElement('button');
            btn.className = 'nav-question-btn enhanced';
            btn.innerHTML = `
                <span class="question-number">${i + 1}</span>
                <div class="question-indicators">
                    <span class="bookmark-indicator ${this.bookmarkedQuestions.has(i) ? 'active' : ''}" title="Bookmarked">★</span>
                    <span class="confidence-indicator ${this.getConfidenceClass(i)}" title="Confidence Level"></span>
                </div>
            `;
            btn.onclick = () => this.goToQuestion(i);
            btn.setAttribute('aria-label', `Go to question ${i + 1}`);
            btn.title = this.getQuestionTooltip(i);
            navGrid.appendChild(btn);
        }
        
        this.updateNavigationState();
    }
    
    getConfidenceClass(questionIndex) {
        const confidence = this.confidenceLevels[questionIndex];
        return confidence ? `confidence-${confidence}` : '';
    }
    
    getQuestionTooltip(questionIndex) {
        const parts = [`Question ${questionIndex + 1}`];
        if (this.answers[questionIndex]) parts.push('Answered');
        if (this.flaggedQuestions.has(questionIndex)) parts.push('Flagged');
        if (this.bookmarkedQuestions.has(questionIndex)) parts.push('Bookmarked');
        if (this.confidenceLevels[questionIndex]) parts.push(`Confidence: ${this.confidenceLevels[questionIndex]}`);
        return parts.join(' • ');
    }
    
    // Enhanced Question Display
    displayQuestion(questionIndex) {
        this.trackQuestionTime(questionIndex);
        this.trackQuestionStartTime();
        
        const question = this.questions[questionIndex];
        const container = document.getElementById('questionContent');
        
        const isMultiple = question.correct.length > 1 || question.correct.includes(',');
        const inputType = isMultiple ? 'checkbox' : 'radio';
        const difficulty = this.calculateDifficulty(question);
        
        container.innerHTML = `
            <div class="question-header-section enhanced">
                <div class="question-meta">
                    <div class="question-number-display">
                        Question ${questionIndex + 1}
                        <span class="difficulty-badge ${difficulty}">${difficulty.toUpperCase()}</span>
                    </div>
                    <div class="question-domain-badge">${question.domain}</div>
                    <div class="question-stats">
                        <span class="time-spent" title="Time spent on this question">
                            ⏱️ ${this.getTimeSpent(questionIndex)}
                        </span>
                    </div>
                </div>
                <div class="question-actions enhanced">
                    <button class="action-button flag-btn ${this.flaggedQuestions.has(questionIndex) ? 'flagged' : ''}" 
                            onclick="enhancedExam.toggleFlag(${questionIndex})" title="Flag for review">
                        🚩 ${this.flaggedQuestions.has(questionIndex) ? 'Unflag' : 'Flag'}
                    </button>
                    <button class="action-button bookmark-btn ${this.bookmarkedQuestions.has(questionIndex) ? 'bookmarked' : ''}" 
                            onclick="enhancedExam.toggleBookmark(${questionIndex})" title="Bookmark question">
                        ⭐ ${this.bookmarkedQuestions.has(questionIndex) ? 'Unbookmark' : 'Bookmark'}
                    </button>
                    <button class="action-button notes-btn" 
                            onclick="enhancedExam.showNotesModal(${questionIndex})" title="Add notes">
                        📝 Notes
                    </button>
                </div>
            </div>
            
            <div class="question-text-content enhanced">
                ${question.text}
                ${isMultiple ? `<div class="multiple-choice-notice">📝 <strong>Note:</strong> Choose ${question.correct.split(',').length > 1 ? question.correct.split(',').length : question.correct.length} answers.</div>` : ''}
            </div>
            
            <div class="confidence-section">
                <label>Confidence Level:</label>
                <div class="confidence-buttons">
                    <button class="confidence-btn ${this.confidenceLevels[questionIndex] === 'low' ? 'active' : ''}" 
                            onclick="enhancedExam.setConfidence(${questionIndex}, 'low')">Low</button>
                    <button class="confidence-btn ${this.confidenceLevels[questionIndex] === 'medium' ? 'active' : ''}" 
                            onclick="enhancedExam.setConfidence(${questionIndex}, 'medium')">Medium</button>
                    <button class="confidence-btn ${this.confidenceLevels[questionIndex] === 'high' ? 'active' : ''}" 
                            onclick="enhancedExam.setConfidence(${questionIndex}, 'high')">High</button>
                </div>
            </div>
            
            <div class="options-section enhanced">
                ${Object.entries(question.options).map(([letter, text]) => `
                    <div class="option-item enhanced ${this.isOptionSelected(questionIndex, letter) ? 'selected' : ''} ${this.isOptionStrikethrough(questionIndex, letter) ? 'strikethrough' : ''}" 
                         onclick="enhancedExam.selectOption(${questionIndex}, '${letter}')">
                        <div class="option-content-wrapper">
                            <input type="${inputType}" 
                                   class="option-input-element"
                                   name="q${questionIndex}" 
                                   value="${letter}" 
                                   ${this.isOptionSelected(questionIndex, letter) ? 'checked' : ''}
                                   onchange="enhancedExam.handleOptionChange(${questionIndex}, '${letter}', this.checked)">
                            <div class="option-text-content">
                                <span class="option-letter-label">${letter}.</span>
                                ${text}
                            </div>
                            <button class="strikethrough-btn" 
                                    onclick="event.stopPropagation(); enhancedExam.toggleStrikethrough(${questionIndex}, '${letter}')"
                                    title="Strike through this option">
                                ${this.isOptionStrikethrough(questionIndex, letter) ? '↶' : '✕'}
                            </button>
                        </div>
                    </div>
                `).join('')}
            </div>
            
            ${this.questionNotes[questionIndex] ? `
                <div class="question-notes-display">
                    <strong>Your Notes:</strong> ${this.questionNotes[questionIndex]}
                </div>
            ` : ''}
        `;
        
        this.updateNavigationState();
        this.updateProgress();
        this.updateNavigationButtons();
        
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    calculateDifficulty(question) {
        // Simple difficulty calculation based on text length and domain
        const textLength = question.text.length;
        const optionCount = Object.keys(question.options).length;
        
        if (textLength > 500 || optionCount === 5) return 'hard';
        if (textLength > 250 || question.domain.includes('Secure')) return 'medium';
        return 'easy';
    }
    
    getTimeSpent(questionIndex) {
        const time = this.timePerQuestion[questionIndex] || 0;
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;
        return `${minutes}:${seconds.toString().padStart(2, '0')}`;
    }
    
    trackQuestionStartTime() {
        this.questionStartTime = Date.now();
    }
    
    trackQuestionTime(questionIndex) {
        if (this.questionStartTime && this.currentQuestion !== questionIndex) {
            const timeSpent = Math.floor((Date.now() - this.questionStartTime) / 1000);
            this.timePerQuestion[this.currentQuestion] = (this.timePerQuestion[this.currentQuestion] || 0) + timeSpent;
        }
    }
    
    // Enhanced Features
    toggleBookmark(questionIndex) {
        if (this.bookmarkedQuestions.has(questionIndex)) {
            this.bookmarkedQuestions.delete(questionIndex);
        } else {
            this.bookmarkedQuestions.add(questionIndex);
            this.showNotification('Question bookmarked! ⭐', 'success');
        }
        this.displayQuestion(questionIndex);
        this.saveComprehensiveState();
    }
    
    setConfidence(questionIndex, level) {
        this.confidenceLevels[questionIndex] = level;
        this.displayQuestion(questionIndex);
        this.saveComprehensiveState();
    }
    
    toggleStrikethrough(questionIndex, optionLetter) {
        if (!this.strikethroughOptions[questionIndex]) {
            this.strikethroughOptions[questionIndex] = new Set();
        }
        
        if (this.strikethroughOptions[questionIndex].has(optionLetter)) {
            this.strikethroughOptions[questionIndex].delete(optionLetter);
        } else {
            this.strikethroughOptions[questionIndex].add(optionLetter);
        }
        
        this.displayQuestion(questionIndex);
        this.saveComprehensiveState();
    }
    
    isOptionStrikethrough(questionIndex, optionLetter) {
        return this.strikethroughOptions[questionIndex] && 
               this.strikethroughOptions[questionIndex].has(optionLetter);
    }
    
    showNotesModal(questionIndex) {
        const currentNote = this.questionNotes[questionIndex] || '';
        const modal = document.createElement('div');
        modal.className = 'notes-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <h3>Notes for Question ${questionIndex + 1}</h3>
                <textarea id="noteText" placeholder="Add your notes here..." rows="4">${currentNote}</textarea>
                <div class="modal-buttons">
                    <button onclick="enhancedExam.saveNote(${questionIndex})" class="save-btn">Save</button>
                    <button onclick="enhancedExam.closeModal()" class="cancel-btn">Cancel</button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
        document.getElementById('noteText').focus();
    }
    
    saveNote(questionIndex) {
        const noteText = document.getElementById('noteText').value.trim();
        if (noteText) {
            this.questionNotes[questionIndex] = noteText;
            this.showNotification('Note saved! 📝', 'success');
        } else {
            delete this.questionNotes[questionIndex];
        }
        this.closeModal();
        this.displayQuestion(questionIndex);
        this.saveComprehensiveState();
    }
    
    closeModal() {
        const modal = document.querySelector('.notes-modal');
        if (modal) modal.remove();
    }
    
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 24px;
            background: ${type === 'success' ? '#16a085' : type === 'error' ? '#e74c3c' : '#4a90e2'};
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 600;
            z-index: 1001;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        setTimeout(() => notification.style.transform = 'translateX(0)', 100);
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
    
    // Continue with more methods...
    initializeAccessibility() {
        // Add ARIA labels and keyboard navigation
        document.addEventListener('keydown', this.handleAccessibilityKeys.bind(this));
    }
    
    handleAccessibilityKeys(e) {
        if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
            switch(e.key) {
                case 'b':
                case 'B':
                    e.preventDefault();
                    this.toggleBookmark(this.currentQuestion);
                    break;
                case 'n':
                case 'N':
                    e.preventDefault();
                    this.showNotesModal(this.currentQuestion);
                    break;
                case 'd':
                case 'D':
                    e.preventDefault();
                    this.toggleDarkMode();
                    break;
            }
        }
    }
    
    toggleDarkMode() {
        this.darkMode = !this.darkMode;
        this.applyUserPreferences();
        this.saveUserPreferences();
        this.showNotification(`Dark mode ${this.darkMode ? 'enabled' : 'disabled'}`, 'info');
    }
    
    
    showSettingsModal() {
        const modal = document.createElement('div');
        modal.className = 'settings-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <h3>⚙️ Exam Settings</h3>
                <div class="settings-group">
                    <label>Font Size:</label>
                    <div class="font-size-buttons">
                        <button class="setting-btn ${this.fontSize === 'small' ? 'active' : ''}" onclick="enhancedExam.setFontSize('small')">Small</button>
                        <button class="setting-btn ${this.fontSize === 'medium' ? 'active' : ''}" onclick="enhancedExam.setFontSize('medium')">Medium</button>
                        <button class="setting-btn ${this.fontSize === 'large' ? 'active' : ''}" onclick="enhancedExam.setFontSize('large')">Large</button>
                    </div>
                </div>
                <div class="settings-group">
                    <label>Exam Mode:</label>
                    <div class="mode-buttons">
                        <button class="setting-btn ${this.examMode === 'practice' ? 'active' : ''}" onclick="enhancedExam.setExamMode('practice')">Practice</button>
                        <button class="setting-btn ${this.examMode === 'simulator' ? 'active' : ''}" onclick="enhancedExam.setExamMode('simulator')">Simulator</button>
                    </div>
                </div>
                <div class="modal-buttons">
                    <button onclick="enhancedExam.closeModal()" class="cancel-btn">Close</button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    }
    
    setFontSize(size) {
        this.fontSize = size;
        this.applyUserPreferences();
        this.saveUserPreferences();
        this.showNotification(`Font size set to ${size}`, 'success');
    }
    
    setExamMode(mode) {
        this.examMode = mode;
        this.saveUserPreferences();
        this.showNotification(`Exam mode: ${mode}`, 'info');
        if (mode === 'simulator') {
            this.showNotification('Simulator mode: No pause, strict timing', 'warning');
        }
    }
    
    showExplanation() {
        const question = this.questions[this.currentQuestion];
        if (question.explanation) {
            const modal = document.createElement('div');
            modal.className = 'explanation-modal';
            modal.innerHTML = `
                <div class="modal-content">
                    <h3>💡 Explanation - Question ${this.currentQuestion + 1}</h3>
                    <div class="explanation-content">
                        <p><strong>Correct Answer:</strong> ${question.correct}</p>
                        <p>${question.explanation || 'Detailed explanation not available for this question.'}</p>
                        ${question.documentation_links.length > 0 ? `
                            <div class="doc-links">
                                <strong>📚 AWS Documentation:</strong>
                                ${question.documentation_links.map(link => `<a href="${link}" target="_blank">${link}</a>`).join('<br>')}
                            </div>
                        ` : ''}
                    </div>
                    <div class="modal-buttons">
                        <button onclick="enhancedExam.closeModal()" class="cancel-btn">Close</button>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
        } else {
            this.showNotification('Explanation not available', 'info');
        }
    }
    
    // Enhanced timer with simulator mode
    startTimer() {
        this.timerInterval = setInterval(() => {
            if (!this.isPaused || this.examMode === 'simulator') {
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
    
    toggleTimer() {
        if (this.examMode === 'simulator') {
            this.showNotification('Timer cannot be paused in simulator mode', 'warning');
            return;
        }
        
        this.isPaused = !this.isPaused;
        const btn = document.getElementById('pauseButton');
        btn.textContent = this.isPaused ? 'Resume' : 'Pause';
    }
    
    // Enhanced progress update
    updateProgress() {
        const answered = Object.keys(this.answers).length;
        const total = this.questions.length;
        const flagged = this.flaggedQuestions.size;
        const bookmarked = this.bookmarkedQuestions.size;
        const percentage = (answered / total) * 100;
        
        // Count confidence levels
        const confidenceStats = { high: 0, medium: 0, low: 0 };
        Object.values(this.confidenceLevels).forEach(level => {
            confidenceStats[level]++;
        });
        
        // Count difficulty levels
        const difficultyStats = { easy: 0, medium: 0, hard: 0 };
        this.questions.forEach(q => {
            difficultyStats[q.difficulty]++;
        });
        
        document.getElementById('progressText').textContent = `Progress: ${answered} of ${total} answered`;
        document.getElementById('flaggedCount').textContent = `Flagged: ${flagged}`;
        document.getElementById('bookmarkedCount').textContent = `Bookmarked: ${bookmarked}`;
        document.getElementById('confidenceStats').textContent = `Confidence: High: ${confidenceStats.high}, Medium: ${confidenceStats.medium}, Low: ${confidenceStats.low}`;
        document.getElementById('progressBarFill').style.width = `${percentage}%`;
        
        // Update sidebar stats
        if (document.getElementById('easyCount')) {
            document.getElementById('easyCount').textContent = difficultyStats.easy;
            document.getElementById('mediumCount').textContent = difficultyStats.medium;
            document.getElementById('hardCount').textContent = difficultyStats.hard;
        }
    }
    
    // Enhanced navigation methods
    goToQuestion(questionIndex) {
        this.trackQuestionTime(this.currentQuestion);
        this.currentQuestion = questionIndex;
        this.displayQuestion(questionIndex);
    }
    
    nextQuestion() {
        if (this.currentQuestion < this.questions.length - 1) {
            this.goToQuestion(this.currentQuestion + 1);
        }
    }
    
    previousQuestion() {
        if (this.currentQuestion > 0) {
            this.goToQuestion(this.currentQuestion - 1);
        }
    }
    
    // Enhanced flag functionality
    toggleFlag(questionIndex) {
        if (this.flaggedQuestions.has(questionIndex)) {
            this.flaggedQuestions.delete(questionIndex);
            this.showNotification('Question unflagged', 'info');
        } else {
            this.flaggedQuestions.add(questionIndex);
            this.showNotification('Question flagged for review! 🚩', 'warning');
        }
        
        this.displayQuestion(questionIndex);
        this.updateProgress();
        this.saveComprehensiveState();
    }
    
    // Enhanced answer selection
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
        this.saveComprehensiveState();
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
        this.saveComprehensiveState();
    }
    
    isOptionSelected(questionIndex, optionLetter) {
        const answer = this.answers[questionIndex];
        if (Array.isArray(answer)) {
            return answer.includes(optionLetter);
        }
        return answer === optionLetter;
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
}

// Global instance
let enhancedExam;

// Global functions for HTML onclick handlers
function toggleTimer() { enhancedExam.toggleTimer(); }
function showReview() { enhancedExam.showReview(); }
function nextQuestion() { enhancedExam.nextQuestion(); }
function previousQuestion() { enhancedExam.previousQuestion(); }
function submitExam() { enhancedExam.submitExam(); }

// Initialize enhanced exam
document.addEventListener('DOMContentLoaded', function() {
    enhancedExam = new EnhancedSAAExam(window.examQuestions || []);
});
