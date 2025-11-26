const fs = require('fs');
const path = require('path');

const examDir = './website/public/exams';
const files = fs.readdirSync(examDir).filter(f => f.startsWith('SAA-C03_Minimal_Exam_') && f.endsWith('.html'));

console.log('CRITICAL DATA CORRUPTION REPORT\n');
console.log('=' .repeat(80));

let totalIssues = 0;

files.forEach(file => {
  const filePath = path.join(examDir, file);
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/const examQuestions = (\[.*?\]);/s);
  
  if (match) {
    const questions = JSON.parse(match[1]);
    const problematic = questions.filter(q => {
      const correctLetters = q.correct.split('');
      return correctLetters.some(letter => !q.options[letter]);
    });
    
    if (problematic.length > 0) {
      console.log(`\n${file}:`);
      console.log('-'.repeat(80));
      
      problematic.forEach(q => {
        totalIssues++;
        const correctLetters = q.correct.split('');
        const missing = correctLetters.filter(letter => !q.options[letter]);
        
        console.log(`\nQuestion ${q.number}:`);
        console.log(`  Correct Answer: ${q.correct}`);
        console.log(`  Available Options: ${Object.keys(q.options).join(', ')}`);
        console.log(`  MISSING OPTIONS: ${missing.join(', ')}`);
        console.log(`  Text: ${q.text.substring(0, 100)}...`);
        
        // Check if option is merged
        Object.entries(q.options).forEach(([key, value]) => {
          const nextLetter = String.fromCharCode(key.charCodeAt(0) + 1);
          if (value.includes(` ${nextLetter}. `)) {
            console.log(`  ⚠️  Option ${key} contains merged option ${nextLetter}`);
            console.log(`     Value: ${value.substring(0, 150)}...`);
          }
        });
      });
    }
  }
});

console.log('\n' + '='.repeat(80));
console.log(`\nTOTAL ISSUES FOUND: ${totalIssues}`);
console.log('\nACTION REQUIRED: These questions need manual data correction.');
console.log('The source data has parsing errors where options are merged together.');
