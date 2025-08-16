#!/usr/bin/node
// 6. Loop to languages
// Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let count = 0;
const max = lines.length;

while (count < max) {
  console.log(lines[count]);
  count += 1;
  // console.log(count + "and" + max)
}
