#!/usr/bin/node
// 7. I love C
// Write a script that prints x times “C is fun”

const maxCount = parseInt(process.argv[2]);

if (isNaN(maxCount)) {
  'Missing number of occurances';
} else {
  let count = 0;
  while (count < maxCount) {
    console.log('C is fun');
    count += 1;
  }
}
