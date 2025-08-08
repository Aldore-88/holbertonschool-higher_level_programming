#!/usr/bin/node
/*
2. Add `.red` class
Write a JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header
*/


const red_header_element = document.getElementById("red_header");

const header_element = document.querySelector("header");

red_header_element.addEventListener('click', function() {
    header_element.classList.add("red")
});