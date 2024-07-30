#!/usr/bin/node

// Import Module
const request = require('request');

// Get movie id through cli
const movieId = process.argv[2];

// Declaration and assignment
const url = `https://swapi.dev/api/films/${movieId}/`;

// Requests
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});

