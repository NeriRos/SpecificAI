document.getElementById('prompt_form').addEventListener("submit", async function (e) {
    e.preventDefault();
    toggleLoading(true)
    const formData = new FormData(e.target);
    try {
        const response = await sendQuestion(formData.get('prompt'), formData.get('action'));
        await parseAnswer(await response.json())
    } catch (e) {
        console.error(e)
        alert('Something went wrong. Please try again.')
    } finally {
        toggleLoading(false)
    }
})

async function sendQuestion(prompt, action) {
    return await fetch('/query/execute', {
        method: "POST",
        body: JSON.stringify({prompt, action}),
        headers: {
            'Content-Type': 'application/json'
        }
    });
}

async function parseAnswer(answers) {
    for (const answer of answers) {
        const item = document.createElement('p')
        item.innerText = answer.text;

        document.getElementById('answers__list').appendChild(item)
    }

    document.getElementById('answers').style.display = 'block';
}

function toggleLoading(status) {
    if (status) {
        document.getElementById('loading').style.display = 'block';
        document.getElementById('submit').style.display = 'none';
    } else {
        document.getElementById('submit').style.display = 'block';
        document.getElementById('loading').style.display = 'none';
    }
}

function reset() {
    document.getElementById('answers').style.display = 'none';
    document.getElementById('answers__list').innerHTML = '';
}