#!/usr/bin/node
const fs = require('fs');

// Check if the command line arguments are provided
if (process.argv.length <= 3) {
  console.error('Usage: node concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

// Extract file paths from command line arguments
const sourceFile1Path = process.argv[2];
const sourceFile2Path = process.argv[3];
const destinationFilePath = process.argv[4];

// Read the contents of the first source file
fs.readFile(sourceFile1Path, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1Path}:`, err);
    return;
  }

  // Read the contents of the second source file
  fs.readFile(sourceFile2Path, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2Path}:`, err);
      return;
    }

    // Concatenate the contents of the two source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFilePath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFilePath}:`, err);
      }
    });
  });
});
