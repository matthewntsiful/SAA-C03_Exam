# Architecture Documentation

> Complete architecture overview for AWS SAA-C03 Exam Suite

## 📐 Architecture Diagrams

### Available Diagrams

1. **[High-Level Architecture](architecture/high-level-architecture.png)** - Overall system design
2. **[AWS Infrastructure](architecture/aws-infrastructure.png)** - AWS resources and connections
3. **[CI/CD Pipeline](architecture/cicd-pipeline.png)** - Deployment workflow
4. **[Application Flow](architecture/application-flow.png)** - User interaction flow
5. **[Data Flow](architecture/data-flow.png)** - Data storage and retrieval

---

## 🏗️ High-Level Architecture

![High-Level Architecture](architecture/high-level-architecture.png)

### Components
- **Frontend**: Static HTML/CSS/JS served via CloudFront
- **Storage**: Browser localStorage (no backend database)
- **CDN**: CloudFront with global edge locations
- **DNS**: Route53 for domain management
- **Security**: WAF for protection, HTTPS only

---

## ☁️ AWS Infrastructure

![AWS Infrastructure](architecture/aws-infrastructure.png)

### AWS Services Used

#### Content Delivery
- **S3 Bucket** (Content)
  - Versioning enabled
  - Encryption at rest (AES256)
  - Public access blocked
  - Origin for CloudFront

- **CloudFront Distribution**
  - Origin Access Control (OAC)
  - Cache policies optimized
  - Compression (Brotli + Gzip)
  - Security headers
  - TLS 1.2+ minimum

#### DNS & SSL
- **Route53 Hosted Zone**
  - A record → CloudFront
  - ACM certificate validation

- **ACM Certificate**
  - Auto-renewal
  - DNS validation

#### Security
- **WAF Web ACL**
  - Rate limiting (2000 req/5min)
  - AWS managed rules
  - Attached to CloudFront

#### Monitoring
- **CloudWatch Alarms**
  - 4xx/5xx error rates
  - WAF blocked requests
  - SNS notifications

#### Logging
- **S3 Bucket** (Logs)
  - CloudFront access logs
  - S3 access logs
  - Lifecycle policies:
    - 30 days → Infrequent Access
    - 90 days → Glacier
    - 365 days → Delete

#### State Management
- **S3 Bucket** (Terraform State)
  - Versioning enabled
  - Encryption enabled
  - DynamoDB locking

- **DynamoDB Table**
  - State locking
  - Prevents concurrent modifications

---

## 🔄 CI/CD Pipeline

![CI/CD Pipeline](architecture/cicd-pipeline.png)

### Workflow

```
┌─────────────┐
│   GitHub    │
│ Repository  │
└──────┬──────┘
       │
       ├─── Push to 'develop' ───┐
       │                         │
       ├─── Push to 'main' ──────┤
       │                         │
       └─── Pull Request ────────┤
                                 │
                                 ▼
                    ┌────────────────────┐
                    │  GitHub Actions    │
                    │  (OIDC Auth)       │
                    └─────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
            ┌───────────────┐   ┌──────────────┐
            │ Terraform Plan│   │ Terraform    │
            │ (PR Check)    │   │ Apply        │
            └───────────────┘   └──────┬───────┘
                                       │
                         ┌─────────────┴─────────────┐
                         │                           │
                         ▼                           ▼
                ┌─────────────────┐         ┌─────────────────┐
                │ Dev Environment │         │ Prod Environment│
                │ (develop branch)│         │ (main branch)   │
                └─────────────────┘         └─────────────────┘
```

### Environments
- **Dev**: Auto-deploy on push to `develop`
- **Prod**: Auto-deploy on push to `main`
- **PR**: Terraform plan only (no apply)

---

## 📱 Application Flow

![Application Flow](architecture/application-flow.png)

### User Journey

```
User → DNS (Route53) → CloudFront → S3 (Origin) → Browser
                           ↓
                        WAF Check
                           ↓
                    Cache Hit/Miss
                           ↓
                    Serve Content
                           ↓
                    Browser Renders
                           ↓
                    localStorage
```

### Key Features Flow

1. **Landing Page**
   - Load exam cards
   - Display progress from localStorage
   - Show analytics dashboard

2. **Exam Taking**
   - Load questions from HTML
   - Auto-save progress every 30s
   - Timer countdown (130 min)
   - Keyboard navigation

3. **Results**
   - Calculate score
   - Save to localStorage
   - Display breakdown by domain
   - Share to social media

4. **Review Mode**
   - Show correct/incorrect answers
   - Display explanations
   - Link to AWS resources

---

## 💾 Data Flow

![Data Flow](architecture/data-flow.png)

### Storage Architecture

```
┌──────────────────────────────────────┐
│         Browser localStorage         │
├──────────────────────────────────────┤
│ • examProgress_{examId}              │
│ • examResults_{examId}_{timestamp}   │
│ • examHistory                        │
│ • userPreferences                    │
│ • flaggedQuestions_{examId}          │
└──────────────────────────────────────┘
```

### Data Structure

**Exam Progress:**
```json
{
  "examId": "exam-01",
  "currentQuestion": 15,
  "answers": {"1": "A", "2": "B,C"},
  "flagged": [5, 12, 23],
  "timeRemaining": 6500,
  "startTime": 1704067200000,
  "lastSaved": 1704067800000
}
```

**Exam Results:**
```json
{
  "examId": "exam-01",
  "score": 78,
  "passed": true,
  "totalQuestions": 65,
  "correctAnswers": 51,
  "timestamp": 1704067200000,
  "timeSpent": 7200,
  "domainBreakdown": {
    "Design Resilient Architectures": {"correct": 12, "total": 15}
  }
}
```

---

## 🔐 Security Architecture

### Layers

1. **Network Layer**
   - WAF rate limiting
   - AWS managed rules
   - HTTPS only (TLS 1.2+)

2. **Application Layer**
   - Security headers (HSTS, CSP, X-Frame-Options)
   - No user authentication (no PII)
   - Client-side only

3. **Storage Layer**
   - S3 encryption at rest
   - Versioning enabled
   - Public access blocked
   - OAC for CloudFront

4. **Access Layer**
   - IAM roles (least privilege)
   - GitHub OIDC (no long-lived credentials)
   - CloudWatch logging

---

## 📊 Monitoring Architecture

### CloudWatch Alarms

1. **CloudFront 4xx Errors** (> 5%)
2. **CloudFront 5xx Errors** (> 1%)
3. **WAF Blocked Requests** (> 100/5min)

### Logging

- **CloudFront Access Logs** → S3
- **S3 Access Logs** → S3
- **Terraform State Changes** → DynamoDB

---

## 🎨 Diagram Tools

### Recommended Tools

1. **draw.io** (diagrams.net)
   - Free, web-based
   - AWS icon library
   - Export to PNG/SVG

2. **Lucidchart**
   - Professional diagrams
   - AWS shapes included
   - Team collaboration

3. **CloudCraft**
   - AWS-specific
   - 3D diagrams
   - Cost estimation

4. **Terraform Graph**
   - Generate from code
   - `terraform graph | dot -Tpng > graph.png`

### Creating Diagrams

```bash
# Install Graphviz (for Terraform graphs)
brew install graphviz

# Generate infrastructure diagram
cd infrastructure/terraform/environments/prod
terraform graph | dot -Tpng > ../../../../docs/architecture/terraform-graph.png
```

---

## 📁 Diagram Files

Place diagram files in `docs/architecture/`:

```
docs/architecture/
├── high-level-architecture.png
├── aws-infrastructure.png
├── cicd-pipeline.png
├── application-flow.png
├── data-flow.png
├── security-architecture.png
├── monitoring-architecture.png
├── terraform-graph.png
├── source/                      # Editable source files
│   ├── high-level.drawio
│   ├── aws-infra.drawio
│   └── cicd.drawio
└── README.md                    # Diagram documentation
```

---

## 🔄 Updating Diagrams

1. Edit source files in `docs/architecture/source/`
2. Export to PNG/SVG
3. Update this documentation if architecture changes
4. Commit both source and exported files

---

## 📚 Additional Resources

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Terraform Graph Documentation](https://www.terraform.io/docs/cli/commands/graph.html)

---

**Last Updated**: January 2025
