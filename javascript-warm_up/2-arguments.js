#!/usr/bin/node

num_args = process.argv.length;
num_args = num_args - 2;

if (num_args < 1) {
  console.log('No argument');
} else if (num_args === 1) {
  console.log('Argument found');
} else if (num_args > 1) {
  console.log('Arguments found');
}
