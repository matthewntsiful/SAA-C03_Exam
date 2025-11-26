# Architecture Documentation Setup

> Complete setup for architecture diagrams in SAA-C03 Exam Suite

## ✅ What Was Created

### Directory Structure
```
docs/architecture/
├── README.md                    # Diagram inventory & guidelines
├── ARCHITECTURE.md              # Main architecture documentation
├── DIAGRAM_GUIDE.md             # Quick creation guide
├── ARCHITECTURE_SETUP.md        # This file
├── .gitkeep                     # Preserve directory
└── source/                      # Editable source files
    └── .gitkeep                 # Preserve directory
```

### Scripts
```
scripts/
└── generate-terraform-diagram.sh   # Auto-generate infrastructure diagram
```

### Documentation Updates
- Main README.md updated with architecture link
- Project structure updated to show architecture directory

## 📐 Diagrams to Create

### Priority 1 (Essential)
1. **High-Level Architecture** - Overall system design
2. **AWS Infrastructure** - AWS resources topology
3. **CI/CD Pipeline** - GitHub Actions workflow

### Priority 2 (Important)
4. **Application Flow** - User interaction flow
5. **Data Flow** - localStorage structure

### Priority 3 (Nice to Have)
6. **Security Architecture** - Security layers
7. **Monitoring Architecture** - CloudWatch setup
8. **Terraform Graph** - Auto-generated infrastructure

## 🚀 Next Steps

### 1. Generate Terraform Diagram (Automated)
```bash
# Install graphviz if not already installed
brew install graphviz

# Generate diagram
./scripts/generate-terraform-diagram.sh
```

### 2. Create Manual Diagrams

**Option A: Using draw.io (Recommended)**
1. Visit https://app.diagrams.net/
2. Enable AWS icon library
3. Create diagrams following [DIAGRAM_GUIDE.md](DIAGRAM_GUIDE.md)
4. Save source to `source/` directory
5. Export PNG to `architecture/` directory

**Option B: Using CloudCraft**
1. Visit https://www.cloudcraft.co/
2. Design AWS architecture
3. Export as PNG
4. Save to `architecture/` directory

### 3. Update Documentation
- Mark diagrams as complete in [README.md](README.md)
- Update [ARCHITECTURE.md](ARCHITECTURE.md) with actual diagram references
- Commit all files to git

## 📋 Diagram Requirements

### High-Level Architecture
**File**: `high-level-architecture.png`  
**Components**:
- User/Browser
- Route53 (DNS)
- CloudFront (CDN)
- S3 (Content)
- WAF (Security)
- localStorage (Client-side)

**Flow**: User → DNS → CDN → Origin → Browser → localStorage

### AWS Infrastructure
**File**: `aws-infrastructure.png`  
**Resources**:
- 3 S3 buckets (content, logs, state)
- CloudFront distribution
- Route53 hosted zone
- ACM certificate
- WAF web ACL
- 3 CloudWatch alarms
- DynamoDB table
- IAM roles

**Connections**: Show all resource relationships

### CI/CD Pipeline
**File**: `cicd-pipeline.png`  
**Stages**:
- GitHub repository
- GitHub Actions (OIDC)
- Terraform plan/apply
- Dev environment
- Prod environment

**Branches**: develop → dev, main → prod

## 🎨 Style Guidelines

### Colors
- AWS Orange: `#FF9900`
- Primary Blue: `#232F3E`
- Success Green: `#10B981`
- Warning Yellow: `#F59E0B`
- Error Red: `#EF4444`

### Layout
- 16px grid spacing
- Consistent icon sizes
- Clear labels on all connections
- Directional arrows
- Legend if needed

### Export Settings
- Format: PNG
- Resolution: 300 DPI
- Background: Transparent or white
- Min width: 1920px

## 🛠️ Tools & Resources

### Diagram Tools
- **draw.io**: https://app.diagrams.net/ (Free, recommended)
- **Lucidchart**: https://www.lucidchart.com/ (Paid)
- **CloudCraft**: https://www.cloudcraft.co/ (AWS-specific)
- **Graphviz**: `brew install graphviz` (CLI)

### AWS Resources
- **AWS Icons**: https://aws.amazon.com/architecture/icons/
- **Architecture Center**: https://aws.amazon.com/architecture/
- **Reference Diagrams**: https://aws.amazon.com/architecture/reference-architecture-diagrams/

### Documentation
- [README.md](README.md) - Diagram inventory
- [ARCHITECTURE.md](ARCHITECTURE.md) - Main documentation
- [DIAGRAM_GUIDE.md](DIAGRAM_GUIDE.md) - Creation guide

## ✅ Completion Checklist

### Setup (Complete)
- [x] Create architecture directory
- [x] Create source directory
- [x] Create documentation files
- [x] Create diagram generation script
- [x] Update main README
- [x] Update project structure

### Diagrams (Pending)
- [ ] High-level architecture
- [ ] AWS infrastructure
- [ ] CI/CD pipeline
- [ ] Application flow
- [ ] Data flow
- [ ] Security architecture
- [ ] Monitoring architecture
- [ ] Terraform graph

### Documentation (Pending)
- [ ] Update diagram status in README
- [ ] Add actual diagram references
- [ ] Document design decisions
- [ ] Create diagram changelog

## 📝 Commit Message Template

```bash
# When adding diagrams
git add docs/architecture/
git commit -m "docs: add [diagram-name] architecture diagram

- Created [diagram-name].png
- Added source file [diagram-name].drawio
- Updated documentation references
"

# When updating diagrams
git commit -m "docs: update [diagram-name] architecture diagram

- Updated [component] to reflect [change]
- Refreshed export with latest design
"
```

## 🔄 Maintenance

### When to Update Diagrams
- Infrastructure changes (new AWS resources)
- Architecture changes (new components)
- CI/CD pipeline updates
- Major feature additions
- Security improvements

### Update Process
1. Edit source file in `source/`
2. Re-export to PNG
3. Update ARCHITECTURE.md if needed
4. Update README.md status
5. Commit both source and export

## 💡 Tips

1. **Start with Terraform Graph**: Auto-generate infrastructure diagram first
2. **Use Templates**: Copy AWS reference architectures as starting point
3. **Iterate**: Create draft, review, refine
4. **Keep Source Files**: Always save editable versions
5. **Document Changes**: Note why architecture evolved

## 📞 Support

### Issues
- Diagram tool questions → Check [DIAGRAM_GUIDE.md](DIAGRAM_GUIDE.md)
- Architecture questions → Check [ARCHITECTURE.md](ARCHITECTURE.md)
- Setup questions → Check this file

### Resources
- AWS Architecture Blog: https://aws.amazon.com/blogs/architecture/
- draw.io Tutorials: https://www.diagrams.net/doc/
- Terraform Graph Docs: https://www.terraform.io/docs/cli/commands/graph.html

---

**Status**: ✅ Setup Complete - Ready for diagram creation  
**Last Updated**: January 2025
