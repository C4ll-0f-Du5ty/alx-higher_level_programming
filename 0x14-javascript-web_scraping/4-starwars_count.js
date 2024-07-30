#!/usr/bin/node
const request = require('request');
const args = process.argv;
let count = 0;
request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  for (const s of JSON.parse(body).results) {
    for (const m of s.characters) {
      if (m.endsWith('/18/')) { count++; }
    }
  }
  console.log(count);
}
);
