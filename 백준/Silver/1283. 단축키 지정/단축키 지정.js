const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input[0]);
const texts = input.slice(1).map(x => x.trim());
let answer = [];
let key = [];

for (const txt of texts) {
  const origin = txt.split(' ');
  const word = origin.map(x => x.toLowerCase());

  let flag = false;
  let keyTxt = '';

  for (let i = 0; i < word.length; i++) {
    if (key.includes(word[i][0])) {
      keyTxt += `${origin[i]} `;
      continue;
    } else {
      key.push(word[i][0]);
      flag = true;
      
      keyTxt += `[${origin[i][0]}]${origin[i].slice(1)}`;

      if (i !== word.length - 1) {
        keyTxt += ' '
      }

      for (let k = i+1; k < word.length; k++) {
        keyTxt += `${origin[k]} `;
      }

      answer.push(keyTxt);
      break;
    }
  }

  if (!flag) {
    const lowerTxt = txt.toLowerCase();

    for (let j = 0; j < txt.length; j++) {
      if (txt[j] === ' ') {
        continue;
      }
      if (key.includes(lowerTxt[j])) {
        if (j === txt.length - 1) {
          answer.push(txt);
        }
        continue;
      } else {
        const tmp = `${txt.slice(0, j)}[${txt[j]}]${txt.slice(j+1)}`;
        key.push(lowerTxt[j]);
        answer.push(tmp);
        break;
      }
    }
  }
}

for (item of answer) {
  console.log(item);
}