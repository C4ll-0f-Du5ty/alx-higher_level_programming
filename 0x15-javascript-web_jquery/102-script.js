
$(document).ready(function () {
    $("INPUT#btn_translate").click(function () {
        const link = "https://hellosalut.stefanbohacek.dev/?lang="
        const lang = $("INPUT#language_code").val()
        $.getJSON(link + lang, function (data) {
            $("DIV#hello").text(data.hello)
        })
    })
})
