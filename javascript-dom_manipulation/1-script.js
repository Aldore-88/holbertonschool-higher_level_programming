#!/usr/bin/node
/*
1. Click and turn red
Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id red_header
*/

const red_header_element = document.getElementById("red_header");
//document.querySelector('#red_header')
const header_element = document.querySelector("header");

red_header_element.addEventListener('click', function() {
    header_element.style.color = "#FF0000"
});