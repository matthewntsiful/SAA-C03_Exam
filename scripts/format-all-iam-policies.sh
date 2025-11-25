#!/bin/bash

# Script to find and format IAM policies in all exam files

echo "🔍 Searching for IAM policy questions in all exam files..."
echo ""

cd "$(dirname "$0")/../website/public/exams"

# Search for IAM policy patterns
grep -n "Version.*2012-10-17.*Statement" *.html | while IFS=: read -r file line content; do
    echo "📄 Found IAM policy in: $file (line $line)"
    echo "   Preview: ${content:0:100}..."
    echo ""
done

echo "✅ Search complete!"
echo ""
echo "To format IAM policies, the policies should be:"
echo "  1. Properly indented JSON"
echo "  2. Wrapped in <pre class='iam-policy-block'><code>...</code></pre>"
echo "  3. Have escaped quotes (\\\")"
echo ""
echo "Example has been applied to SAA-C03_Minimal_Exam_02.html question 96"
