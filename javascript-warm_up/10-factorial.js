#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  }
  // console.log(num)
  return (num * factorial(num - 1));
}

const inputNum = parseInt(process.argv[2]);
// console.log(inputNum)
console.log(factorial(inputNum));
