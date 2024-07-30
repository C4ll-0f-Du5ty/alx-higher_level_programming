#!/usr/bin/node
const request = require('request');
const args = process.argv;
request('https://swapi-api.alx-tools.com/api/films/' + args[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  printSynchronous(characters, 0);
}
);

function printSynchronous (characters, index) {
    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        console.log(JSON.parse(body).name);
        if (index + 1 < characters.length) {
          printSynchronous(characters, ++index)
        }
      }
    }
    );
}
