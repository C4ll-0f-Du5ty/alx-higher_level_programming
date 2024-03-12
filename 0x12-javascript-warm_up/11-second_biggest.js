#!/usr/bin/node
function sort (arr) {
  for (let i = 0; i < arr.length; i++) {
    let temp = i;
    for (let j = i; j < arr.length; j++) {
      if (arr[j] > arr[temp]) {
        temp = j;
      }
    }
    const c = arr[i];
    arr[i] = arr[temp];
    arr[temp] = c;
  }
}
const g = process.argv.slice(2);
if (g.length === 0 || g.length === 1) {
  console.log(0);
} else {
  sort(g);
  console.log(g[1]);
}
