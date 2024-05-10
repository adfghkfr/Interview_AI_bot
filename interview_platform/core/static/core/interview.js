async function adjustTextAreaHeight(field) {
    field.style.height = 'auto';
    field.style.height = `${field.scrollHeight}px`;
}

async function submitQuestion() {
    const input = document.getElementById('user_input');
    const messageContainer = document.getElementById('chat-container');
    const userText = input.value.trim();

    if (userText) {
        messageContainer.innerHTML += `<div>User: ${userText}</div>`;
        const postData = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `user_input=${encodeURIComponent(userText)}`
        };

        try {
            const response = await fetch('/api/interview/', postData);
            const data = await response.json();
            messageContainer.innerHTML += `<div>Bot: ${data.response}</div>`;
            messageContainer.scrollTop = messageContainer.scrollHeight;
            input.value = '';
            await adjustTextAreaHeight(input);
        } catch (error) {
            console.error('Error:', error);
            messageContainer.innerHTML += `<div>Error communicating with the server. Please try again later.</div>`;
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = () => {
    adjustTextAreaHeight(document.getElementById('user_input'));
}