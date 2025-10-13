// static/js/chatbot_http.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Chatbot HTTP script loaded'); // Para debug
    
    // Elementos del DOM
    const chatButton = document.getElementById('open-chat');
    const chatContainer = document.getElementById('chat-container');
    const minimizeButton = document.getElementById('minimize-chat');
    const closeButton = document.getElementById('close-chat');
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-btn');
    const typingIndicator = document.getElementById('typing-indicator');
    
    console.log('Elements:', {chatButton, chatContainer, chatMessages}); // Debug
    
    let isChatOpen = false;
    let chatHistory = [];
    
    // Función para mostrar/ocultar chat
    function toggleChat(show) {
        if (show) {
            chatContainer.style.display = 'block';
            chatButton.style.display = 'none';
            isChatOpen = true;
            userInput.focus();
            
            // Animación de entrada
            setTimeout(() => {
                chatContainer.classList.add('show');
            }, 10);
        } else {
            chatContainer.classList.remove('show');
            setTimeout(() => {
                chatContainer.style.display = 'none';
                chatButton.style.display = 'block';
                isChatOpen = false;
            }, 30000);
        }
    }
    
    // Función para mostrar un mensaje en el chat
    function appendMessage(message, isUser = false, sender = null) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(isUser ? 'message-user' : 'message-bot');
        
        if (sender && !isUser) {
            messageDiv.innerHTML = `<div class="fw-bold">${sender}</div>${message}`;
        } else {
            messageDiv.textContent = message;
        }
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Guardar en historial
        chatHistory.push({
            message: message,
            isUser: isUser,
            timestamp: new Date().toISOString()
        });
    }
    
    // Mostrar indicador de "escribiendo"
    function showTypingIndicator() {
        typingIndicator.style.display = 'block';
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Ocultar indicador de "escribiendo"
    function hideTypingIndicator() {
        typingIndicator.style.display = 'none';
    }
    
    // Función para obtener el token CSRF
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, 10) === 'csrftoken=') {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Función para enviar mensaje via AJAX
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        // Mostrar mensaje del usuario
        appendMessage(message, true);
        userInput.value = '';
        
        // Mostrar indicador de escritura
        showTypingIndicator();
        
        try {
            // Enviar petición al servidor
            const response = await fetch('/chatbot/api/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    message: message,
                    history: chatHistory.slice(-10)
                })
            });
            
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.status === 'success') {
                appendMessage(data.message, false, '🤖 Asistente');
            } else {
                appendMessage('⚠️ No se pudo procesar tu solicitud. Intenta nuevamente.', false);
            }
            
        } catch (error) {
            console.error('Error:', error);
            appendMessage('❌ Error de conexión. Por favor, intenta más tarde.', false);
            
        } finally {
            hideTypingIndicator();
        }
    }
    
    // Event Listeners
    if (chatButton) {
        chatButton.addEventListener('click', function() {
            console.log('Open chat button clicked');
            toggleChat(true);
        });
    }
    
    if (minimizeButton) {
        minimizeButton.addEventListener('click', function() {
            toggleChat(false);
        });
    }
    
    if (closeButton) {
        closeButton.addEventListener('click', function() {
            toggleChat(false);
        });
    }
    
    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    }
    
    if (userInput) {
        userInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
    
    // Cerrar chat al hacer clic fuera
    document.addEventListener('click', function(e) {
        if (isChatOpen && 
            !chatContainer.contains(e.target) && 
            e.target.id !== 'open-chat' &&
            !e.target.closest('#chat-container')) {
            toggleChat(false);
        }
    });
    
    // Prevenir que clics dentro del chat cierren el contenedor
    if (chatContainer) {
        chatContainer.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
    
    // Inicializar estilos
    function initializeChat() {
        // Asegurar que el chat esté oculto al inicio
        if (chatContainer) {
            chatContainer.style.display = 'none';
        }
        if (chatButton) {
            chatButton.style.display = 'block';
        }
        if (typingIndicator) {
            typingIndicator.style.display = 'none';
        }
        
        console.log('Chat initialized successfully');
    }
    
    // Inicializar cuando el DOM esté listo
    initializeChat();
});