#!/usr/bin/node
const g = process.argv.slice(2);
if (!isNaN(parseInt(g[0]))) {
  console.log('My number:', g[0])
} else {
  console.log('Not a number')
}
