#!/usr/bin/node
const k = require('./100-data').list;
let i = 0;
const m = k.map((x) => x * (i++));
console.log(k);
console.log(m);
