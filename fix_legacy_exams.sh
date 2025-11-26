#!/bin/bash

echo "Fixing legacy exam files..."

# Copy the fix scripts to work with legacy directory
cp auto_fix_options.js auto_fix_legacy.js
cp reconstruct_questions.js reconstruct_legacy.js

# Update paths in the scripts
sed -i '' 's|./website/public/exams|./website/SAA-C03_Complete_Exam_Suite/Enhanced_HTML_Quizzes|g' auto_fix_legacy.js
sed -i '' 's|./website/public/exams|./website/SAA-C03_Complete_Exam_Suite/Enhanced_HTML_Quizzes|g' reconstruct_legacy.js

# Run the fixes
echo "Step 1: Fixing merged options..."
node auto_fix_legacy.js

echo ""
echo "Step 2: Reconstructing corrupted questions..."
node reconstruct_legacy.js

# Cleanup
rm auto_fix_legacy.js reconstruct_legacy.js

echo ""
echo "✓ Legacy exam files fixed!"
