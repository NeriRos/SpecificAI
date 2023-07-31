window.onload = () => {
    document.getElementById('topic_form').addEventListener("submit", async function (e) {
        e.preventDefault();
        window.location = '/query?topic=' + document.getElementById('topic').value;
    })
}