#!/usr/bin/node

const onlyNums = process.argv.slice(2);
if (onlyNums.length > 1) {
  // console.log(onlyNums);
  console.log(onlyNums.sort((a, b) => b - a));
  console.log(onlyNums[1]);
} else {
  console.log('0');
}
