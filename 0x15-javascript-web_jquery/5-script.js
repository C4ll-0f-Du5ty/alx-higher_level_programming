#!/usr/bin/node
$(document).ready(function () {
    $("DIV#add_item").click(function () {
        const Element = $('<li>').text("Item")
        $("UL.my_list").append(Element)
    })
})
