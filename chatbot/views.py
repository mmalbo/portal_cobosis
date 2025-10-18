# chatbot/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods
import json
#from .utils import encontrar_respuesta
from .chatbotAuth import encontrar_respuesta
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from registration.models import Profile


@method_decorator(csrf_exempt, name='dispatch')
class ChatbotAuthAPI(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            action = data.get('action', '')
            
            if action == 'login':
                username = data.get('username', '')
                password = data.get('password', '')
                
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Autenticación exitosa',
                        'user': {
                            'nombre': f"{user.first_name} {user.last_name}".strip() or user.username,
                            'email': user.email
                        }
                    })
                else:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Usuario o contraseña incorrectos'
                    }, status=401)
                    
            return JsonResponse({
                'status': 'error',
                'message': 'Acción no válida'
            }, status=400)
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Error interno del servidor'
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ChatbotPrivateAPI(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            print("En la llamada post")
            # Obtener información del cliente autenticado
            try:
                usuario = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Perfil de cliente no encontrado'
                }, status=404)
            
            # Procesar mensaje con acceso a datos privados
            respuesta = encontrar_respuesta(user_message, usuario=usuario)
            
            return JsonResponse({
                'status': 'success',
                'message': respuesta
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Error: {str(e)}'
            }, status=500)
        

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