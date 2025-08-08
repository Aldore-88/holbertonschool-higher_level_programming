console.log("script started")
const update_header_element = document.getElementById("update_header");
const header_element = document.querySelector("header")

update_header_element.addEventListener('click', function() {
    header_element.innerHTML = "New Header!!!";

    console.log(header_element);
    console.log("woo");
})  
console.log("event still running");