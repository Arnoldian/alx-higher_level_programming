#!/usr/bin/node

// Modules import
const request = require('request');
const fs = require('fs');

// See if correct no. of args is given
if (process.argv.length !== 4) {
    console.error('Usage: ./5-request_store.js <URL> <file_path>');
    process.exit(1);
}

// Get URL and file path from cli args
const url = process.argv[2];
const filePath = process.argv[3];

// Do GET request to given URL
request(url, (error, response, body) => {
    // Errors check
    if (error) {
        console.error('Error fetching the URL:', error);
        process.exit(1);
    }

    // response status code is OK (200) check
    if (response.statusCode !== 200) {
        console.error('Failed to fetch the page. Status code:', response.statusCode);
        process.exit(1);
    }

    // Body write, to given file w UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            process.exit(1);
        }
        console.log('Content saved to', filePath);
    });
});

