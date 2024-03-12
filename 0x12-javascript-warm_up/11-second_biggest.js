#!/usr/bin/node
const g = process.argv.slice(2);
if (g.length === 0 || g.length === 1) {
  console.log(0);
} else {
  const m = Math.max(...g);
  let k = 0;
  for (let i = 0; i < g.length; i++) {
    if (g[i] < m && g[i] > k) {
      k = g[i];
    }
  }
  console.log(k);
}
