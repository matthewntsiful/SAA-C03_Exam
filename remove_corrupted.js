const fs = require('fs');
const path = require('path');

const corruptedQuestions = {
  'SAA-C03_Minimal_Exam_14.html': [886],
  'SAA-C03_Minimal_Exam_15.html': [924],
  'SAA-C03_Minimal_Exam_16.html': [218, 219]
};

const examDir = './website/public/exams';

console.log('REMOVING CORRUPTED QUESTIONS\n');
console.log('='.repeat(80));

let totalRemoved = 0;

Object.entries(corruptedQuestions).forEach(([file, qNums]) => {
  const filePath = path.join(examDir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/const examQuestions = (\[.*?\]);/s);
  
  if (match) {
    let questions = JSON.parse(match[1]);
    const originalCount = questions.length;
    
    // Remove corrupted questions
    questions = questions.filter(q => !qNums.includes(q.number));
    
    const removed = originalCount - questions.length;
    
    if (removed > 0) {
      console.log(`\n${file}:`);
      console.log(`  Removed ${removed} corrupted questions: ${qNums.join(', ')}`);
      console.log(`  Questions remaining: ${questions.length}`);
      
      // Replace in file
      const originalJson = match[1];
      const newJson = JSON.stringify(questions);
      content = content.replace(originalJson, newJson);
      
      // Update question count in header
      content = content.replace(/(\d+) Questions/g, `${questions.length} Questions`);
      
      fs.writeFileSync(filePath, content, 'utf8');
      totalRemoved += removed;
    }
  }
});

console.log('\n' + '='.repeat(80));
console.log(`\nTOTAL REMOVED: ${totalRemoved} corrupted questions`);
console.log('\nNote: These questions had missing options and corrupted text.');
console.log('They have been removed to maintain exam integrity.');
