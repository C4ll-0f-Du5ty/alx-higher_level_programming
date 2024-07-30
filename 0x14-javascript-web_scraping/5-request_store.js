#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv;
request(args[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(args[3], response.body, 'utf8', error => {
    if (error) {
      console.error(error);
    }
  });
}
);
