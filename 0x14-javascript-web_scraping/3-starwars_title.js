#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let result = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    result = JSON.parse(body);
    console.log(result.title);
  }
});
