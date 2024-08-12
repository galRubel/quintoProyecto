const form = document.getElementById('chat-form');
const mytextInput = document.getElementById('mytext');
const responseTextarea = document.getElementById('response');

const API_KEY = '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';

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const mytext = mytextInput.value.trim();

    if (mytext) {
        try {
            const response = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${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}`,
                },
                body: JSON.stringify({
                    model: 'gpt-4',
                    messages: [{ role: 'user', content: mytext }],
                    temperature: 1.0,
                    top_p: 0.7,
                    n: 1,
                    stream: false,
                    presence_penalty: 0,
                    frequency_penalty: 0,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                responseTextarea.value = data.choices[0].message.content;
            } else {
                responseTextarea.value = 'Error: Unable to process your request.';
            }
        } catch (error) {
            console.error(error);
            responseTextarea.value = 'Error: Unable to process your request.';
        }
    }
});