# Project Structure

```
SAA-C03_Exam/
├── website/                          # Main application
│   ├── server.js                     # Express server
│   ├── package.json                  # Dependencies
│   ├── views/                        # EJS templates
│   │   ├── minimal.ejs              # Landing page
│   │   └── index.ejs                # Alternative full view
│   ├── public/                       # Static assets
│   │   ├── exams/                   # Exam HTML files
│   │   │   ├── SAA-C03_Minimal_Exam_01.html
│   │   │   ├── SAA-C03_Minimal_Exam_02.html
│   │   │   └── ... (16 total)
│   │   ├── css/                     # Custom styles (if needed)
│   │   ├── js/                      # Shared JavaScript
│   │   └── assets/                  # Images, icons
│   └── README.md                     # Application docs
│
├── infrastructure/                   # IaC
│   ├── terraform/                   # Terraform configs
│   │   ├── modules/                 # Reusable modules
│   │   │   ├── s3/
│   │   │   ├── cloudfront/
│   │   │   ├── route53/
│   │   │   └── waf/
│   │   └── environments/            # Environment configs
│   │       ├── dev/
│   │       ├── staging/
│   │       └── prod/
│   ├── cloudformation-template.yaml
│   └── deploy-to-s3.sh
│
├── scripts-legacy/                   # Python utilities
│   └── (legacy enhancement scripts)
│
├── docs/                            # Documentation
│   ├── FEATURES.md                  # Feature list
│   ├── DEPLOYMENT.md                # Deployment guide
│   └── API.md                       # API documentation
│
├── README.md                        # Project overview
└── .gitignore                       # Git ignore rules
```

## Directory Purposes

### `/website`
Main application code. Contains Express server, views, and static files.

**Key Files:**
- `server.js` - Express server configuration
- `package.json` - Node.js dependencies
- `views/minimal.ejs` - Landing page with analytics
- `public/exams/` - All 16 practice exam HTML files

### `/infrastructure`
Infrastructure as Code for AWS deployment.

**Terraform Modules:**
- `s3/` - S3 bucket for static hosting
- `cloudfront/` - CDN distribution
- `route53/` - DNS management
- `waf/` - Web Application Firewall

**Environments:**
- `dev/` - Development environment
- `staging/` - Staging environment
- `prod/` - Production environment

### `/scripts-legacy`
Legacy Python scripts for exam generation and enhancement.

### `/docs`
Comprehensive documentation for features, deployment, and APIs.

## File Organization Best Practices

### Exam Files
- Location: `website/public/exams/`
- Naming: `SAA-C03_Minimal_Exam_XX.html` (XX = 01-16)
- Self-contained: Each file includes all HTML, CSS, JS

### Static Assets
- CSS: `website/public/css/`
- JavaScript: `website/public/js/`
- Images: `website/public/assets/`

### Templates
- EJS files: `website/views/`
- Partials: `website/views/partials/` (if needed)

### Configuration
- Environment: `.env` (not committed)
- Terraform: `infrastructure/terraform/environments/*/terraform.tfvars`

## Access Patterns

### Development
```
http://localhost:3000/                    → Landing page
http://localhost:3000/exams/SAA-C03_Minimal_Exam_01.html → Exam 1
```

### Production
```
https://saa-exams.domain.com/             → Landing page
https://saa-exams.domain.com/exams/SAA-C03_Minimal_Exam_01.html → Exam 1
```

## Build Output

### Development
No build step required. Server serves files directly.

### Production (S3)
```
s3://bucket-name/
├── index.html (from minimal.ejs)
├── exams/
│   ├── SAA-C03_Minimal_Exam_01.html
│   └── ...
├── css/
├── js/
└── assets/
```

## Environment Variables

### Development (.env)
```
PORT=3000
NODE_ENV=development
```

### Production
Set in AWS Systems Manager Parameter Store or environment.

## Dependencies

### Runtime
- Node.js 14+
- Express.js
- EJS

### Development
- Terraform
- AWS CLI
- Python 3 (for scripts)

## Maintenance

### Adding New Exam
1. Create `SAA-C03_Minimal_Exam_XX.html` in `public/exams/`
2. Update `EXAM_ID` constant
3. Add questions array
4. Test locally
5. Deploy

### Updating Infrastructure
1. Modify Terraform files in `infrastructure/terraform/`
2. Run `terraform plan`
3. Review changes
4. Run `terraform apply`

### Updating Styles
1. Modify Tailwind classes in templates
2. Or add custom CSS in `public/css/`
3. Test in browser
4. Deploy

## Security

### Sensitive Files (Never Commit)
- `.env`
- `terraform.tfstate`
- `*.tfvars` (with secrets)
- AWS credentials

### Public Files
- All HTML, CSS, JS in `public/`
- Documentation
- Infrastructure code (without secrets)

## Backup Strategy

### Code
- Git repository (GitHub/GitLab)
- Regular commits

### Data
- User progress: Browser localStorage (client-side)
- Infrastructure state: Terraform remote backend (S3)

### Exam Content
- Original files: `SAA-C03_Complete_Exam_Suite/` (backup)
- Active files: `public/exams/`

## Deployment Workflow

1. **Develop** → Edit files in `website/`
2. **Test** → Run locally with `npm run dev`
3. **Build** → (Optional) Generate static files
4. **Deploy** → Upload to S3 or run Terraform
5. **Verify** → Test production URL

## Monitoring

### Logs
- Application: `console.log` → CloudWatch
- Access: CloudFront logs → S3
- Errors: Browser console

### Metrics
- CloudWatch dashboards
- CloudFront analytics
- Custom metrics in landing page

---

**Last Updated:** 2024
**Version:** 1.0.0
