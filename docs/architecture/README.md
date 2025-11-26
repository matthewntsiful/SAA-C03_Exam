# Architecture Diagrams

> Visual documentation for AWS SAA-C03 Exam Suite infrastructure

## 📐 Diagram Inventory

| Diagram | File | Status | Description |
|---------|------|--------|-------------|
| High-Level Architecture | `high-level-architecture.png` | 🔴 Pending | Overall system design |
| AWS Infrastructure | `aws-infrastructure.png` | 🔴 Pending | AWS resources topology |
| CI/CD Pipeline | `cicd-pipeline.png` | 🔴 Pending | GitHub Actions workflow |
| Application Flow | `application-flow.png` | 🔴 Pending | User interaction flow |
| Data Flow | `data-flow.png` | 🔴 Pending | localStorage structure |
| Security Architecture | `security-architecture.png` | 🔴 Pending | Security layers |
| Monitoring | `monitoring-architecture.png` | 🔴 Pending | CloudWatch setup |
| Terraform Graph | `terraform-graph.png` | 🔴 Pending | Infrastructure graph |

## 🎨 Creating Diagrams

### Option 1: draw.io (Recommended)

1. Visit [diagrams.net](https://app.diagrams.net/)
2. Use AWS icon library (Shapes → More Shapes → AWS)
3. Save source files to `source/` directory
4. Export as PNG to this directory

### Option 2: Terraform Graph

```bash
# Generate infrastructure diagram
cd ../../../infrastructure/terraform/environments/prod
terraform init
terraform graph | dot -Tpng > ../../../../docs/architecture/terraform-graph.png
```

### Option 3: CloudCraft

1. Visit [cloudcraft.co](https://www.cloudcraft.co/)
2. Design AWS architecture
3. Export as PNG/SVG

## 📋 Diagram Requirements

### High-Level Architecture
**Components to include:**
- User/Browser
- Route53 (DNS)
- CloudFront (CDN)
- S3 (Content bucket)
- WAF (Security)
- localStorage (Client-side storage)

### AWS Infrastructure
**Resources to show:**
- S3 buckets (content, logs, state)
- CloudFront distribution
- Route53 hosted zone
- ACM certificate
- WAF web ACL
- CloudWatch alarms
- DynamoDB (state locking)
- IAM roles
- Connections between resources

### CI/CD Pipeline
**Stages to illustrate:**
- GitHub repository
- GitHub Actions (OIDC)
- Terraform plan/apply
- Dev environment deployment
- Prod environment deployment
- Branch strategy (develop/main)

### Application Flow
**User journey:**
1. User visits domain
2. DNS resolution (Route53)
3. CloudFront cache check
4. WAF validation
5. S3 origin fetch
6. Browser rendering
7. localStorage operations

### Data Flow
**localStorage structure:**
- Exam progress objects
- Exam results history
- User preferences
- Flagged questions
- Analytics data

## 🔧 Tools & Resources

### Diagram Tools
- **draw.io**: https://app.diagrams.net/ (Free)
- **Lucidchart**: https://www.lucidchart.com/ (Paid)
- **CloudCraft**: https://www.cloudcraft.co/ (AWS-specific)
- **Graphviz**: `brew install graphviz` (CLI)

### AWS Resources
- **AWS Architecture Icons**: https://aws.amazon.com/architecture/icons/
- **AWS Architecture Center**: https://aws.amazon.com/architecture/
- **Well-Architected Framework**: https://aws.amazon.com/architecture/well-architected/

### Icon Sets
- AWS Official Icons (SVG)
- Font Awesome (for generic icons)
- Material Design Icons

## 📏 Style Guidelines

### Colors
- **AWS Orange**: `#FF9900`
- **Primary Blue**: `#232F3E`
- **Success Green**: `#10B981`
- **Warning Yellow**: `#F59E0B`
- **Error Red**: `#EF4444`

### Fonts
- **Headings**: Amazon Ember Bold
- **Body**: Amazon Ember Regular
- **Code**: Courier New, monospace

### Layout
- Use consistent spacing (16px grid)
- Group related components
- Show data flow with arrows
- Label all connections
- Include legends for icons

## 📦 File Organization

```
architecture/
├── high-level-architecture.png       # Exported diagrams
├── aws-infrastructure.png
├── cicd-pipeline.png
├── application-flow.png
├── data-flow.png
├── security-architecture.png
├── monitoring-architecture.png
├── terraform-graph.png
├── source/                           # Editable sources
│   ├── high-level.drawio
│   ├── aws-infra.drawio
│   ├── cicd.drawio
│   ├── app-flow.drawio
│   └── data-flow.drawio
└── README.md                         # This file
```

## ✅ Checklist

Before committing diagrams:

- [ ] All components labeled clearly
- [ ] Connections show direction (arrows)
- [ ] Legend included (if needed)
- [ ] High resolution (min 1920px width)
- [ ] Transparent or white background
- [ ] Source file saved in `source/`
- [ ] PNG exported to this directory
- [ ] Referenced in main ARCHITECTURE.md
- [ ] Status updated in table above

## 🔄 Updating Diagrams

When infrastructure changes:

1. Update source file in `source/`
2. Re-export to PNG
3. Update ARCHITECTURE.md if needed
4. Commit both source and PNG
5. Update status in table above

## 📝 Naming Convention

- Use kebab-case: `aws-infrastructure.png`
- Source files match: `aws-infra.drawio`
- Descriptive names
- No version numbers (use git)

---

**Status**: 🔴 Diagrams pending creation  
**Last Updated**: January 2025
