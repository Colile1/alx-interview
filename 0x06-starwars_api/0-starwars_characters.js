#!/usr/bin/node
// Prints all characters of a Star Wars movie by Movie ID using the Star Wars API
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  if (res.statusCode !== 200) {
    console.error(`Error: Status code ${res.statusCode}`);
    process.exit(1);
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  const printCharacter = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (err, res, body) => {
      if (!err && res.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
        printCharacter(index + 1);
      } else {
        console.error('Error fetching character');
        process.exit(1);
      }
    });
  };
  printCharacter(0);
});
