# Deployment Guide - AWS SAA-C03 Exam Suite

## 🚀 Quick Deploy Options

### Option 1: Local Development (Fastest)
```bash
cd website
npm install
npm run dev
```
Access at: http://localhost:3000

### Option 2: AWS S3 + CloudFront (Recommended)
```bash
cd infrastructure/terraform/environments/dev
terraform init
terraform plan
terraform apply
```

### Option 3: Static File Hosting
Upload `website/` folder to any static host (Netlify, Vercel, GitHub Pages)

---

## 📋 Detailed Deployment Steps

### Local Development

**Prerequisites:**
- Node.js 14+ installed
- npm or yarn

**Steps:**
```bash
# 1. Navigate to website directory
cd website

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev

# 4. Open browser
open http://localhost:3000
```

**Development Features:**
- Hot reload (restart server for changes)
- Express server on port 3000
- Serves EJS templates
- Static file serving

---

### AWS Production Deployment

**Prerequisites:**
- AWS CLI configured
- Terraform installed
- AWS account with appropriate permissions

**Architecture:**
```
Route53 → CloudFront → S3 Bucket
                ↓
              WAF
```

**Step 1: Configure Variables**
```bash
cd infrastructure/terraform/environments/dev
```

Edit `terraform.tfvars`:
```hcl
project_name = "saa-exams"
environment  = "dev"
domain_name  = "your-domain.com"
```

**Step 2: Deploy Infrastructure**
```bash
terraform init
terraform plan
terraform apply
```

**Step 3: Build and Upload**
```bash
cd ../../../website

# Build static files (if needed)
npm run build

# Upload to S3
aws s3 sync . s3://your-bucket-name/ \
  --exclude "node_modules/*" \
  --exclude ".git/*"
```

**Step 4: Invalidate CloudFront**
```bash
aws cloudfront create-invalidation \
  --distribution-id YOUR_DIST_ID \
  --paths "/*"
```

**Step 5: Verify**
```bash
curl https://your-domain.com
```

---

### Static Hosting (Netlify/Vercel)

**Netlify:**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd website
netlify deploy --prod
```

**Vercel:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd website
vercel --prod
```

**GitHub Pages:**
```bash
# 1. Create gh-pages branch
git checkout -b gh-pages

# 2. Copy website files to root
cp -r website/* .

# 3. Push to GitHub
git add .
git commit -m "Deploy to GitHub Pages"
git push origin gh-pages

# 4. Enable GitHub Pages in repo settings
```

---

## 🔧 Configuration

### Environment Variables
Create `.env` file in `website/`:
```env
PORT=3000
NODE_ENV=production
```

### Server Configuration
Edit `website/server.js`:
```javascript
const PORT = process.env.PORT || 3000;
```

### Domain Configuration
Update in `infrastructure/terraform/environments/dev/terraform.tfvars`:
```hcl
domain_name = "saa-exams.your-domain.com"
```

---

## 📦 Build Process

### Development Build
```bash
npm run dev
```

### Production Build
```bash
npm run build  # If build script exists
npm start      # Production server
```

### Static Export
```bash
# Copy all files
cp -r website/views/*.ejs website/public/
cp -r website/SAA-C03_Complete_Exam_Suite website/public/

# Upload to S3
aws s3 sync website/public s3://your-bucket/
```

---

## 🔐 Security Checklist

- [ ] Enable HTTPS (CloudFront SSL)
- [ ] Configure WAF rules
- [ ] Set up CORS policies
- [ ] Enable S3 bucket encryption
- [ ] Configure CloudFront security headers
- [ ] Set up Route53 health checks
- [ ] Enable CloudTrail logging
- [ ] Configure backup policies

---

## 🌐 DNS Configuration

### Route53 Setup
```bash
# Create hosted zone
aws route53 create-hosted-zone \
  --name your-domain.com \
  --caller-reference $(date +%s)

# Create A record
aws route53 change-resource-record-sets \
  --hosted-zone-id YOUR_ZONE_ID \
  --change-batch file://dns-record.json
```

**dns-record.json:**
```json
{
  "Changes": [{
    "Action": "CREATE",
    "ResourceRecordSet": {
      "Name": "saa-exams.your-domain.com",
      "Type": "A",
      "AliasTarget": {
        "HostedZoneId": "Z2FDTNDATAQYW2",
        "DNSName": "your-cloudfront-dist.cloudfront.net",
        "EvaluateTargetHealth": false
      }
    }
  }]
}
```

---

## 📊 Monitoring

### CloudWatch Alarms
```bash
# Create alarm for 4xx errors
aws cloudwatch put-metric-alarm \
  --alarm-name saa-exams-4xx-errors \
  --metric-name 4xxErrorRate \
  --namespace AWS/CloudFront \
  --statistic Average \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold
```

### Logging
- CloudFront access logs → S3
- WAF logs → CloudWatch
- Application logs → CloudWatch Logs

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example
```yaml
name: Deploy to AWS

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      
      - name: Deploy to S3
        run: |
          cd website
          aws s3 sync . s3://your-bucket/ --delete
      
      - name: Invalidate CloudFront
        run: |
          aws cloudfront create-invalidation \
            --distribution-id ${{ secrets.CLOUDFRONT_ID }} \
            --paths "/*"
```

---

## 🧪 Testing

### Local Testing
```bash
# Test server
npm test

# Test endpoints
curl http://localhost:3000
curl http://localhost:3000/exams/SAA-C03_Minimal_Exam_01.html
```

### Production Testing
```bash
# Test HTTPS
curl -I https://your-domain.com

# Test CloudFront
curl -I https://your-cloudfront-dist.cloudfront.net

# Test specific exam
curl https://your-domain.com/exams/SAA-C03_Minimal_Exam_01.html
```

---

## 🐛 Troubleshooting

### Issue: 404 Errors
**Solution:** Check S3 bucket policy and CloudFront origin settings

### Issue: Slow Load Times
**Solution:** Enable CloudFront caching, compress files

### Issue: CORS Errors
**Solution:** Configure S3 CORS policy:
```json
[{
  "AllowedHeaders": ["*"],
  "AllowedMethods": ["GET", "HEAD"],
  "AllowedOrigins": ["*"],
  "ExposeHeaders": []
}]
```

### Issue: SSL Certificate
**Solution:** Request ACM certificate in us-east-1 region

---

## 📈 Performance Optimization

### CloudFront Settings
- Enable compression
- Set cache TTL (1 day for static files)
- Enable HTTP/2
- Configure origin shield

### S3 Settings
- Enable transfer acceleration
- Set appropriate storage class
- Configure lifecycle policies

### Application
- Minify CSS/JS (already using Tailwind CDN)
- Optimize images
- Enable browser caching

---

## 💰 Cost Estimation

**Monthly AWS Costs (Estimated):**
- S3 Storage (1GB): $0.023
- CloudFront (10GB transfer): $0.85
- Route53 (1 hosted zone): $0.50
- WAF (basic rules): $5.00
- **Total: ~$6.40/month**

**Free Tier Eligible:**
- S3: 5GB storage, 20,000 GET requests
- CloudFront: 1TB transfer, 10M requests
- Route53: First hosted zone

---

## 🎯 Post-Deployment Checklist

- [ ] Verify all 16 exams load correctly
- [ ] Test exam submission and results
- [ ] Verify progress tracking works
- [ ] Test dark mode toggle
- [ ] Check mobile responsiveness
- [ ] Verify analytics dashboard
- [ ] Test clear progress button
- [ ] Check SSL certificate
- [ ] Verify DNS resolution
- [ ] Test from different browsers
- [ ] Monitor CloudWatch metrics
- [ ] Set up backup strategy

---

## 📞 Support

**Common Issues:**
1. Exam not loading → Check S3 file paths
2. Progress not saving → Check localStorage enabled
3. Timer not working → Check JavaScript enabled
4. Dark mode not persisting → Check localStorage

**Logs Location:**
- CloudFront: S3 bucket (access logs)
- WAF: CloudWatch Logs
- Application: Browser console

---

**Deployment Status:** ✅ Production Ready
**Last Updated:** 2024
**Version:** 1.0.0
