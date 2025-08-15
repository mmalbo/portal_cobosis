document.addEventListener('DOMContentLoaded', function() {
    const chatButton = document.getElementById('open-chat');
    const chatContainer = document.getElementById('chat-container');
    const closeButton = document.getElementById('close-chat');
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-btn');
    
    let chatSocket;
    let isDragging = false;
    let offsetX, offsetY;
    
    // Función para mostrar un mensaje en el chat
    function appendMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(isUser ? 'message-user' : 'message-bot');
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
        
        // Scroll automático al último mensaje
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Función para conectar al WebSocket
    function connectWebSocket() {
        const wsScheme = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        const host = window.location.host;
        const path = '/ws/chatbot/';
        
        chatSocket = new WebSocket(wsScheme + host + path);
        
        chatSocket.onopen = function(e) {
            console.log('Conexión WebSocket establecida');
        };
        
        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            appendMessage(data.message, false);
        };
        
        chatSocket.onclose = function(e) {
            console.log('Conexión WebSocket cerrada');
            // Reconectar después de 5 segundos
            setTimeout(connectWebSocket, 5000);
        };
        
        chatSocket.onerror = function(e) {
            console.error('Error en WebSocket:', e);
        };
    }
    
    // Función para enviar mensaje
    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            // Mostrar mensaje del usuario
            appendMessage(message, true);
            
            // Enviar al servidor
            if (chatSocket && chatSocket.readyState === WebSocket.OPEN) {
                chatSocket.send(JSON.stringify({
                    'message': message
                }));
            } else {
                appendMessage("Error de conexión. Recargando...", false);
                setTimeout(connectWebSocket, 1000);
            }
            
            // Limpiar input
            userInput.value = '';
        }
    }
    
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'message-bot';
        typingDiv.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function hideTypingIndicator() {
        const typing = document.getElementById('typing-indicator');
        if (typing) typing.remove();
    }
    
    // Event Listeners
    chatButton.addEventListener('click', function() {
        chatContainer.style.display = 'block';
        chatButton.style.display = 'none';
        userInput.focus();
        connectWebSocket();
    });
    
    closeButton.addEventListener('click', function() {
        chatContainer.style.display = 'none';
        chatButton.style.display = 'block';
        
        // Cerrar conexión WebSocket
        if (chatSocket) {
            chatSocket.close();
        }
    });
    
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Funcionalidad para arrastrar el chat
    const chatHeader = document.querySelector('.chat-header');
    
    chatHeader.addEventListener('mousedown', function(e) {
        isDragging = true;
        offsetX = e.clientX - chatContainer.getBoundingClientRect().left;
        offsetY = e.clientY - chatContainer.getBoundingClientRect().top;
        chatContainer.style.cursor = 'grabbing';
    });
    
    document.addEventListener('mousemove', function(e) {
        if (isDragging) {
            const x = e.clientX - offsetX;
            const y = e.clientY - offsetY;
            
            // Mantener dentro de los límites de la ventana
            const maxX = window.innerWidth - chatContainer.offsetWidth;
            const maxY = window.innerHeight - chatContainer.offsetHeight;
            
            chatContainer.style.left = Math.max(0, Math.min(x, maxX)) + 'px';
            chatContainer.style.top = Math.max(0, Math.min(y, maxY)) + 'px';
        }
    });
    
    document.addEventListener('mouseup', function() {
        isDragging = false;
        chatContainer.style.cursor = 'default';
    });
    
    // Botón de limpiar chat
    const clearButton = document.createElement('button');
    clearButton.className = 'btn btn-sm btn-outline-secondary mt-2';
    clearButton.innerHTML = '<i class="bi bi-trash"></i> Limpiar chat';
    document.querySelector('.chat-input').appendChild(clearButton);
    
    clearButton.addEventListener('click', function() {
        chatMessages.innerHTML = '<div class="message-bot">Conversación reiniciada. ¿En qué puedo ayudarte?</div>';
    });

});