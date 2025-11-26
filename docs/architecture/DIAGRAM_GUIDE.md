# Quick Diagram Creation Guide

> Step-by-step guide to create architecture diagrams

## 🚀 Quick Start (5 minutes)

### Method 1: draw.io (Easiest)

1. **Open draw.io**
   - Visit https://app.diagrams.net/
   - Click "Create New Diagram"

2. **Load AWS Icons**
   - Click "More Shapes" (bottom left)
   - Search "AWS"
   - Enable "AWS 19" library
   - Click "Apply"

3. **Create Diagram**
   - Drag AWS icons from left panel
   - Connect with arrows
   - Add labels and text

4. **Save & Export**
   - File → Save As → `docs/architecture/source/[name].drawio`
   - File → Export As → PNG
   - Save to `docs/architecture/[name].png`
   - Resolution: 300 DPI, Transparent background

### Method 2: Terraform Graph (Automated)

```bash
# Generate infrastructure diagram automatically
./scripts/generate-terraform-diagram.sh
```

## 📋 Diagram Checklist

### High-Level Architecture
```
Components needed:
☐ User/Browser icon
☐ Route53 (DNS)
☐ CloudFront (CDN)
☐ S3 bucket (content)
☐ WAF shield
☐ localStorage (browser)
☐ Arrows showing flow
☐ Labels on connections
```

### AWS Infrastructure
```
Resources to include:
☐ S3 buckets (3): content, logs, state
☐ CloudFront distribution
☐ Route53 hosted zone
☐ ACM certificate
☐ WAF web ACL
☐ CloudWatch alarms (3)
☐ DynamoDB table (state lock)
☐ IAM roles
☐ VPC (if applicable)
☐ All connections labeled
```

### CI/CD Pipeline
```
Stages to show:
☐ GitHub repository
☐ GitHub Actions workflow
☐ OIDC authentication
☐ Terraform plan step
☐ Terraform apply step
☐ Dev environment
☐ Prod environment
☐ Branch strategy (develop/main)
```

## 🎨 AWS Icon Reference

### Common Icons
- **Compute**: EC2, Lambda, ECS
- **Storage**: S3, EBS, EFS
- **Database**: RDS, DynamoDB, ElastiCache
- **Networking**: VPC, Route53, CloudFront, ELB
- **Security**: IAM, WAF, Shield, Secrets Manager
- **Management**: CloudWatch, CloudFormation, Systems Manager
- **Developer Tools**: CodePipeline, CodeBuild, CodeDeploy

### Our Project Uses
- S3 (Storage)
- CloudFront (Content Delivery)
- Route53 (DNS)
- WAF (Security)
- CloudWatch (Monitoring)
- DynamoDB (Database)
- IAM (Security)

## 🖼️ Example Layouts

### Simple Flow (Left to Right)
```
User → Route53 → CloudFront → S3
              ↓
            WAF
```

### Layered Architecture (Top to Bottom)
```
┌─────────────────────────────┐
│     Presentation Layer      │
│  (CloudFront + Route53)     │
└─────────────────────────────┘
┌─────────────────────────────┐
│      Security Layer         │
│         (WAF)               │
└─────────────────────────────┘
┌─────────────────────────────┐
│      Storage Layer          │
│         (S3)                │
└─────────────────────────────┘
```

### Hub and Spoke
```
        CloudFront (center)
       /     |      \
      /      |       \
    S3     WAF    Route53
```

## 🎯 Best Practices

### Visual Design
- Use consistent icon sizes
- Align elements on grid
- Group related components
- Use color coding (same service = same color)
- Add white space for readability

### Labels
- Label all connections
- Use action verbs ("fetches", "validates", "stores")
- Include protocols (HTTPS, DNS)
- Show data flow direction

### Technical Details
- Include service names
- Show ports if relevant
- Indicate encryption (TLS, AES256)
- Mark public vs private resources

## 📏 Export Settings

### PNG Export (draw.io)
```
Format: PNG
DPI: 300
Background: Transparent
Border: 10px
Zoom: 100%
```

### SVG Export (draw.io)
```
Format: SVG
Embed fonts: Yes
Include copy of diagram: Yes
```

## 🔄 Update Workflow

1. Edit source file in `docs/architecture/source/`
2. Export to PNG (300 DPI)
3. Save to `docs/architecture/`
4. Update ARCHITECTURE.md if needed
5. Commit both files:
   ```bash
   git add docs/architecture/
   git commit -m "docs: update [diagram-name] architecture diagram"
   ```

## 🛠️ Tools Comparison

| Tool | Pros | Cons | Best For |
|------|------|------|----------|
| draw.io | Free, AWS icons, offline | Manual updates | Custom diagrams |
| Terraform Graph | Auto-generated, accurate | Complex output | Infrastructure |
| CloudCraft | AWS-specific, 3D | Paid, online only | Presentations |
| Lucidchart | Professional, templates | Paid | Team collaboration |

## 📚 Resources

- **AWS Icons**: https://aws.amazon.com/architecture/icons/
- **draw.io**: https://app.diagrams.net/
- **AWS Architecture Blog**: https://aws.amazon.com/blogs/architecture/
- **Diagram Examples**: https://aws.amazon.com/architecture/reference-architecture-diagrams/

## 💡 Tips

1. **Start Simple**: Begin with high-level, add details later
2. **Use Templates**: Copy existing AWS diagrams as starting point
3. **Iterate**: Create draft, get feedback, refine
4. **Version Control**: Save source files, not just exports
5. **Document**: Add notes explaining design decisions

---

**Need Help?** Check [ARCHITECTURE.md](../ARCHITECTURE.md) for detailed requirements
