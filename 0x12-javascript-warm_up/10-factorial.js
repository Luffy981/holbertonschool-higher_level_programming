#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);
let factorial = 1;
for (let i = 1; i < number + 1; i++) {
  factorial = factorial * i;
}
console.log(factorial);
