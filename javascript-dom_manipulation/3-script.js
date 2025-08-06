const toggle_header_element = document.getElementById("toggle_header");
const header_element = document.querySelector("header");

toggle_header_element.addEventListener('click', function() {
    if (header_element.classList.contains("red")){
        header_element.classList.remove("red");
        header_element.classList.add("green");
    }
    else {
        header_element.classList.remove("green");
        header_element.classList.add("red");
    }
})