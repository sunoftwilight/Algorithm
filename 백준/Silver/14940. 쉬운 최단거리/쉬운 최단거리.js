const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const direct = [[0, 1], [1, 0], [0, -1], [-1, 0]];

const [n, m] = input[0].trim().split(' ').map(Number);
const arr = input.slice(1).map(x => x.split(' ').map(Number));

let ans = [];

for (let a = 0; a < n; a++) {
  ans.push(new Array(m).fill(-1));
}

let [tgR, tgC] = [0, 0];

for (let i = 0; i < n; i++) {
  const tmp = arr[i].findIndex(x => x === 2);

  if (tmp !== -1) {
    [tgR, tgC] = [i, tmp];
    break;
  }
}

let visited = [];

for (let a = 0; a < n; a++) {
  visited.push(new Array(m).fill(false));
}

let Q = [];

Q.push([tgR, tgC, 0]);
visited[tgR][tgC] = true;
ans[tgR][tgC] = 0;

while (Q.length > 0) {
  const [ci, cj, dis] = Q.shift();

  for (let dir of direct) {
    const [di, dj] = dir
    const [ni, nj] = [ci + di, cj + dj];
    
    if (0 <= ni && ni < n && 0 <= nj && nj < m && arr[ni][nj] !== 0 && !visited[ni][nj]) {
      visited[ni][nj] = true;
      ans[ni][nj] = dis+1
      Q.push([ni, nj, dis+1]);
    }
  }
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (arr[i][j] === 0 || arr[i][j] === 2) {
      ans[i][j] = 0;
    }
  }

  console.log(ans[i].join(' '));
}