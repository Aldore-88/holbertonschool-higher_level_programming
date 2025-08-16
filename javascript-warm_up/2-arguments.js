#!/usr/bin/node
// 2. Arguments
// Write a script that prints a message depending of the number of arguments passed:

const numArgs = process.argv.length - 2;

if (numArgs < 1) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else if (numArgs > 1) {
  console.log('Arguments found');
}
