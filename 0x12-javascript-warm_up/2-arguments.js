#!/usr/bin/node
const g = process.argv.slice(2);
if (g.length === 1) { console.log('Argument found'); }
else if (g.length > 1) { console.log('Arguments found'); }
else { console.log('No argument'); }
