const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, K] = input[0].trim().split(' ');
const arr = input[1].trim().split(' ').map(Number);

let answer = 0;
let check = new Array(100001).fill(0);

let start = 0;
let end = 0;

while (end < N) {
  if (check[arr[end]] >= K) {
    check[arr[start]] -= 1;
    start++;
  } else {
    check[arr[end]] += 1;
    answer = Math.max(answer, end - start + 1);
    end++;
  }
}

console.log(answer);