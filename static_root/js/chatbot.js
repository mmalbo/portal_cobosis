// static/js/chatbot.js
let chatHistory = [];

async function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        appendMessage(message, true);
        userInput.value = '';
        
        // Mostrar indicador de escritura
        showTypingIndicator();
        
        try {
            const response = await fetch('/api/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                appendMessage(data.message, false);
            } else {
                appendMessage('Error: No se pudo procesar tu mensaje', false);
            }
        } catch (error) {
            appendMessage('Error de conexión. Intenta nuevamente.', false);
        } finally {
            hideTypingIndicator();
        }
    }
}

// Función para obtener el token CSRF
function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue || '';
}