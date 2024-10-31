var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();

let dict = new Object;

for (let i = 0; i < input.length; i++) {
  const alpha = input[i].toLowerCase();

  if (dict[alpha]) {
    dict[alpha] += 1
  } else {
    dict[alpha] = 1
  }
}

let items = new Array;

for (let key of Object.keys(dict)) {
  const value = dict[key];
  items.push([value, key]);
}

items.sort((a, b) => b[0] - a[0]);

if (items.length > 1 && items[0][0] === items[1][0]) {
  console.log('?');
} else {
  console.log(items[0][1].toUpperCase());
}