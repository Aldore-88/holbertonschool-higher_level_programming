#!/usr/bin/node
/*
6.Star wars character
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/

const URL_json = "https://swapi-api.hbtn.io/api/people/5/?format=json";
const character_element = document.getElementById("character");

fetch(URL_json)
    .then((response) => {
        console.log("First .then() received:", response);
        return response.json();
    })
    .then((data) => {
        console.log("Second .then() received:", data);
        ActorName.textContent = data.name;
    });
