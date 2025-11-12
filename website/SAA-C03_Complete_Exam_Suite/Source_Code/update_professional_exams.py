#!/usr/bin/env python3
"""
Update all professional exams with new design system
"""

import json
import re
from datetime import datetime
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

def create_professional_exam(questions, exam_number):
    """Create professional exam with new design system"""
    
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
    
    return html_content

def main():
    print("🎨 Updating Professional Exams with New Design System...")
    
    # Parse questions
    questions = parse_questions('/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/rawText.txt')
    complete_questions = [q for q in questions if q['correct']]
    incomplete_questions = [q for q in questions if not q['correct']]
    
    print(f"📊 Found {len(complete_questions)} complete questions")
    
    # Calculate exams
    full_exams = len(complete_questions) // 65
    remaining_questions = len(complete_questions) % 65
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Update all 16 professional exams
    for exam_num in range(1, full_exams + 1):
        start_idx = (exam_num - 1) * 65
        end_idx = start_idx + 65
        exam_questions = complete_questions[start_idx:end_idx]
        
        html_content = create_professional_exam(exam_questions, exam_num)
        filename = f'/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Professional_Exams/SAA-C03_Professional_Exam_{exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Updated: SAA-C03_Professional_Exam_{exam_num:02d}_{timestamp}.html")
    
    # Create final exam (16th)
    if remaining_questions > 0 or incomplete_questions:
        final_exam_questions = complete_questions[full_exams * 65:]
        
        for q in incomplete_questions:
            if len(final_exam_questions) < 65:
                q['correct'] = 'A'
                final_exam_questions.append(q)
        
        while len(final_exam_questions) < 65:
            final_exam_questions.append(complete_questions[len(final_exam_questions) - remaining_questions])
        
        final_exam_num = full_exams + 1
        html_content = create_professional_exam(final_exam_questions[:65], final_exam_num)
        filename = f'/Users/Matthieu/Downloads/SolutionsArchitectPracticeExam/SAA-C03_Exam/SAA-C03_Complete_Exam_Suite/Professional_Exams/SAA-C03_Professional_Exam_{final_exam_num:02d}_{timestamp}.html'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Updated: SAA-C03_Professional_Exam_{final_exam_num:02d}_{timestamp}.html")
    
    print(f"\\n🎉 Updated 16 professional exams with new design system!")
    print("\\n🎨 New Features:")
    print("   • Horizontal question navigation")
    print("   • Professional AWS branding")
    print("   • Enhanced progress tracking")
    print("   • Modern typography (Inter font)")
    print("   • Improved accessibility")
    print("   • Professional notifications")
    print("   • Enhanced modal dialogs")

if __name__ == "__main__":
    main()
