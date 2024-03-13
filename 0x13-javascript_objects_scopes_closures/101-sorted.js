#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize an empty object to hold the new dictionary
const newDict = {};

// Iterate over the imported dictionary
for (const [userId, occurrence] of Object.entries(dict)) {
  // Use the occurrence as a key in the new dictionary
  // If the key doesn't exist, initialize it with an empty array
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  // Append the user ID to the array associated with its occurrence
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
