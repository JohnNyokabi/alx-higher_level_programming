#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
    if (!error) {
	const res = JSON.parse(body).res;
	console.log(res.reduce((count, movie) => {
	    return movie.characters.find((characters) => character.endsWith('/18/'))
		? count + 1
	        : count;
	}, 0));
    }
});
