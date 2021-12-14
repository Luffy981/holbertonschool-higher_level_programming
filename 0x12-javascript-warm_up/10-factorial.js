#!/usr/bin/node
const { argv } = require('process');
let number = parseInt(argv[2]);
function Factorial(number) {
  if (!number)
    console.log(1);
    return;
  if (number !== 0) {
    return(number * Factorial(number - 1));
  }
  return;
}
Factorial(number);
