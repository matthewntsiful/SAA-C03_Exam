// Progress tracking functionality
class ExamProgress {
    constructor() {
        this.loadProgress();
        this.updateUI();
    }

    loadProgress() {
        this.progress = JSON.parse(localStorage.getItem('examProgress') || '{}');
    }

    saveProgress() {
        localStorage.setItem('examProgress', JSON.stringify(this.progress));
    }

    updateExamProgress(examId, score, completed = false) {
        console.log(`Updating exam ${examId}: score=${score}, completed=${completed}`);
        if (!this.progress[examId]) {
            this.progress[examId] = { attempts: 0, scores: [] };
        }
        this.progress[examId].score = score;
        this.progress[examId].completed = completed;
        this.progress[examId].lastTaken = new Date().toISOString();
        this.progress[examId].attempts = (this.progress[examId].attempts || 0) + 1;
        this.progress[examId].scores = this.progress[examId].scores || [];
        this.progress[examId].scores.push(score);
        this.saveProgress();
        this.updateUI();
    }

    updateUI() {
        Object.keys(this.progress).forEach(examId => {
            const data = this.progress[examId];
            const statusEl = document.getElementById(`status-${examId}`);
            const scoreEl = document.getElementById(`score-${examId}`);
            const progressEl = document.getElementById(`progress-${examId}`);
            const progressBarEl = document.getElementById(`progress-bar-${examId}`);
            const btnEl = document.getElementById(`exam-btn-${examId}`);

            if (statusEl && scoreEl && progressEl && progressBarEl && btnEl) {
                if (data.completed) {
                    statusEl.className = data.score >= 70 ? 
                        'w-3 h-3 bg-green-500 rounded-full' : 
                        'w-3 h-3 bg-red-500 rounded-full';
                    scoreEl.textContent = `${data.score}%`;
                    progressEl.textContent = '100%';
                    progressBarEl.style.width = '100%';
                    progressBarEl.className = data.score >= 70 ? 
                        'bg-green-500 h-2 rounded-full transition-all duration-300' :
                        'bg-red-500 h-2 rounded-full transition-all duration-300';
                    btnEl.textContent = 'Retake Exam';
                } else {
                    statusEl.className = 'w-3 h-3 bg-yellow-500 rounded-full';
                    scoreEl.textContent = 'In progress';
                    progressEl.textContent = '50%';
                    progressBarEl.style.width = '50%';
                    btnEl.textContent = 'Continue Exam';
                }
            }
        });
    }
}

// Initialize progress tracking
document.addEventListener('DOMContentLoaded', () => {
    window.examProgress = new ExamProgress();
    
    // Demo data for testing
    if (Object.keys(window.examProgress.progress).length === 0) {
        window.examProgress.updateExamProgress('1', 85, true);
        window.examProgress.updateExamProgress('3', 65, true);
        window.examProgress.updateExamProgress('5', 0, false);
        
        // Add demo recent exams
        const recentExams = [
            { id: '5', title: 'Exam 5', startTime: new Date().toISOString(), lastAccessed: new Date().toISOString() },
            { id: '2', title: 'Exam 2', startTime: new Date(Date.now() - 3600000).toISOString(), lastAccessed: new Date(Date.now() - 3600000).toISOString() }
        ];
        localStorage.setItem('recentExams', JSON.stringify(recentExams));
        
        // Force show recent exams section
        setTimeout(() => {
            const section = document.getElementById('recent-exams-section');
            if (section) section.style.display = 'block';
        }, 100);
    }
});