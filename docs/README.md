# SAA-C03 Practice Exams - Node.js

Professional AWS Solutions Architect Associate practice exam suite built with Node.js.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Deploy to S3
npm run deploy
```

## 📁 Project Structure

```
├── server.js                 # Express server
├── scripts/
│   ├── build.js              # Build script
│   └── deploy.js             # S3 deployment
├── SAA-C03_Complete_Exam_Suite/
│   ├── Enhanced_HTML_Quizzes/ # Practice exams
│   └── Analytics_Dashboard/   # Performance analytics
└── public/                   # Built assets
```

## 🌐 Routes

- `/` - Home page with exam list
- `/exams/*` - Practice exam files
- `/analytics/*` - Analytics dashboard
- `/api/exams` - Exam metadata API

## 🔧 Environment Variables

```bash
PORT=3000                     # Server port
S3_BUCKET=your-bucket-name    # S3 bucket for deployment
```

## 📊 Features

- ✅ 16 Professional practice exams
- ✅ Real-time timer and progress tracking
- ✅ Auto-save functionality
- ✅ Performance analytics
- ✅ Mobile responsive design
- ✅ S3 deployment ready