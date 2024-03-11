#!/usr/bin/node
const g = process.argv.slice(2)
if (g.length > 0)
    console.log('Argument found')
else
    console.log('No argument')
