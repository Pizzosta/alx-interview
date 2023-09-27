#!/usr/bin/node
// script that prints all characters of a Star Wars movie
// usage ./0-starwars_characters.js {movieID}

const request = require('request');

const movieId = process.argv[2];

const filmsUrl = `https://swapi.dev/api/films/${movieId}/`;

function printCharacters () {
  request(filmsUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(body);
      const characters = film.characters;

      fetchCharacters(characters, 0);
    } else {
      console.error('Failed to fetch movie data.');
    }
  });
}

function fetchCharacters (characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);

      fetchCharacters(characterUrls, index + 1);
    } else {
      console.error('Failed to fetch character data.');
    }
  });
}

printCharacters();
