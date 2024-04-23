#!/usr/bin/node
//Import the 'request' module.
const request = require('request');
// Construct the URL for the specific Star Wars fil
const url = 'https://swapi-api.alx-tools.comm/api/films/' + process.argv[2];
// Use the 'request' module to preform an HTTP GET request to the constructed URL.
request(url, function(error, response, body){
  // log title is successful, log error if not.
  console.log(error || JSON.parse(body).title);
});
