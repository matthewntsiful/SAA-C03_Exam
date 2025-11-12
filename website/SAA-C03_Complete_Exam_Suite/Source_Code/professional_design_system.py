#!/usr/bin/env python3
"""
Professional Design System for SAA-C03 Exam Suite
Implements consistent branding and UX across all components
"""

def get_professional_css():
    """Professional CSS design system"""
    return '''
        :root {
            --aws-orange: #ff9900;
            --aws-blue: #232f3e;
            --aws-light-blue: #4a90e2;
            --aws-dark-blue: #161e2d;
            --success-green: #16a085;
            --warning-orange: #f39c12;
            --danger-red: #e74c3c;
            --light-gray: #f8f9fa;
            --medium-gray: #6c757d;
            --dark-gray: #343a40;
            --border-light: #e9ecef;
            --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.15);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.2);
            --border-radius: 8px;
            --border-radius-lg: 12px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            --font-mono: 'SF Mono', 'Monaco', 'Cascadia Code', monospace;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: var(--font-primary);
            line-height: 1.6;
            color: var(--dark-gray);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-size: 16px;
        }
        
        /* Professional Header */
        .professional-header {
            background: var(--aws-blue);
            color: white;
            padding: 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow-lg);
        }
        
        .header-top {
            background: var(--aws-dark-blue);
            padding: 8px 0;
            font-size: 0.85em;
        }
        
        .header-top-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .certification-badge {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--aws-orange);
            font-weight: 600;
        }
        
        .cert-icon {
            width: 24px;
            height: 24px;
            background: var(--aws-orange);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }
        
        .suite-info {
            color: #ccc;
            font-size: 0.8em;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .header-main {
            padding: 16px 0;
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .brand-section {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .aws-logo {
            width: 48px;
            height: 48px;
            background: var(--aws-orange);
            border-radius: var(--border-radius);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        
        .brand-text h1 {
            font-size: 1.6em;
            font-weight: 700;
            margin-bottom: 4px;
            background: linear-gradient(135deg, #ffffff, #f0f0f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .brand-text p {
            font-size: 0.95em;
            opacity: 0.9;
            color: #e0e0e0;
            font-weight: 500;
        }
        
        .header-controls {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .timer-section {
            background: rgba(255,255,255,0.1);
            padding: 12px 20px;
            border-radius: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
            backdrop-filter: blur(10px);
        }
        
        .timer-display {
            font-family: var(--font-mono);
            font-size: 1.1em;
            font-weight: 700;
            color: var(--aws-orange);
        }
        
        .control-button {
            background: var(--aws-light-blue);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            font-size: 0.9em;
        }
        
        .control-button:hover {
            background: #357abd;
            transform: translateY(-1px);
        }
        
        /* Professional Progress Bar */
        .progress-section {
            background: white;
            border-bottom: 1px solid var(--border-light);
        }
        
        .progress-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 16px 24px;
        }
        
        .progress-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            font-size: 0.9em;
            color: var(--medium-gray);
        }
        
        .progress-stats {
            display: flex;
            gap: 24px;
        }
        
        .progress-bar-container {
            width: 100%;
            height: 6px;
            background: #e9ecef;
            border-radius: 3px;
            overflow: hidden;
        }
        
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--aws-light-blue), var(--success-green));
            width: 0%;
            transition: width 0.4s ease;
        }
        
        /* Left Sidebar Question Navigation */
        .main-layout {
            display: flex;
            min-height: calc(100vh - 200px);
        }
        
        .question-sidebar {
            width: 200px;
            background: var(--light-gray);
            border-right: 1px solid var(--border-light);
            padding: 20px 16px;
            position: sticky;
            top: 200px;
            height: fit-content;
            max-height: calc(100vh - 220px);
            overflow-y: auto;
        }
        
        .sidebar-header {
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border-light);
        }
        
        .sidebar-title {
            font-weight: 600;
            color: var(--dark-gray);
            font-size: 0.9em;
            margin-bottom: 8px;
        }
        
        .sidebar-legend {
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: 0.75em;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .legend-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            flex-shrink: 0;
        }
        
        .legend-dot.answered { background: var(--success-green); }
        .legend-dot.flagged { background: var(--warning-orange); }
        .legend-dot.current { background: var(--aws-light-blue); }
        .legend-dot.unanswered { background: white; border: 2px solid var(--border-light); }
        
        .question-nav-sidebar {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 6px;
            margin-top: 4px;
        }
        
        .nav-question-btn {
            width: 32px;
            height: 32px;
            border: 2px solid var(--border-light);
            background: white;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.8em;
            transition: var(--transition);
            position: relative;
        }
        
        .nav-question-btn:hover {
            border-color: var(--aws-light-blue);
            transform: scale(1.1);
            box-shadow: var(--shadow-sm);
        }
        
        .nav-question-btn.answered {
            background: var(--success-green);
            color: white;
            border-color: var(--success-green);
        }
        
        .nav-question-btn.flagged {
            background: var(--warning-orange);
            color: white;
            border-color: var(--warning-orange);
        }
        
        .nav-question-btn.current {
            background: var(--aws-light-blue);
            color: white;
            border-color: var(--aws-light-blue);
            box-shadow: var(--shadow-md);
            transform: scale(1.1);
        }
        
        /* Main Content Area */
        .content-area {
            flex: 1;
            background: white;
        }
        
        /* Professional Main Content */
        .main-container {
            background: white;
            min-height: calc(100vh - 200px);
        }
        
        .question-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 32px 24px;
        }
        
        .question-header-section {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 32px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-light);
        }
        
        .question-meta {
            flex: 1;
        }
        
        .question-number-display {
            font-size: 1.8em;
            font-weight: 700;
            color: var(--aws-blue);
            margin-bottom: 8px;
        }
        
        .question-domain-badge {
            background: linear-gradient(135deg, var(--aws-light-blue), var(--aws-blue));
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
            display: inline-block;
        }
        
        .question-actions {
            display: flex;
            gap: 12px;
        }
        
        .action-button {
            background: none;
            border: 2px solid var(--warning-orange);
            color: var(--warning-orange);
            padding: 10px 20px;
            border-radius: 24px;
            cursor: pointer;
            font-weight: 600;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .action-button.flagged {
            background: var(--warning-orange);
            color: white;
        }
        
        .action-button:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-sm);
        }
        
        .question-text-content {
            font-size: 1.1em;
            line-height: 1.8;
            color: var(--dark-gray);
            margin: 32px 0;
        }
        
        /* Professional Options */
        .options-section {
            margin: 32px 0;
        }
        
        .option-item {
            margin: 16px 0;
            padding: 20px 24px;
            border: 2px solid var(--border-light);
            border-radius: var(--border-radius-lg);
            cursor: pointer;
            transition: var(--transition);
            background: white;
            position: relative;
        }
        
        .option-item:hover {
            border-color: var(--aws-light-blue);
            background: #f8fbff;
            transform: translateX(4px);
        }
        
        .option-item.selected {
            border-color: var(--aws-light-blue);
            background: #e8f4fd;
            box-shadow: var(--shadow-md);
        }
        
        .option-content-wrapper {
            display: flex;
            align-items: flex-start;
            gap: 16px;
        }
        
        .option-input-element {
            margin-top: 4px;
            transform: scale(1.4);
        }
        
        .option-text-content {
            flex: 1;
            font-size: 1em;
            line-height: 1.7;
        }
        
        .option-letter-label {
            font-weight: 700;
            color: var(--aws-blue);
            margin-right: 12px;
        }
        
        /* Professional Navigation */
        .bottom-navigation {
            background: var(--light-gray);
            border-top: 1px solid var(--border-light);
            padding: 24px 0;
        }
        
        .nav-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .nav-btn-primary {
            background: var(--aws-light-blue);
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 28px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1em;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-btn-primary:hover {
            background: #357abd;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .nav-btn-primary:disabled {
            background: var(--medium-gray);
            cursor: not-allowed;
            transform: none;
        }
        
        .submit-button {
            background: var(--success-green);
            font-size: 1.1em;
            padding: 16px 32px;
        }
        
        .submit-button:hover {
            background: #138d75;
        }
        
        /* Professional Results */
        .results-section {
            display: none;
            background: var(--light-gray);
            min-height: 100vh;
            padding: 32px 0;
        }
        
        .results-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 24px;
        }
        
        .results-hero {
            background: white;
            padding: 48px;
            border-radius: var(--border-radius-lg);
            text-align: center;
            margin-bottom: 32px;
            box-shadow: var(--shadow-lg);
        }
        
        .results-score {
            font-size: 4em;
            font-weight: 800;
            margin: 24px 0;
        }
        
        .score-pass { color: var(--success-green); }
        .score-fail { color: var(--danger-red); }
        
        .results-message {
            font-size: 1.3em;
            margin: 24px 0;
            font-weight: 600;
        }
        
        .results-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
            margin: 32px 0;
        }
        
        .result-card {
            background: white;
            padding: 28px;
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-md);
            border-left: 4px solid var(--aws-light-blue);
        }
        
        .card-header {
            font-size: 1.2em;
            font-weight: 700;
            margin-bottom: 16px;
            color: var(--aws-blue);
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                align-items: stretch;
                gap: 16px;
            }
            
            .header-controls {
                justify-content: center;
            }
            
            .main-layout {
                flex-direction: column;
            }
            
            .question-sidebar {
                width: 100%;
                position: static;
                max-height: none;
                padding: 16px;
                border-right: none;
                border-bottom: 1px solid var(--border-light);
            }
            
            .sidebar-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .sidebar-legend {
                flex-direction: row;
                gap: 12px;
            }
            
            .question-nav-sidebar {
                grid-template-columns: repeat(10, 1fr);
                gap: 4px;
            }
            
            .nav-question-btn {
                width: 28px;
                height: 28px;
                font-size: 0.7em;
            }
            
            .question-content {
                padding: 24px 16px;
            }
            
            .question-header-section {
                flex-direction: column;
                gap: 16px;
            }
            
            .nav-content {
                flex-direction: column;
                gap: 16px;
            }
            
            .results-hero {
                padding: 32px 24px;
            }
            
            .results-score {
                font-size: 2.5em;
            }
        }
        
        /* Accessibility */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
        
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }
        
        /* Print Styles */
        @media print {
            .professional-header,
            .question-nav-section,
            .bottom-navigation {
                display: none;
            }
            
            .main-container {
                box-shadow: none;
            }
        }
    '''

def get_professional_html_template():
    """Professional HTML template with horizontal navigation"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AWS SAA-C03 Associate Practice Exam - Industry standard Solutions Architect Associate certification preparation">
    <meta name="keywords" content="AWS, SAA-C03, Solutions Architect Associate, Practice Exam, Certification Prep">
    <title>AWS SAA-C03 Associate Practice Exam {exam_number:02d} | Solutions Architect Certification</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <style>
        {css_content}
    </style>
</head>
<body>
    <!-- Professional Header -->
    <header class="professional-header">
        <div class="header-top">
            <div class="header-top-content">
                <div class="certification-badge">
                    <div class="cert-icon">🎯</div>
                    <span>AWS Certified Solutions Architect Associate (SAA-C03)</span>
                </div>
                <div class="suite-info">
                    <span>🏆</span>
                    <span>Industry Standard Practice Exam Suite</span>
                </div>
            </div>
        </div>
        
        <div class="header-main">
            <div class="header-content">
                <div class="brand-section">
                    <div class="aws-logo">AWS</div>
                    <div class="brand-text">
                        <h1>SAA-C03 Associate Practice Exam {exam_number:02d}</h1>
                        <p>Solutions Architect Associate • Certification Preparation</p>
                    </div>
                </div>
                
                <div class="header-controls">
                    <div class="timer-section">
                        <span style="color: #ff9900;">⏱️</span>
                        <div class="timer-display" id="timerDisplay">130:00</div>
                    </div>
                    <button class="control-button" onclick="toggleTimer()" id="pauseButton">Pause</button>
                    <button class="control-button" onclick="showReview()">Review</button>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Progress Section -->
    <div class="progress-section">
        <div class="progress-container">
            <div class="progress-header">
                <div class="progress-stats">
                    <span id="progressText">Progress: 0 of 65 answered</span>
                    <span id="flaggedCount">Flagged: 0</span>
                </div>
                <div style="color: #ff9900; font-weight: 600;">
                    Time Remaining: <span id="timeRemaining">130:00</span>
                </div>
            </div>
            <div class="progress-bar-container">
                <div class="progress-bar-fill" id="progressBarFill"></div>
            </div>
        </div>
    </div>
    
    <!-- Main Layout with Left Sidebar -->
    <div class="main-layout">
        <!-- Left Question Navigation Sidebar -->
        <aside class="question-sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title">Questions</div>
                <div class="sidebar-legend">
                    <div class="legend-item">
                        <div class="legend-dot current"></div>
                        <span>Current</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-dot answered"></div>
                        <span>Answered</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-dot flagged"></div>
                        <span>Flagged</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-dot unanswered"></div>
                        <span>Unanswered</span>
                    </div>
                </div>
            </div>
            <div class="question-nav-sidebar" id="questionNavGrid">
                <!-- Navigation buttons will be generated by JavaScript -->
            </div>
        </aside>
        
        <!-- Main Content Area -->
        <div class="content-area">
            <div class="question-content" id="questionContent">
                <!-- Question content will be loaded here -->
            </div>
            
            <!-- Bottom Navigation -->
            <div class="bottom-navigation">
                <div class="nav-content">
                    <button class="nav-btn-primary" onclick="previousQuestion()" id="prevButton">
                        ← Previous Question
                    </button>
                    
                    <div style="display: flex; gap: 16px;">
                        <button class="nav-btn-primary" onclick="nextQuestion()" id="nextButton">
                            Next Question →
                        </button>
                        <button class="nav-btn-primary submit-button" onclick="submitExam()" id="submitButton" style="display: none;">
                            Submit Exam
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Results Section -->
    <div class="results-section" id="resultsSection">
        <!-- Results will be displayed here -->
    </div>

    <script>
        // Questions data will be injected here
        window.examQuestions = {questions_json};
        
        {javascript_content}
    </script>
</body>
</html>'''

if __name__ == "__main__":
    print("Professional design system created!")
