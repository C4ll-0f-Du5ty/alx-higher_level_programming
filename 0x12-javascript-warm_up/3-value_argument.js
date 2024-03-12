#!/usr/bin/node
const g = process.argv.slice(2);
if (g.length === 0) {
  console.log('No argument');
} else {
  console.log(String(g));
}
