#!/usr/bin/env python3
"""
Update existing professional exam files with left sidebar navigation
"""

import json
import re
import glob
from professional_design_system import get_professional_css, get_professional_html_template

def parse_questions(file_path):
    """Parse questions from rawText.txt"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    current_question = None
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if re.match(r'^\d+\.', line):
            if current_question and current_question.get('text') and current_question.get('options'):
                questions.append(current_question)
            
            current_question = {
                'number': len(questions) + 1,
                'text': '',
                'options': {},
                'correct': '',
                'domain': 'General'
            }
            
            question_text = line
            i += 1
            while i < len(lines) and not re.match(r'^[A-E]\.', lines[i].strip()) and not re.match(r'^\d+\.', lines[i].strip()):
                if lines[i].strip():
                    question_text += ' ' + lines[i].strip()
                i += 1
            
            current_question['text'] = question_text.replace(f"{current_question['number']}. ", "").strip()
            continue
        
        if re.match(r'^[A-E]\.', line) and current_question:
            option_letter = line[0]
            option_text = line[2:].strip()
            
            i += 1
            while i < len(lines) and not re.match(r'^[A-E]\.', lines[i].strip()) and not re.match(r'^Suggested Answer:', lines[i].strip()) and not re.match(r'^\d+\.', lines[i].strip()):
                if lines[i].strip() and not lines[i].strip().startswith('Page '):
                    option_text += ' ' + lines[i].strip()
                i += 1
            
            current_question['options'][option_letter] = option_text
            continue
        
        if line.startswith('Suggested Answer:') and current_question:
            answer = line.replace('Suggested Answer:', '').strip().upper()
            current_question['correct'] = answer
            
            text_lower = current_question['text'].lower()
            if any(word in text_lower for word in ['security', 'iam', 'encryption', 'kms', 'vpc', 'firewall', 'ssl', 'tls', 'certificate', 'auth', 'compliance', 'policy']):
                current_question['domain'] = 'Design Secure Architectures'
            elif any(word in text_lower for word in ['multi-az', 'backup', 'disaster', 'recovery', 'failover', 'replica', 'availability', 'fault', 'resilient']):
                current_question['domain'] = 'Design Resilient Architectures'
            elif any(word in text_lower for word in ['performance', 'cache', 'cdn', 'cloudfront', 'elasticache', 'latency', 'throughput', 'scaling']):
                current_question['domain'] = 'Design High-Performing Architectures'
            elif any(word in text_lower for word in ['cost', 'pricing', 'reserved', 'spot', 'savings', 'budget', 'billing', 'optimize']):
                current_question['domain'] = 'Design Cost-Optimized Architectures'
        
        i += 1
    
    if current_question and current_question.get('text') and current_question.get('options'):
        questions.append(current_question)
    
    return questions

def update_existing_exam(file_path, questions, exam_number):
    """Update existing exam file with new design"""
    
    # Read JavaScript content
    with open('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Source_Code/professional_exam_js.js', 'r') as f:
        js_content = f.read()
    
    # Get template and CSS
    html_template = get_professional_html_template()
    css_content = get_professional_css()
    
    # Format the template
    html_content = html_template.format(
        exam_number=exam_number,
        css_content=css_content,
        questions_json=json.dumps(questions, ensure_ascii=False),
        javascript_content=js_content
    )
    
    # Write directly to existing file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    print("🔄 Updating Existing Professional Exam Files...")
    
    # Parse questions
    questions = parse_questions('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/rawText.txt')
    complete_questions = [q for q in questions if q['correct']]
    incomplete_questions = [q for q in questions if not q['correct']]
    
    # Get existing professional exam files
    exam_files = glob.glob('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Professional_Exams/SAA-C03_Professional_Exam_*_20251110_090831.html')
    exam_files.sort()
    
    print(f"📊 Found {len(exam_files)} existing professional exam files to update")
    
    # Update each existing file
    for i, file_path in enumerate(exam_files, 1):
        if i <= 15:  # First 15 exams
            start_idx = (i - 1) * 65
            end_idx = start_idx + 65
            exam_questions = complete_questions[start_idx:end_idx]
        else:  # 16th exam
            exam_questions = complete_questions[15 * 65:]
            # Add incomplete questions
            for q in incomplete_questions:
                if len(exam_questions) < 65:
                    q['correct'] = 'A'
                    exam_questions.append(q)
            # Fill remaining slots
            while len(exam_questions) < 65:
                exam_questions.append(complete_questions[len(exam_questions) - len(complete_questions[15 * 65:])])
            exam_questions = exam_questions[:65]
        
        update_existing_exam(file_path, exam_questions, i)
        print(f"✅ Updated: {file_path.split('/')[-1]}")
    
    # Clean up newer files
    newer_files = glob.glob('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Professional_Exams/SAA-C03_Professional_Exam_*_20251110_09*.html')
    for file_path in newer_files:
        if '090831' not in file_path:  # Keep the original timestamp files
            import os
            os.remove(file_path)
            print(f"🗑️ Removed duplicate: {file_path.split('/')[-1]}")
    
    print(f"\\n🎉 Updated all existing professional exam files with left sidebar navigation!")
    print("\\n✨ Changes applied:")
    print("   • Left sidebar question navigation (200px width)")
    print("   • 5-column grid layout for question numbers")
    print("   • Sticky sidebar positioning")
    print("   • Mobile responsive design")
    print("   • No new files created - existing files updated")

if __name__ == "__main__":
    main()
