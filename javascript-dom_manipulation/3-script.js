#!/usr/bin/node
/*
3.Toggle classes
Write a JavaScript script that toggles the class of the header element when the user clicks on the tag id toggle_header
*/

const toggle_header_element = document.getElementById("toggle_header");
const header_element = document.querySelector("header");

toggle_header_element.addEventListener('click', function() {
        header_element.classList.toggle("red");
        header_element.classList.toggle("green");
})