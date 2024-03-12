#!/usr/bin/node
const g = process.argv.slice(2);
if (g.length === 0 || isNaN(parseInt(g[0]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < g[0]; i++) {
    console.log('X'.repeat(g[0]));
  }
}
