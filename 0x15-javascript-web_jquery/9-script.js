#!/usr/bin/node

$(document).ready(function () {
    const link = "https://hellosalut.stefanbohacek.dev/?lang=fr"
    $.get(link, function (data) {
        $("DIV#hello").text(data.hello)
    })
})
