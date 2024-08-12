$(document).ready(function () {
    $("INPUT#btn_translate").click(fetchTranslation);
    $("INPUT#language_code").keyup(function (event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const link = "https://hellosalut.stefanbohacek.dev/?lang="
        const lang = $("INPUT#language_code").val()
        $.getJSON(link + lang, function (data) {
            $("DIV#hello").text(data.hello)
        })
    }
});
