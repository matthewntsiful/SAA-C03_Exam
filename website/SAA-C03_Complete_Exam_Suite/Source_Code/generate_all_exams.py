#!/usr/bin/env python3
import re
import json
from datetime import datetime

def parse_questions(file_path):
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
                'domain': 'General'
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
            
            # Classify domain based on keywords
            text_lower = current_question['text'].lower()
            if any(word in text_lower for word in ['security', 'iam', 'encryption', 'kms', 'vpc', 'firewall', 'ssl', 'tls', 'certificate', 'auth']):
                current_question['domain'] = 'Design Secure Architectures'
            elif any(word in text_lower for word in ['multi-az', 'backup', 'disaster', 'recovery', 'failover', 'replica', 'availability', 'fault']):
                current_question['domain'] = 'Design Resilient Architectures'
            elif any(word in text_lower for word in ['performance', 'cache', 'cdn', 'cloudfront', 'elasticache', 'latency', 'throughput']):
                current_question['domain'] = 'Design High-Performing Architectures'
            elif any(word in text_lower for word in ['cost', 'pricing', 'reserved', 'spot', 'savings', 'budget', 'billing']):
                current_question['domain'] = 'Design Cost-Optimized Architectures'
        
        i += 1
    
    # Add last question
    if current_question and current_question.get('text') and current_question.get('options'):
        questions.append(current_question)
    
    return questions

def create_exam_html(questions, exam_number, timestamp):
    html_template = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>SAA-C03 Practice Exam {exam_num} - {timestamp}</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; margin: 0; }}
        
        .header {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: white;
            padding: 40px;
            text-align: center;
            margin: -20px -20px 30px -20px;
        }}
        
        .aws-logo {{
            font-size: 3em;
            margin-bottom: 15px;
            color: #ff9900;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
            letter-spacing: 2px;
        }}
        
        .header h2 {{
            font-size: 1.5em;
            color: #64b5f6;
            margin-bottom: 25px;
            font-weight: 400;
        }}
        
        .exam-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}
        
        .info-item {{
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        .info-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #ff9900;
            display: block;
        }}
        
        .info-label {{
            font-size: 0.9em;
            margin-top: 8px;
            opacity: 0.9;
        }}
        
        .controls {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #007cba;
            color: white;
            padding: 15px 25px;
            border-radius: 25px;
            box-shadow: 0 4px 15px rgba(0,124,186,0.3);
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 15px;
            font-weight: bold;
        }}
        
        .controls button {{
            background: #ff9900;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 15px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .controls button:hover {{
            background: #e68900;
            transform: translateY(-2px);
        }}
        
        .question {{
            background: white;
            margin: 30px 0;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border-left: 5px solid #007cba;
        }}
        
        .question h3 {{
            color: #007cba;
            margin-bottom: 20px;
            font-size: 1.3em;
        }}
        
        .question p {{
            line-height: 1.8;
            margin: 15px 0;
            color: #2c3e50;
        }}
        
        .option {{
            margin: 15px 0;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: #f8f9fa;
        }}
        
        .option:hover {{
            border-color: #007cba;
            background: #e7f3ff;
            transform: translateX(5px);
        }}
        
        .option.selected {{
            border-color: #007cba;
            background: #e7f3ff;
            box-shadow: 0 4px 15px rgba(0,124,186,0.2);
        }}
        
        .option input[type="radio"], .option input[type="checkbox"] {{
            margin-right: 12px;
            transform: scale(1.2);
        }}
        
        .results {{
            margin: 30px 0;
            padding: 20px;
            border: 2px solid #007cba;
            border-radius: 10px;
            display: none;
        }}
        .score {{
            font-size: 2em;
            font-weight: bold;
            text-align: center;
            margin: 20px 0;
        }}
        .pass {{ color: #28a745; }}
        .fail {{ color: #dc3545; }}
        
        .domain-stat {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #007cba;
        }}
        .domain-name {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .domain-score.pass {{
            color: #28a745;
            font-weight: bold;
        }}
        .domain-score.fail {{
            color: #dc3545;
            font-weight: bold;
        }}
        
        .review-item {{
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #ddd;
        }}
        .review-item.correct {{
            background: #d4edda;
            border-left-color: #28a745;
        }}
        .review-item.incorrect {{
            background: #f8d7da;
            border-left-color: #dc3545;
        }}
        .review-item.unanswered {{
            background: #fff3cd;
            border-left-color: #ffc107;
        }}
        .review-question {{
            font-weight: bold;
            margin-bottom: 8px;
        }}
        .correct-answer {{
            color: #28a745;
            font-weight: bold;
        }}
        .your-answer {{
            color: #dc3545;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="controls">
        <div>Timer: <span id="timer">130:00</span></div>
        <button onclick="toggleTimer()" id="pauseBtn">Pause</button>
    </div>
    
    <div class="header">
        <div class="aws-logo">☁️</div>
        <h1>AWS SAA-C03 Practice Exam</h1>
        <h2>Solutions Architect Associate Certification</h2>
        
        <div class="exam-info">
            <div class="info-item">
                <span class="info-number">65</span>
                <div class="info-label">Questions</div>
            </div>
            <div class="info-item">
                <span class="info-number">130</span>
                <div class="info-label">Minutes</div>
            </div>
            <div class="info-item">
                <span class="info-number">720</span>
                <div class="info-label">Pass Score</div>
            </div>
            <div class="info-item">
                <span class="info-number">{exam_num}</span>
                <div class="info-label">Exam #{exam_num}</div>
            </div>
        </div>
    </div>
    
    {questions_html}
    
    <div style="text-align: center; margin: 40px 0;">
        <button onclick="submitExam()" style="background: #28a745; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 1.1em; cursor: pointer;">Submit Exam</button>
    </div>
    
    <div id="results" class="results">
        <div class="score" id="scoreDisplay"></div>
        <div id="passStatus"></div>
        
        <div style="margin: 30px 0;">
            <h3>📊 Domain Performance</h3>
            <div id="domainStats" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;"></div>
        </div>
        
        <div style="margin: 30px 0;">
            <h3>📝 Question Review</h3>
            <div id="reviewSection" style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 15px; border-radius: 5px;"></div>
        </div>
    </div>

    <script>
        const questions = {questions_json};
        let timeLeft = 130 * 60;
        let timerInterval;
        let isPaused = false;

        function startTimer() {{
            timerInterval = setInterval(() => {{
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                document.getElementById('timer').textContent = `${{minutes}}:${{seconds.toString().padStart(2, '0')}}`;
                
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval);
                    submitExam();
                }}
                timeLeft--;
            }}, 1000);
        }}

        function toggleTimer() {{
            const btn = document.getElementById('pauseBtn');
            if (isPaused) {{
                isPaused = false;
                startTimer();
                btn.textContent = 'Pause';
            }} else {{
                isPaused = true;
                clearInterval(timerInterval);
                btn.textContent = 'Resume';
            }}
        }}

        function selectSingle(element) {{
            const radio = element.querySelector('input[type="radio"]');
            if (radio) {{
                radio.checked = true;
                
                const questionDiv = element.closest('.question');
                questionDiv.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
                element.classList.add('selected');
            }}
        }}

        function submitExam() {{
            clearInterval(timerInterval);
            
            let correct = 0;
            let answered = 0;
            let domainStats = {{}};
            let reviewHTML = '';
            
            // Initialize domain stats
            const domains = ['Design Secure Architectures', 'Design Resilient Architectures', 
                           'Design High-Performing Architectures', 'Design Cost-Optimized Architectures', 'General'];
            domains.forEach(domain => {{
                domainStats[domain] = {{ correct: 0, total: 0 }};
            }});
            
            for (let i = 1; i <= 65; i++) {{
                const question = questions[i-1];
                const userAnswers = [];
                document.querySelectorAll(`input[name="q${{i}}"]:checked`).forEach(input => {{
                    userAnswers.push(input.value);
                }});
                
                // Track domain stats
                domainStats[question.domain].total++;
                
                let isCorrect = false;
                let status = 'unanswered';
                let answerText = '';
                
                if (userAnswers.length > 0) {{
                    answered++;
                    if (userAnswers.includes(question.correct)) {{
                        correct++;
                        isCorrect = true;
                        status = 'correct';
                        domainStats[question.domain].correct++;
                        answerText = `<div class="correct-answer">✓ Correct: ${{question.correct}}</div>`;
                    }} else {{
                        status = 'incorrect';
                        answerText = `<div class="your-answer">✗ Your answer: ${{userAnswers.join(', ')}}</div>
                                    <div class="correct-answer">✓ Correct answer: ${{question.correct}}</div>`;
                    }}
                }} else {{
                    answerText = `<div class="correct-answer">✓ Correct answer: ${{question.correct}}</div>
                                <div style="color: #856404;">⚠ Not answered</div>`;
                }}
                
                // Build review item
                reviewHTML += `
                    <div class="review-item ${{status}}">
                        <div class="review-question">Question ${{i}}: ${{question.text.substring(0, 100)}}...</div>
                        <div class="review-answers">${{answerText}}</div>
                        <div style="font-size: 0.8em; color: #6c757d; margin-top: 5px;">Domain: ${{question.domain}}</div>
                    </div>
                `;
            }}
            
            // Calculate scores
            const score = Math.round((correct / 65) * 1000);
            const percentage = Math.round((correct / 65) * 100);
            
            // Display main score
            document.getElementById('scoreDisplay').innerHTML = `
                <div>Final Score: ${{score}}/1000 (${{percentage}}%)</div>
                <div style="font-size: 0.6em; margin-top: 10px;">
                    Correct: ${{correct}}/65
                </div>
            `;
            
            // Display pass/fail status
            const passStatus = document.getElementById('passStatus');
            if (score >= 720) {{
                passStatus.innerHTML = '<div class="pass">🎉 CONGRATULATIONS! YOU PASSED!</div>';
            }} else {{
                passStatus.innerHTML = '<div class="fail">📚 Keep studying! You need 720 to pass</div>';
            }}
            
            // Display domain statistics
            let domainHTML = '';
            Object.entries(domainStats).forEach(([domain, stats]) => {{
                if (stats.total > 0) {{
                    const domainPercentage = Math.round((stats.correct / stats.total) * 100);
                    const domainClass = domainPercentage >= 70 ? 'pass' : 'fail';
                    domainHTML += `
                        <div class="domain-stat">
                            <div class="domain-name">${{domain.replace('Design ', '')}}</div>
                            <div class="domain-score ${{domainClass}}">${{stats.correct}}/${{stats.total}} (${{domainPercentage}}%)</div>
                        </div>
                    `;
                }}
            }});
            document.getElementById('domainStats').innerHTML = domainHTML;
            
            // Display detailed review
            document.getElementById('reviewSection').innerHTML = reviewHTML;
            
            document.getElementById('results').style.display = 'block';
        }}

        // Start on load and add checkbox handlers
        window.onload = function() {{
            startTimer();
            
            // Add direct click handlers for checkboxes
            document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {{
                checkbox.addEventListener('change', function() {{
                    const option = this.closest('.option');
                    if (this.checked) {{
                        option.classList.add('selected');
                    }} else {{
                        option.classList.remove('selected');
                    }}
                }});
            }});
        }};
    </script>
</body>
</html>'''

    # Generate questions HTML
    questions_html = ""
    for i, q in enumerate(questions, 1):
        # Determine if multiple choice
        is_multiple = len(q['correct']) > 1 or ',' in q['correct']
        input_type = "checkbox" if is_multiple else "radio"
        
        questions_html += f'''
    <div class="question">
        <h3>Question {i}</h3>
        <p><strong>{q['domain']}</strong></p>
        <p>{q['text']}</p>
'''
        
        for option_letter, option_text in q['options'].items():
            if is_multiple:
                questions_html += f'''        <div class="option">
            <input type="checkbox" name="q{i}" value="{option_letter}"> {option_letter}. {option_text}
        </div>
'''
            else:
                questions_html += f'''        <div class="option" onclick="selectSingle(this)">
            <input type="radio" name="q{i}" value="{option_letter}"> {option_letter}. {option_text}
        </div>
'''
        
        questions_html += "    </div>\n"
    
    # Convert questions to JSON
    questions_json = json.dumps(questions, ensure_ascii=False)
    
    return html_template.format(
        exam_num=exam_number,
        timestamp=timestamp,
        questions_html=questions_html,
        questions_json=questions_json
    )

def main():
    print("🔍 Parsing questions from rawText.txt...")
    questions = parse_questions('/Users/Matthieu/Downloads/SAA-C03_Exam/rawText.txt')
    
    print(f"📊 Found {len(questions)} complete questions")
    
    # Separate complete and incomplete questions
    complete_questions = [q for q in questions if q['correct']]
    incomplete_questions = [q for q in questions if not q['correct']]
    
    print(f"✅ Complete questions: {len(complete_questions)}")
    print(f"❌ Incomplete questions: {len(incomplete_questions)}")
    
    # Calculate number of full exams
    full_exams = len(complete_questions) // 65
    remaining_questions = len(complete_questions) % 65
    
    print(f"📝 Can create {full_exams} full exams of 65 questions each")
    print(f"📝 Remaining questions: {remaining_questions}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Generate full exams
    for exam_num in range(1, full_exams + 1):
        start_idx = (exam_num - 1) * 65
        end_idx = start_idx + 65
        exam_questions = complete_questions[start_idx:end_idx]
        
        html_content = create_exam_html(exam_questions, exam_num, timestamp)
        filename = f'/Users/Matthieu/Downloads/SAA-C03_Exam/SAA-C03_Full_Exam_{exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: SAA-C03_Full_Exam_{exam_num:02d}_{timestamp}.html")
    
    # Create final exam with remaining + incomplete questions
    if remaining_questions > 0 or incomplete_questions:
        final_exam_questions = complete_questions[full_exams * 65:]
        
        # Add incomplete questions (without suggested answers)
        for q in incomplete_questions:
            if len(final_exam_questions) < 65:
                q['correct'] = 'A'  # Default answer for incomplete questions
                final_exam_questions.append(q)
        
        # Fill remaining slots with questions from the beginning if needed
        while len(final_exam_questions) < 65:
            final_exam_questions.append(complete_questions[len(final_exam_questions) - remaining_questions])
        
        final_exam_num = full_exams + 1
        html_content = create_exam_html(final_exam_questions[:65], final_exam_num, timestamp)
        filename = f'/Users/Matthieu/Downloads/SAA-C03_Exam/SAA-C03_Full_Exam_{final_exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: SAA-C03_Full_Exam_{final_exam_num:02d}_{timestamp}.html (includes incomplete questions)")
    
    print(f"\n🎉 Generated {full_exams + (1 if remaining_questions > 0 or incomplete_questions else 0)} practice exams!")
    print(f"📁 Files saved to: SAA-C03_Complete_Exam_Suite/Source_Code/")

if __name__ == "__main__":
    main()
