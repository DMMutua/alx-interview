#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

axios
  .get(apiUrl)
  .then((response) => {
    const film = response.data;
    const characters = film.characters;

    const characterRequests = characters.map((characterUrl) => {
      return axios.get(characterUrl);
    });

    axios.all(characterRequests)
      .then(axios.spread((...responses) => {
        responses.forEach((response) => {
          const character = response.data;
          console.log(character.name);
        });
      }))
      .catch((error) => {
        console.error('Error:', error);
      });
  })
  .catch((error) => {
    console.error('Error:', error);
  });
