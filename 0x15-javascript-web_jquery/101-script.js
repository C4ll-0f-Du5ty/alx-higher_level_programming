$(document).ready(function () {
    $("DIV#add_item").click(function () {
        const temp = $("<li>").text("Item")
        $("UL.my_list").append(temp)
    })
    $("DIV#remove_item").click(function () {
        $("UL.my_list li").last().remove()
    })
    $("DIV#clear_list").click(function () {
        $("UL.my_list").empty()
    })
})
