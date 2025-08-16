#!/usr/bin/node
// 5. An Integer
// Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const arg = process.argv;
const isNum = parseInt(arg[2]);

if (isNaN(isNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + isNum);
}
