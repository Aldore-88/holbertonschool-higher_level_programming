/*
8.Say Hello!
Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.

** I DONT GET THIS TASK, is the website incorrect??? **
*/

document.addEventListener("DOMContentLoaded", function(){
    const hello_element = document.getElementById("hello");

    // fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    fetch("https://stefanbohacek.com/hellosalut/?lang=fr")
    .then((response) => {
            return response.json();
        })
    .then((data_json) => {
        hello_element.textContent = data_json.hello;
    })
})