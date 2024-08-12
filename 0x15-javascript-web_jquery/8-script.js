#!/usr/bin/node

$(document).ready(function () {
    const link = "https://swapi-api.alx-tools.com/api/films/?format=json"
    $.get(link, function (data) {
        for (r of data.results) {
            let temp = $("<li>").text(r.title)
            $("UL#list_movies").append(temp)
        }
    })
})
