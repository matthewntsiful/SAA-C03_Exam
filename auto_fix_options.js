const fs = require('fs');
const path = require('path');

function fixMergedOptions(questions) {
  let fixed = 0;
  
  questions.forEach(q => {
    // Check each option for merged content
    Object.keys(q.options).forEach(key => {
      const value = q.options[key];
      const nextLetter = String.fromCharCode(key.charCodeAt(0) + 1);
      
      // Pattern: "text. F. more text" or "text F. more text"
      const pattern = new RegExp(`\\s*${nextLetter}\\.\\s+(.+)$`);
      const match = value.match(pattern);
      
      if (match) {
        // Split the merged options
        const currentText = value.substring(0, value.indexOf(match[0])).trim();
        const nextText = match[1].trim();
        
        q.options[key] = currentText;
        q.options[nextLetter] = nextText;
        
        console.log(`  ✓ Fixed Q${q.number}: Split option ${key} and ${nextLetter}`);
        fixed++;
      }
    });
  });
  
  return fixed;
}

const examDir = './website/public/exams';
const files = fs.readdirSync(examDir).filter(f => f.startsWith('SAA-C03_Minimal_Exam_') && f.endsWith('.html'));

console.log('AUTO-FIXING MERGED OPTIONS\n');
console.log('='.repeat(80));

let totalFixed = 0;

files.forEach(file => {
  const filePath = path.join(examDir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/const examQuestions = (\[.*?\]);/s);
  
  if (match) {
    const questions = JSON.parse(match[1]);
    const originalJson = match[1];
    
    const fixedCount = fixMergedOptions(questions);
    
    if (fixedCount > 0) {
      console.log(`\n${file}: Fixed ${fixedCount} questions`);
      
      // Replace the questions array in the file
      const newJson = JSON.stringify(questions);
      content = content.replace(originalJson, newJson);
      
      fs.writeFileSync(filePath, content, 'utf8');
      totalFixed += fixedCount;
    }
  }
});

console.log('\n' + '='.repeat(80));
console.log(`\nTOTAL FIXED: ${totalFixed} questions`);
