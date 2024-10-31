var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const info = input.slice(1).map((item) => item.trim().split(' ').map(Number));
const rank = Array.from({length: info.length}, x => 1);

for (let i = 0; i < info.length; i++) {
  const [myW, myH] = info[i];

  for (let j = 0; j < info.length; j++) {
    if (i !== j) {
      const [yourW, yourH] = info[j];

      if (myW < yourW && myH < yourH) {
        rank[i] += 1;
      }
    }
  }
}

console.log(rank.join(' '));
