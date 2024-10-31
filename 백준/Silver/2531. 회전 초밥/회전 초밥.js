const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, dishes, seq, coup] = input[0].split(' ').map(Number);
let line = input.slice(1).map(item => Number(item.trim()));

const circleLine = line.concat(line.slice(0, seq-1));

let check = Array.from({length: dishes + 1}, x => 0);
let counting = 0;

for (let i = 0; i < seq; i++) {
  check[circleLine[i]] += 1;
}
check[coup] += 1;

let answer = check.filter(x => x !== 0).length;

let outWindow = 0;
let inWindow = outWindow + seq;

while (outWindow < N - 1) {
  check[circleLine[outWindow]] -= 1;
  check[circleLine[inWindow]] += 1;

  const cou = check.filter(x => x !== 0).length;
  answer = Math.max(answer, cou);

  outWindow++;
  inWindow++;
}

console.log(answer);
