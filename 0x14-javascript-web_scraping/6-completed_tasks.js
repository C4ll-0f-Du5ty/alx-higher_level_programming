#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  const Users = {};
  for (const s of JSON.parse(response.body)) {
    if (s.completed && Users[s.userId] === undefined) { Users[s.userId] = 1; } else if (s.completed) { Users[s.userId] += 1; }
  }

  console.log(Users);
}
);
