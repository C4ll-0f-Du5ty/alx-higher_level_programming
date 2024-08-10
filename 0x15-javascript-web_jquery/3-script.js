#!/usr/bin/node

const div = document.querySelector("DIV#red_header")
const header = document.querySelector("header")
div.addEventListener("click", function () {
    header.classList.add("red")
})
