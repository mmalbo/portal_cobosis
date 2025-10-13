# chatbot/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods
import json
from .utils import encontrar_respuesta
from datetime import datetime, timezone

@require_http_methods(["POST"])
@csrf_exempt
def chatbot_api(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('message', '').strip()
        chat_history = data.get('history', [])
        
        if not user_message:
            return JsonResponse({
                'status': 'error',
                'message': 'Mensaje vacío'
            }, status=400)
        
        # Obtener respuesta del chatbot (puedes pasar el historial si lo necesitas)
        bot_response = encontrar_respuesta(user_message)
        return JsonResponse({
            'status': 'success',
            'message': bot_response,
            'timestamp': datetime.now().isoformat()
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Formato JSON inválido'
        }, status=400)
        
    except Exception as e:
        # Log del error para debugging
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error en chatbot API: {str(e)}")
        
        return JsonResponse({
            'status': 'error',
            'message': 'Error interno del servidor'
        }, status=500)