#!/usr/bin/node
const request = require('request');
const MovieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieID;
const method = 'GET';

request(url, method, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        const characters = JSON.parse(body).characters;
        for (const character of characters) {
            request(character, method, function (error, response, body) {
                if (error) {
                    console.log(error);
                } else {
                    console.log(JSON.parse(body).name);
                }
            });
        }
    }
});