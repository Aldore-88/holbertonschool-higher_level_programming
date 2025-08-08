const update_header_element = document.getElementById("update_header");
const header_element = document.querySelector("header")

update_header_element.addEventListener('click', function() {
    header_element.innerHTML = "New Header!!!";
})