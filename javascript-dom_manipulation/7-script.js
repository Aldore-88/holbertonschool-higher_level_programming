/*
7.Star Wars movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
*/

const URL_data = "https://swapi-api.hbtn.io/api/films/?format=json";
const list_element = document.getElementById("list_movies");

fetch(URL_data)
    .then((response) => {
        return response.json();
    })
    .then((data_json) => {
        // console.log("received:", data_json.results);
        const title_count = data_json.results.length;
        // console.log(title_count);

        for (let i=0; i < title_count; i++){

            const new_title = document.createElement('li');
            new_title.textContent = data_json.results[i].title;

            list_element.appendChild(new_title);
        };
    });