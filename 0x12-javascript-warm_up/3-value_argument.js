#!/usr/bin/node
const g = process.argv.slice(2);
if (g[0] === undefined) {
  console.log('No argument');
} else {
  console.log(g[0]);
}
