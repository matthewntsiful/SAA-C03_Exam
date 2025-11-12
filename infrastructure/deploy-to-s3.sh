#!/bin/bash

# SAA-C03 Practice Exam - S3 Static Website Deployment
BUCKET_NAME="saa-c03-practice-exams-$(date +%s)"
REGION="us-east-1"

echo "🚀 Deploying SAA-C03 Practice Exams to S3..."

# 1. Create S3 bucket
aws s3 mb s3://$BUCKET_NAME --region $REGION

# 2. Enable static website hosting
aws s3 website s3://$BUCKET_NAME --index-document index.html

# 3. Upload HTML files
aws s3 sync SAA-C03_Complete_Exam_Suite/Enhanced_HTML_Quizzes/ s3://$BUCKET_NAME/exams/ \
    --exclude "*.md" \
    --cache-control "max-age=86400"

# 4. Upload analytics dashboard
aws s3 cp SAA-C03_Complete_Exam_Suite/Analytics_Dashboard/analytics_dashboard.html s3://$BUCKET_NAME/

# 5. Create index page
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>SAA-C03 Practice Exams</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        .exam-link { display: block; padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 8px; text-decoration: none; color: #333; }
        .exam-link:hover { background: #e9ecef; }
    </style>
</head>
<body>
    <h1>🎯 SAA-C03 Practice Exams</h1>
    <p>Professional AWS Solutions Architect Associate certification practice exams.</p>
    
    <h2>📊 Analytics Dashboard</h2>
    <a href="analytics_dashboard.html" class="exam-link">View Performance Analytics</a>
    
    <h2>📝 Practice Exams</h2>
EOF

# Add exam links
for i in {1..16}; do
    echo "    <a href=\"exams/SAA-C03_Professional_Exam_$(printf "%02d" $i)_20251110_211434.html\" class=\"exam-link\">Practice Exam $i</a>" >> index.html
done

cat >> index.html << 'EOF'
</body>
</html>
EOF

aws s3 cp index.html s3://$BUCKET_NAME/

# 6. Set bucket policy for public read
cat > bucket-policy.json << EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::$BUCKET_NAME/*"
        }
    ]
}
EOF

aws s3api put-bucket-policy --bucket $BUCKET_NAME --policy file://bucket-policy.json

echo "✅ S3 bucket created: $BUCKET_NAME"
echo "🌐 Website URL: http://$BUCKET_NAME.s3-website-$REGION.amazonaws.com"
echo ""
echo "Next steps:"
echo "1. Create CloudFront distribution"
echo "2. Add WAF protection"
echo "3. Configure custom domain"