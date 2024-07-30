#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(response.statusCode);
}
);
