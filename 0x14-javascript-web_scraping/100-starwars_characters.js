#!/usr/bin/node

// Import module
const request = require('request');

// Assign movie ID from cli args
const movieId = process.argv[2];

// Fetch movie details using Star Wars API and assign
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Requests
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Function fetches and prints movie actor names
  function fetchCharacterName(url) {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character details:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }

  // Fetches and prints each character's name
  characterUrls.forEach(fetchCharacterName);
});

