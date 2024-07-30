#!/usr/bin/node

const fs = require('fs');

// Get cli args
const filePath = process.argv[2];
const content = process.argv[3];

// Function writes content to file
function writeToFile(filePath, content) {
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error(err);
        } else {
            console.log('File written successfully');
        }
    });
}

// Function call w given args
writeToFile(filePath, content);

