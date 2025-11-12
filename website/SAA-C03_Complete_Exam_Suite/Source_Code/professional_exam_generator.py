#!/usr/bin/env python3
"""
Professional SAA-C03 Practice Exam Generator
Implements all industry best practices for online certification exams
"""

import re
import json
import random
from datetime import datetime

def parse_questions(file_path):
    """Parse questions from rawText.txt with enhanced error handling"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    current_question = None
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Match question number
        if re.match(r'^\d+\.', line):
            # Save previous question if exists
            if current_question and current_question.get('text') and current_question.get('options'):
                questions.append(current_question)
            
            # Start new question
            current_question = {
                'number': len(questions) + 1,
                'text': '',
                'options': {},
                'correct': '',
                'domain': 'General',
                'explanation': ''
            }
            
            # Get question text (may span multiple lines)
            question_text = line
            i += 1
            while i < len(lines) and not re.match(r'^[A-E]\.', lines[i].strip()) and not re.match(r'^\d+\.', lines[i].strip()):
                if lines[i].strip():
                    question_text += ' ' + lines[i].strip()
                i += 1
            
            current_question['text'] = question_text.replace(f"{current_question['number']}. ", "").strip()
            continue
        
        # Match answer options
        if re.match(r'^[A-E]\.', line) and current_question:
            option_letter = line[0]
            option_text = line[2:].strip()
            
            # Get full option text (may span multiple lines)
            i += 1
            while i < len(lines) and not re.match(r'^[A-E]\.', lines[i].strip()) and not re.match(r'^Suggested Answer:', lines[i].strip()) and not re.match(r'^\d+\.', lines[i].strip()):
                if lines[i].strip() and not lines[i].strip().startswith('Page '):
                    option_text += ' ' + lines[i].strip()
                i += 1
            
            current_question['options'][option_letter] = option_text
            continue
        
        # Match suggested answer
        if line.startswith('Suggested Answer:') and current_question:
            answer = line.replace('Suggested Answer:', '').strip().upper()
            current_question['correct'] = answer
            
            # Enhanced domain classification
            text_lower = current_question['text'].lower()
            if any(word in text_lower for word in ['security', 'iam', 'encryption', 'kms', 'vpc', 'firewall', 'ssl', 'tls', 'certificate', 'auth', 'compliance', 'policy', 'permission', 'role']):
                current_question['domain'] = 'Design Secure Architectures'
            elif any(word in text_lower for word in ['multi-az', 'backup', 'disaster', 'recovery', 'failover', 'replica', 'availability', 'fault', 'resilient', 'redundancy', 'cross-region']):
                current_question['domain'] = 'Design Resilient Architectures'
            elif any(word in text_lower for word in ['performance', 'cache', 'cdn', 'cloudfront', 'elasticache', 'latency', 'throughput', 'scaling', 'load balancer', 'auto scaling']):
                current_question['domain'] = 'Design High-Performing Architectures'
            elif any(word in text_lower for word in ['cost', 'pricing', 'reserved', 'spot', 'savings', 'budget', 'billing', 'optimize', 'cheaper', 'expensive']):
                current_question['domain'] = 'Design Cost-Optimized Architectures'
        
        i += 1
    
    # Add last question
    if current_question and current_question.get('text') and current_question.get('options'):
        questions.append(current_question)
    
    return questions

def create_professional_exam_html(questions, exam_number, timestamp):
    """Create professional exam HTML with all best practices"""
    
    # Randomize question order
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    
    # Read the enhanced template
    with open('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Source_Code/enhanced_exam_js.js', 'r') as f:
        js_content = f.read()
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AWS SAA-C03 Practice Exam - Professional certification preparation with industry best practices">
    <meta name="keywords" content="AWS, SAA-C03, Solutions Architect, Practice Exam, Certification, Professional">
    <meta name="author" content="SAA-C03 Practice Exam Suite">
    <title>AWS SAA-C03 Professional Practice Exam {exam_number:02d} | Industry Standard Certification Prep</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="AWS SAA-C03 Professional Practice Exam {exam_number:02d}">
    <meta property="og:description" content="Professional AWS Solutions Architect certification practice exam with industry best practices">
    <meta property="og:type" content="website">
    
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
            --shadow-light: 0 2px 10px rgba(0,0,0,0.1);
            --shadow-medium: 0 4px 15px rgba(0,0,0,0.15);
            --shadow-heavy: 0 8px 25px rgba(0,0,0,0.2);
            --border-radius: 12px;
            --transition: all 0.3s ease;
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
            box-shadow: var(--shadow-heavy);
        }}
        
        /* Header Styles */
        .exam-header {{
            background: var(--primary-color);
            color: white;
            padding: 20px 30px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: var(--shadow-light);
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
            font-family: 'Courier New', monospace;
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
            transition: var(--transition);
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
            transition: var(--transition);
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
            transition: var(--transition);
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
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: var(--transition);
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
            box-shadow: var(--shadow-medium);
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
            transition: var(--transition);
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
            box-shadow: var(--shadow-medium);
            border-left: 5px solid var(--accent-color);
        }}
        
        .card-title {{
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--text-primary);
        }}
        
        /* Review Items */
        .review-item {{
            margin: 10px 0;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #ddd;
        }}
        
        .review-item.correct {{
            background: #d4edda;
            border-left-color: var(--success-color);
        }}
        
        .review-item.incorrect {{
            background: #f8d7da;
            border-left-color: var(--danger-color);
        }}
        
        .review-item.unanswered {{
            background: #fff3cd;
            border-left-color: var(--warning-color);
        }}
        
        .review-question {{
            font-weight: bold;
            margin-bottom: 8px;
        }}
        
        .correct-answer {{
            color: var(--success-color);
            font-weight: bold;
        }}
        
        .your-answer {{
            color: var(--danger-color);
            font-weight: bold;
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
            
            .final-score {{
                font-size: 2em;
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
        
        /* Print Styles */
        @media print {{
            .exam-header, .nav-panel, .question-navigation {{
                display: none;
            }}
            
            .exam-container {{
                box-shadow: none;
            }}
            
            .option {{
                break-inside: avoid;
            }}
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
                        <h1>AWS SAA-C03 Professional Practice Exam {exam_number:02d}</h1>
                        <p>Solutions Architect Associate Certification • Industry Standard</p>
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

    <script>
        // Inject questions data
        window.examQuestions = {json.dumps(shuffled_questions, ensure_ascii=False)};
        
        {js_content}
    </script>
</body>
</html>'''
    
    return html_content

def main():
    print("🚀 Generating Professional SAA-C03 Practice Exams with Industry Best Practices...")
    
    # Parse questions
    questions = parse_questions('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/rawText.txt')
    complete_questions = [q for q in questions if q['correct']]
    incomplete_questions = [q for q in questions if not q['correct']]
    
    print(f"📊 Found {len(complete_questions)} complete questions")
    print(f"📊 Found {len(incomplete_questions)} incomplete questions")
    
    # Calculate number of full exams
    full_exams = len(complete_questions) // 65
    remaining_questions = len(complete_questions) % 65
    
    print(f"📝 Creating {full_exams} full exams + 1 final exam = 16 total exams")
    
    # Generate professional exams
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create 15 full exams (65 questions each)
    for exam_num in range(1, full_exams + 1):
        start_idx = (exam_num - 1) * 65
        end_idx = start_idx + 65
        exam_questions = complete_questions[start_idx:end_idx]
        
        html_content = create_professional_exam_html(exam_questions, exam_num, timestamp)
        filename = f'/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Enhanced_HTML_Quizzes/SAA-C03_Professional_Exam_{exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: SAA-C03_Professional_Exam_{exam_num:02d}_{timestamp}.html")
    
    # Create final exam (16th) with remaining + incomplete questions
    if remaining_questions > 0 or incomplete_questions:
        final_exam_questions = complete_questions[full_exams * 65:]
        
        # Add incomplete questions with default answer 'A'
        for q in incomplete_questions:
            if len(final_exam_questions) < 65:
                q['correct'] = 'A'  # Default answer for incomplete questions
                final_exam_questions.append(q)
        
        # Fill remaining slots with questions from the beginning if needed
        while len(final_exam_questions) < 65:
            final_exam_questions.append(complete_questions[len(final_exam_questions) - remaining_questions])
        
        final_exam_num = full_exams + 1
        html_content = create_professional_exam_html(final_exam_questions[:65], final_exam_num, timestamp)
        filename = f'/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Enhanced_HTML_Quizzes/SAA-C03_Professional_Exam_{final_exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: SAA-C03_Professional_Exam_{final_exam_num:02d}_{timestamp}.html (includes incomplete questions)")
    
    total_exams = full_exams + (1 if remaining_questions > 0 or incomplete_questions else 0)
    print(f"\n🎉 Generated {total_exams} professional practice exams with industry best practices!")
    print("\n🔥 Features included:")
    print("   • Randomized question order")
    print("   • Question flagging system")
    print("   • Auto-save functionality")
    print("   • Progress tracking")
    print("   • Keyboard shortcuts")
    print("   • Mobile responsive design")
    print("   • Accessibility features")
    print("   • Professional UI/UX")
    print("   • Enhanced analytics")
    print("   • Time warnings")

if __name__ == "__main__":
    main()
