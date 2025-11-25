#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const EXAMS_DIR = path.join(__dirname, '../website/public/exams');

function formatPolicyInText(text) {
    const patterns = [
        /\{\s*\\"Version\\":\s*\\"2012-10-17\\"[^}]*\\"Statement\\"[^}]*\}/g,
        /\{\s*"Version":\s*"2012-10-17"[^}]*"Statement"[^}]*\}/g
    ];

    let formatted = text;

    patterns.forEach(pattern => {
        formatted = formatted.replace(pattern, (match) => {
            try {
                let cleaned = match.replace(/\\"/g, '"').replace(/\s+/g, ' ').trim();
                const policy = JSON.parse(cleaned);
                const prettyJson = JSON.stringify(policy, null, 2);
                return `<br><br><pre class="iam-policy-block"><code>${prettyJson}</code></pre><br>`;
            } catch (e) {
                return match;
            }
        });
    });

    return formatted;
}

function processExamFile(filePath) {
    console.log(`Processing: ${path.basename(filePath)}`);
    
    let content = fs.readFileSync(filePath, 'utf8');
    const questionsMatch = content.match(/const examQuestions = (\[[\s\S]*?\]);/);
    
    if (!questionsMatch) return;

    try {
        const questions = eval(questionsMatch[1]);
        let modified = false;

        questions.forEach((q) => {
            if (q.text && q.text.includes('Version') && q.text.includes('Statement')) {
                const originalText = q.text;
                q.text = formatPolicyInText(q.text);
                if (q.text !== originalText) {
                    modified = true;
                    console.log(`  ✓ Formatted policy in question ${q.number}`);
                }
            }

            if (q.options) {
                Object.keys(q.options).forEach(key => {
                    const originalOption = q.options[key];
                    q.options[key] = formatPolicyInText(q.options[key]);
                    if (q.options[key] !== originalOption) modified = true;
                });
            }
        });

        if (modified) {
            const newQuestionsStr = JSON.stringify(questions, null, 0);
            content = content.replace(questionsMatch[1], newQuestionsStr);

            if (!content.includes('.iam-policy-block')) {
                const cssInsertPoint = content.indexOf('</style>');
                if (cssInsertPoint > 0) {
                    const policyCSS = `
        .iam-policy-block {
            background: #1e1e1e;
            border: 2px solid #3b82f6;
            border-radius: 8px;
            padding: 20px;
            margin: 16px 0;
            overflow-x: auto;
            font-family: 'Courier New', Consolas, Monaco, monospace;
            font-size: 14px;
            line-height: 1.6;
        }
        .iam-policy-block code {
            color: #d4d4d4;
            display: block;
            white-space: pre;
        }
        .dark-mode .iam-policy-block {
            background: #0d1117;
            border-color: #58a6ff;
        }
`;
                    content = content.slice(0, cssInsertPoint) + policyCSS + content.slice(cssInsertPoint);
                }
            }

            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`  ✅ Updated`);
        }
    } catch (e) {
        console.error(`  ❌ Error: ${e.message}`);
    }
}

const examFiles = fs.readdirSync(EXAMS_DIR)
    .filter(f => f.endsWith('.html'))
    .map(f => path.join(EXAMS_DIR, f));

examFiles.forEach(processExamFile);
console.log('\n✅ Done!');
