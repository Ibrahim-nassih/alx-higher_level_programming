#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const char = JSON.parse(body).characters;
    printChar(char, 0);
  }
});

function printChar (characters, i) {
  request(characters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printChar(characters, i + 1);
      }
    }
  });
}
