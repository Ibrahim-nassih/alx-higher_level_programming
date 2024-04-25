#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, esponse, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const todos = data.characters;
  for (const i of todos) {
    request.get(i, function (error, esponse, bodys) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(bodys);
      console.log(data1.name);
    });
  }
});
