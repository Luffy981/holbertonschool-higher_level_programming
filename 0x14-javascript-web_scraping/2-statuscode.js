#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log('code: %d', response.statusCode);
    return;
  }
  console.log('code: %d', response.statusCode);
});
