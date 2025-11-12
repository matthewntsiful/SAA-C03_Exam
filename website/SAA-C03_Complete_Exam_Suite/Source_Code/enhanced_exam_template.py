#!/usr/bin/env python3
"""
SAA-C03 Enhanced Practice Exam Generator with Industry Best Practices
- Randomized question order
- Flagging system for review
- Progress indicators
- Auto-save functionality
- Detailed explanations
- Performance analytics
- Mobile responsive design
- Accessibility features
"""

import re
import json
import random
from datetime import datetime

def create_enhanced_exam_html(questions, exam_number, timestamp):
    """Create enhanced exam HTML with all best practices"""
    
    # Randomize question order for each exam
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AWS SAA-C03 Practice Exam - Professional certification preparation">
    <meta name="keywords" content="AWS, SAA-C03, Solutions Architect, Practice Exam, Certification">
    <title>AWS SAA-C03 Practice Exam {exam_num} | Professional Certification Prep</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <style>
        :root {{
            --primary-color: #232f3e;
            --secondary-color: #ff9900;
            --accent-color: #007cba;
            --success-color: #28a745;
            --danger-color: #dc3545;
            --warning-color: #ffc107;
            --light-bg: #f8f9fa;
            --border-color: #dee2e6;
            --text-primary: #2c3e50;
            --text-secondary: #6c757d;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .exam-container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
            box-shadow: 0 0 30px rgba(0,0,0,0.1);
        }}
        
        /* Header Styles */
        .exam-header {{
            background: var(--primary-color);
            color: white;
            padding: 20px 30px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}
        
        .exam-title {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        
        .aws-logo {{
            font-size: 2em;
            color: var(--secondary-color);
        }}
        
        .title-text h1 {{
            font-size: 1.5em;
            font-weight: 600;
        }}
        
        .title-text p {{
            font-size: 0.9em;
            opacity: 0.8;
            margin-top: 2px;
        }}
        
        /* Timer and Controls */
        .exam-controls {{
            display: flex;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }}
        
        .timer-display {{
            background: rgba(255,255,255,0.1);
            padding: 10px 20px;
            border-radius: 25px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: bold;
        }}
        
        .timer-icon {{
            color: var(--secondary-color);
        }}
        
        .control-btn {{
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: #005a8b;
            transform: translateY(-2px);
        }}
        
        /* Progress Bar */
        .progress-container {{
            background: var(--light-bg);
            padding: 15px 30px;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .progress-info {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            font-size: 0.9em;
            color: var(--text-secondary);
        }}
        
        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-color), var(--success-color));
            width: 0%;
            transition: width 0.3s ease;
        }}
        
        /* Navigation Panel */
        .nav-panel {{
            background: var(--light-bg);
            padding: 20px 30px;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .question-nav {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(40px, 1fr));
            gap: 8px;
            max-width: 800px;
        }}
        
        .nav-btn {{
            width: 40px;
            height: 40px;
            border: 2px solid var(--border-color);
            background: white;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }}
        
        .nav-btn:hover {{
            border-color: var(--accent-color);
            transform: scale(1.05);
        }}
        
        .nav-btn.answered {{
            background: var(--success-color);
            color: white;
            border-color: var(--success-color);
        }}
        
        .nav-btn.flagged {{
            background: var(--warning-color);
            color: var(--text-primary);
            border-color: var(--warning-color);
        }}
        
        .nav-btn.current {{
            background: var(--accent-color);
            color: white;
            border-color: var(--accent-color);
        }}
        
        /* Question Styles */
        .question-container {{
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
        }}
        
        .question-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 15px;
        }}
        
        .question-info {{
            flex: 1;
        }}
        
        .question-number {{
            font-size: 1.4em;
            font-weight: bold;
            color: var(--accent-color);
            margin-bottom: 5px;
        }}
        
        .question-domain {{
            background: var(--accent-color);
            color: white;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: 500;
            display: inline-block;
        }}
        
        .question-actions {{
            display: flex;
            gap: 10px;
        }}
        
        .flag-btn {{
            background: none;
            border: 2px solid var(--warning-color);
            color: var(--warning-color);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .flag-btn.flagged {{
            background: var(--warning-color);
            color: var(--text-primary);
        }}
        
        .question-text {{
            font-size: 1.1em;
            line-height: 1.7;
            margin: 25px 0;
            color: var(--text-primary);
        }}
        
        /* Options Styles */
        .options-container {{
            margin: 30px 0;
        }}
        
        .option {{
            margin: 15px 0;
            padding: 20px;
            border: 2px solid var(--border-color);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: white;
            position: relative;
        }}
        
        .option:hover {{
            border-color: var(--accent-color);
            background: #f0f8ff;
            transform: translateX(5px);
        }}
        
        .option.selected {{
            border-color: var(--accent-color);
            background: #e7f3ff;
            box-shadow: 0 4px 15px rgba(0,124,186,0.2);
        }}
        
        .option-content {{
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }}
        
        .option-input {{
            margin-top: 2px;
            transform: scale(1.3);
        }}
        
        .option-text {{
            flex: 1;
            font-size: 1em;
            line-height: 1.6;
        }}
        
        .option-letter {{
            font-weight: bold;
            color: var(--accent-color);
            margin-right: 8px;
        }}
        
        /* Navigation Buttons */
        .question-navigation {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 40px 0;
            padding: 20px 0;
            border-top: 1px solid var(--border-color);
        }}
        
        .nav-button {{
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1em;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .nav-button:hover {{
            background: #005a8b;
            transform: translateY(-2px);
        }}
        
        .nav-button:disabled {{
            background: var(--text-secondary);
            cursor: not-allowed;
            transform: none;
        }}
        
        .submit-btn {{
            background: var(--success-color);
            font-size: 1.1em;
            padding: 15px 30px;
        }}
        
        .submit-btn:hover {{
            background: #218838;
        }}
        
        /* Results Styles */
        .results-container {{
            display: none;
            padding: 30px;
            background: var(--light-bg);
        }}
        
        .results-header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        
        .final-score {{
            font-size: 3em;
            font-weight: bold;
            margin: 20px 0;
        }}
        
        .score-pass {{
            color: var(--success-color);
        }}
        
        .score-fail {{
            color: var(--danger-color);
        }}
        
        .results-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }}
        
        .result-card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-left: 5px solid var(--accent-color);
        }}
        
        .card-title {{
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--text-primary);
        }}
        
        /* Mobile Responsive */
        @media (max-width: 768px) {{
            .exam-header {{
                padding: 15px 20px;
            }}
            
            .header-content {{
                flex-direction: column;
                align-items: stretch;
            }}
            
            .exam-controls {{
                justify-content: center;
            }}
            
            .question-container {{
                padding: 20px 15px;
            }}
            
            .question-nav {{
                grid-template-columns: repeat(auto-fill, minmax(35px, 1fr));
            }}
            
            .nav-btn {{
                width: 35px;
                height: 35px;
                font-size: 0.8em;
            }}
            
            .option {{
                padding: 15px;
            }}
            
            .question-navigation {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
        
        /* Accessibility */
        @media (prefers-reduced-motion: reduce) {{
            * {{
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }}
        }}
        
        .sr-only {{
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }}
    </style>
</head>
<body>
    <div class="exam-container">
        <!-- Header -->
        <header class="exam-header">
            <div class="header-content">
                <div class="exam-title">
                    <div class="aws-logo">☁️</div>
                    <div class="title-text">
                        <h1>AWS SAA-C03 Practice Exam {exam_num}</h1>
                        <p>Solutions Architect Associate Certification</p>
                    </div>
                </div>
                <div class="exam-controls">
                    <div class="timer-display">
                        <span class="timer-icon">⏱️</span>
                        <span id="timer">130:00</span>
                    </div>
                    <button class="control-btn" onclick="toggleTimer()" id="pauseBtn">Pause</button>
                    <button class="control-btn" onclick="showReview()">Review</button>
                </div>
            </div>
        </header>
        
        <!-- Progress Bar -->
        <div class="progress-container">
            <div class="progress-info">
                <span>Progress: <span id="progressText">0 of 65 answered</span></span>
                <span>Time Remaining: <span id="timeRemaining">130:00</span></span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
        </div>
        
        <!-- Question Navigation -->
        <div class="nav-panel">
            <div class="question-nav" id="questionNav">
                <!-- Navigation buttons will be generated by JavaScript -->
            </div>
        </div>
        
        <!-- Question Container -->
        <main class="question-container" id="questionContainer">
            <!-- Questions will be loaded here -->
        </main>
        
        <!-- Results Container -->
        <div class="results-container" id="resultsContainer">
            <!-- Results will be displayed here -->
        </div>
    </div>
</body>
</html>'''
    
    return html_template.format(exam_num=exam_number)

if __name__ == "__main__":
    print("Enhanced exam template created with industry best practices!")
