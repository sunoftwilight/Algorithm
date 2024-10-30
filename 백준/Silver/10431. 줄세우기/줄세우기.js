var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0])

for (let tc = 1; tc <= T; tc++) {
  const arr = input[tc].split(' ').map(Number).slice(1);
  let answer = 0;
  let line = [];

  for (let i = 0; i < 20; i++) {
    const higher = line.findIndex((item) => item > arr[i]);

    if (higher !== -1) {
      answer += line.slice(higher).length;
      line.splice(higher, 0, arr[i]);
    } else {
      line.push(arr[i]);
    }
  }

  console.log(`${tc} ${answer}`);
}