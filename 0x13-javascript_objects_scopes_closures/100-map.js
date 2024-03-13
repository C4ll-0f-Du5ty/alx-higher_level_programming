#!/usr/bin/node
const k = require('./100-data').list;
const m = k.map((x, i) => x * (i));
console.log(k);
console.log(m);
