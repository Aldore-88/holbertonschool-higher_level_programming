#!/usr/bin/node
/*
4.List of elements
Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item
*/

const add_item_element = document.getElementById("add_item");
const my_list_element = document.querySelector(".my_list");

add_item_element.addEventListener('click', function(){
    const new_item = document.createElement('li');
    new_item.textContent = "Item";

    my_list_element.appendChild(new_item);
})