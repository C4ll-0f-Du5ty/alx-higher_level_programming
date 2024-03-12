#!/usr/bin/node
function add(a, b) {
    return parseInt(a) + parseInt(b)
}

const g = process.argv.slice(2)
console.log(add(g[0], g[1]))
