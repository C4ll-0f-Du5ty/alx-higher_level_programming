#!/usr/bin/node
function factorial(x, y) {
    if (y > 1) {
        factorial(x * (y - 1), y - 1);
    }
    else {
        console.log(x);
    }

}

const g = process.argv.slice(2)
if (g[0] === undefined) {
    console.log(1)
} else {
    console.log(factorial(parseInt(g[0]), parseInt(g[0])))
}
