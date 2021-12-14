#!/usr/bin/node
const { argv } = require('process');
argv.sort();
const number = argv.length;
console.log(argv[number - 2]);
