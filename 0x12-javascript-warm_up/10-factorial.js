#!/usr/bin/node
function factorial(x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  }
  return x * factorial(x - 1)
}

const g = process.argv.slice(2);
console.log(factorial(parseInt(g[0])));

