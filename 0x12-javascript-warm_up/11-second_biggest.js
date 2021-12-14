#!/usr/bin/node
const { argv } = require('process');
if (!argv[3]) {
  console.log(0);
} else if (argv[2] && argv[3]) {
  argv.sort();
  const number = argv.length;
  console.log(argv[number - 2]);
}

