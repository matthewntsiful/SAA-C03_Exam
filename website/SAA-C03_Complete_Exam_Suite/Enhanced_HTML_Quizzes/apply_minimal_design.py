#!/usr/bin/env python3
import json
import re
import glob

# Read the minimal template
with open('SAA-C03_Minimal_Exam_01.html', 'r') as f:
    template = f.read()

# Find all exam files with timestamp 211434
exam_files = sorted(glob.glob('SAA-C03_Professional_Exam_*_20251110_211434.html'))

for exam_file in exam_files:
    # Extract exam number
    exam_num = re.search(r'Exam_(\d+)_', exam_file).group(1)
    
    print(f"Processing Exam {exam_num}...")
    
    # Read the original exam file to extract questions
    with open(exam_file, 'r') as f:
        content = f.read()
    
    # Extract questions JSON
    match = re.search(r'window\.examQuestions = (\[.*?\]);', content, re.DOTALL)
    if match:
        questions_json = match.group(1)
        
        # Create new minimal exam file with correct exam number and ID
        new_content = template.replace(
            'SAA-C03 Practice Exam 01', 
            f'SAA-C03 Practice Exam {exam_num}'
        ).replace(
            'const EXAM_ID = 1;',
            f'const EXAM_ID = {exam_num};'
        ).replace(
            'const examQuestions = [', 
            f'const examQuestions = '
        )
        
        # Replace the sample questions with real questions
        new_content = re.sub(
            r'const examQuestions = .*?\];',
            f'const examQuestions = {questions_json};',
            new_content,
            flags=re.DOTALL
        )
        
        # Write the new minimal exam file
        output_file = f'SAA-C03_Minimal_Exam_{exam_num.zfill(2)}.html'
        with open(output_file, 'w') as f:
            f.write(new_content)
        
        print(f"  ✓ Created {output_file}")
    else:
        print(f"  ✗ Could not extract questions from {exam_file}")

print("\n✅ All 16 exams converted to minimal design!")
