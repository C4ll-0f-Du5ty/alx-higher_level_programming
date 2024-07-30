#!/usr/bin/node
const request = require('request');
const args = process.argv;
request('https://swapi-api.alx-tools.com/api/films/' + args[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
}
);
