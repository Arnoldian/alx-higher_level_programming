#!/usr/bin/node

// Import "fs" module, works w/ file system
const fs = require('fs');

// Get file path from cli args
const filePath = process.argv[2];

// Function to read/print content of file
function readFile(filePath) {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            // error occurs then print error object
            console.error(err);
        } else {
            // successful then print content of file
            console.log(data);
        }
    });
}

// function call with provided file path
readFile(filePath);

