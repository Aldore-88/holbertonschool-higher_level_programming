#!/usr/bin/node
// 8. Square
// Write a script that prints a square

const size = process.argv[2];

let countH = 0;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (countH < size) {
    // X
    // X
    // X
    console.log('X'.repeat(size));
    countH += 1;
  }
}
