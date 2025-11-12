# Quick Start Guide 🚀

## 30-Second Start

```bash
cd website
npm install
npm run dev
```

Open: http://localhost:3000

**Done!** 🎉

---

## What You Get

✅ **16 Practice Exams** (1,040 questions)  
✅ **Real Exam Conditions** (130 min, 65 questions)  
✅ **Progress Tracking** (scores, attempts, analytics)  
✅ **Answer Review** (see correct/incorrect)  
✅ **Dark Mode** (eye-friendly)  
✅ **Mobile Ready** (works everywhere)  

---

## How to Use

### 1. Take an Exam
- Click any exam card
- Answer 65 questions
- Use timer (130 minutes)
- Flag questions for review
- Submit when done

### 2. View Results
- See your score (need 72% to pass)
- Click "Review Answers"
- See correct/incorrect answers
- Learn from mistakes

### 3. Track Progress
- View analytics dashboard
- See average score
- Check pass rate
- Monitor improvement

---

## Key Features

### During Exam
- **Pause/Resume** - Take breaks
- **Question Grid** - Jump to any question
- **Flag Questions** - Mark for review
- **Auto-Save** - Resume later (4 hours)
- **Progress Bar** - See completion

### After Exam
- **Score Display** - Percentage and pass/fail
- **Time Taken** - How long you took
- **Review Mode** - See all answers
- **Retake** - Try again
- **Analytics** - Track performance

---

## File Locations

```
website/
├── server.js              # Start here
├── views/minimal.ejs      # Landing page
└── public/exams/          # 16 exam files
```

---

## Common Commands

### Development
```bash
npm run dev          # Start dev server
npm start            # Start production server
```

### Testing
```bash
open http://localhost:3000                    # Landing page
open http://localhost:3000/exams/SAA-C03_Minimal_Exam_01.html  # Exam 1
```

### Clear Data
```javascript
localStorage.clear()  # In browser console
```

---

## Keyboard Shortcuts

- **Arrow Keys** - Navigate questions
- **Space** - Select answer
- **F** - Flag question
- **Enter** - Next question

---

## Tips for Success

1. **Take all 16 exams** - Complete coverage
2. **Review wrong answers** - Learn from mistakes
3. **Aim for 80%+** - Build confidence
4. **Retake failed exams** - Improve weak areas
5. **Track progress** - Monitor improvement

---

## Troubleshooting

### Exam not loading?
- Check browser console (F12)
- Clear localStorage
- Try different browser

### Progress not saving?
- Enable localStorage in browser
- Check browser privacy settings
- Clear old data

### Timer not working?
- Enable JavaScript
- Check browser console
- Refresh page

---

## Documentation

- **[README](README.md)** - Project overview
- **[FEATURES](docs/FEATURES.md)** - Complete feature list
- **[DEPLOYMENT](docs/DEPLOYMENT.md)** - Deploy to AWS
- **[STRUCTURE](docs/PROJECT_STRUCTURE.md)** - File organization

---

## Quick Reference

| Item | Value |
|------|-------|
| Exams | 16 |
| Questions per Exam | 65 |
| Time per Exam | 130 min |
| Passing Score | 72% |
| Total Questions | 1,040 |

---

## Support

**Issues?**
1. Check browser console
2. Clear localStorage
3. Review documentation
4. Try different browser

**Questions?**
- Read [FEATURES.md](docs/FEATURES.md)
- Check [DEPLOYMENT.md](docs/DEPLOYMENT.md)
- Review [README.md](README.md)

---

## Deployment

### AWS (Production)
```bash
cd infrastructure/terraform/environments/dev
terraform init
terraform apply
```

### Static Hosting
```bash
# Netlify
netlify deploy --prod

# Vercel
vercel --prod
```

---

## What's Next?

1. ✅ **Take Exam 1** - Start practicing
2. ✅ **Review Answers** - Learn from mistakes
3. ✅ **Track Progress** - Monitor improvement
4. ✅ **Complete All 16** - Full preparation
5. ✅ **Pass SAA-C03** - Get certified! 🎉

---

**Ready to start? Run `npm run dev` and visit http://localhost:3000**

**Good luck with your AWS certification! 🚀**
