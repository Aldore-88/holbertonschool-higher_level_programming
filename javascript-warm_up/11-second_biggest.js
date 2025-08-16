#!/usr/bin/node

const onlyNums = process.argv.slice(2);

console.log(onlyNums);
console.log(onlyNums.sort((a, b) => b - a));
