#!/usr/bin/node
const request = require('request');
const MovieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieID;
const method = 'GET';

request(url, method, function (error, response, body) {
    request(url, function (error, response, body) {
        if (!error) {
            const characters = JSON.parse(body).characters;
            print
        }
    });

    function print(characters, i) {
        request(characters[i], function (error, response, body) {
            if (!error) {
                console.log(JSON.parse(body).name);
                if (i + 1 < characters.length) {
                    print(characters, i + 1);
                }
            }
        });
    }
});