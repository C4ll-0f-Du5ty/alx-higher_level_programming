#!/usr/bin/node
const g = process.argv.slice(2);
const t = 'C is fun';
if (g.length === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < g[0]; i++) {
    console.log(t);
  }
}
