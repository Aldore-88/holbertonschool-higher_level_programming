#!/usr/bin/node

const num_args = process.argv.length - 2;

if (num_args < 1) {
  console.log('No argument');
} else if (num_args === 1) {
  console.log('Argument found');
} else if (num_args > 1) {
  console.log('Arguments found');
}
