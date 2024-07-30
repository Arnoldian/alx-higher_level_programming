#!/usr/bin/node

// Declarations and assignments
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles' ID

// Requests and writes to console
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;
  const moviesWithWedge = films.filter(film => 
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(moviesWithWedge.length);
});

