const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [p, m] = input[0].split(' ').map(Number);
const arr = input.slice(1).map(item => item.trim());

let rooms = new Object;
let createNum = 1;

const newRoom = (nick, newLevel, leader) => {
  rooms[nick] = {
    'level': newLevel,
    'create': createNum,
    'members': [leader],
  };

  createNum += 1;
}

for (const user of arr) {
  const myLevel = Number(user.split(' ')[0]);
  const myNick = user.split(' ')[1];
  const roomNames = Object.keys(rooms);
  let canEnter = [];

  if (roomNames.length > 0) {    
    for (const name of roomNames) {
      if (rooms[name].level - 10 <= myLevel && myLevel <= rooms[name].level + 10) {
        canEnter.push(name);
      }
    }

    let goRoom = canEnter[0];

    for (let enter of canEnter) {
      if (rooms[enter].members.length < m) {
        goRoom = enter;
        break;
      }
    }

    if (goRoom && rooms[goRoom].members.length < m) {
      rooms[goRoom].members.push(user);
    } else {
      newRoom(myNick, myLevel, user);
    }
  } else {
    newRoom(myNick, myLevel, user);
  }
}

for (let item in rooms) {
  const result = rooms[item].members.sort((a, b) => a.split(' ')[1].localeCompare(b.split(' ')[1]));

  if (result.length >= m) {
    console.log('Started!');
  } else {
    console.log('Waiting!');
  }
  
  for (let u of result) {
    console.log(u);
  }
}