# chatbot/utils.py
import spacy
from enlac_preg.models import FAQ
from django.db import connection
from spacy.matcher import Matcher
from spacy.tokens import Span
import random
from datetime import datetime, timedelta
try:
    nlp = spacy.load("es_core_news_md")
except:
    # Fallback si no está instalado
    nlp = None
    
# Base de conocimientos para Cobosis
knowledge_base = {
    "saludos": [
        "¡Hola! Soy el asistente virtual de Cobosis. ¿En qué puedo ayudarte hoy?",
        "¡Hola! Bienvenido a Cobosis. ¿Cómo puedo asistirte?",
        "Hola, ¿en qué puedo ayudarte hoy?"
    ],
    "despedidas": [
        "¡Fue un placer ayudarte! Que tengas un buen día.",
        "¡Hasta luego! No dudes en contactarnos si necesitas más ayuda.",
        "Gracias por contactarnos. ¡Que tengas un excelente día!"
    ],
    "empresa": [
        "Cobosis es una empresa familiar especializada en transformación digital para pequeñas empresas en Cuba.",
        "Somos una empresa de desarrollo de software enfocada en la digitalización de negocios con presencia en Cuba."
    ],
    "servicios": [
        "Ofrecemos: desarrollo de tiendas virtuales, sistemas de gestión personalizados, análisis de datos, portales web y más.",
        "Nuestros servicios incluyen: desarrollo de software a medida, e-commerce, análisis inteligente de datos y soluciones de transformación digital."
    ],
    "tienda_virtual": [
        "Nuestra tienda virtual incluye: catálogo de productos, carrito de compras, pasarela de pagos, gestión de inventario y análisis de ventas.",
        "Desarrollamos tiendas online completas con gestión de inventario, facturación electrónica y dashboards de análisis."
    ],
    "precios": [
        "Nuestros precios varían según el proyecto. ¿Podrías decirme qué tipo de solución necesitas?",
        "Tenemos diferentes modelos de precios según el servicio. ¿Te interesa algún servicio en particular?"
    ],
    "contacto": [
        "Puedes contactarnos al email: ycoca@cobosis.com o por teléfono: +53 5 823 6469",
        "Nuestros contactos: email ycoca@cobosis.com, teléfono +53 5 823 6469"
    ],
    "default": [
        "Lo siento, no entendí completamente tu pregunta. ¿Podrías reformularla?",
        "No estoy seguro de entender. ¿Podrías explicarlo de otra manera?",
        "Mi conocimiento es limitado en ese tema. ¿Tienes otra pregunta?"
    ]
}

# Sinónimos clave para mejorar el reconocimiento
sinonimos = {
    "hola": ["hola", "buenos días", "buenas tardes", "buenas noches", "saludos"],
    "adiós": ["adiós", "hasta luego", "chao", "nos vemos", "hasta pronto"],
    "empresa": ["empresa", "negocio", "compañía", "organización", "firma", "Mipyme", "TCP"],
    "servicios": ["servicios", "soluciones", "ofertas", "productos", "qué hacen"],
    "tienda": ["tienda", "ecommerce", "comercio electrónico", "tienda online", "tienda virtual"],
    "precio": ["precio", "costo", "tarifa", "valor", "cuánto cuesta"],
    "contacto": ["contacto", "comunicar", "hablar", "llamar", "escribir", "email"]
}

# Configurar el matcher de spaCy
matcher = Matcher(nlp.vocab)

# Patrones para reconocimiento de intenciones
patrones = [
    # Saludos
    ["saludos", [[{"LOWER": {"IN": sinonimos["hola"]}}]]],
    
    # Despedidas
    ["despedidas", [[{"LOWER": {"IN": sinonimos["adiós"]}}]]],
    
    # Preguntas sobre la empresa
    ["empresa", [[{"LOWER": "qué"}, {"LOWER": "es"}, {"LOWER": "cobosis"}]]],
    ["empresa", [[{"LOWER": "hablenme"}, {"LOWER": "de"}, {"LOWER": "cobosis"}]]],
    
    # Preguntas sobre servicios
    ["servicios", [[{"LOWER": "qué"}, {"LOWER": "servicios"}]]],
    ["servicios", [[{"LOWER": "qué"}, {"LOWER": "ofrecen"}]]],
    
    # Preguntas sobre tienda virtual
    ["tienda_virtual", [[{"LOWER": "tienda"}, {"LOWER": "virtual"}]]],
    ["tienda_virtual", [[{"LOWER": "ecommerce"}]]],
    
    # Preguntas sobre precios
    ["precios", [[{"LOWER": "precio"}]]],
    ["precios", [[{"LOWER": "cuánto"}, {"LOWER": "cuesta"}]]],
    
    # Preguntas sobre contacto
    ["contacto", [[{"LOWER": "contacto"}]]],
    ["contacto", [[{"LOWER": "teléfono"}]]],
    ["contacto", [[{"LOWER": "email"}]]],
]

# Añadir patrones al matcher
for patron_id, patron in patrones:
    matcher.add(patron_id, patron)

# Función para reconocer intención
def reconocer_intencion(texto):
    doc = nlp(texto.lower())
    coincidencias = matcher(doc)
    
    if coincidencias:
        # Devolver la intención con mayor puntuación
        mayor_puntaje = 0
        intencion_principal = None
        
        for coincidencia_id, inicio, fin in coincidencias:
            puntaje = fin - inicio  # Longitud del patrón coincidente
            print(puntaje)
            if puntaje > mayor_puntaje:
                mayor_puntaje = puntaje
                intencion_principal = nlp.vocab.strings[coincidencia_id]
        
        return intencion_principal
    
    # Si no hay coincidencias, usar similitud semántica
    return reconocer_intencion_por_similitud(doc)

# Función alternativa por similitud semántica
def reconocer_intencion_por_similitud(doc):
    # Frases de referencia para cada intención
    print("Intención por similitud")
    frases_referencia = {
        "EMPRESA": nlp("¿Qué es Cobosis?"),
        "SERVICIOS": nlp("¿Qué servicios ofrecen?"),
        "TIENDA_VIRTUAL": nlp("tienda virtual ecommerce"),
        "PRECIOS": nlp("precios costos tarifas"),
        "CONTACTO": nlp("contacto teléfono email")
    }
    
    mejor_similitud = 0
    intencion_detectada = "default"
    
    for intencion, frase_ref in frases_referencia.items():
        similitud = doc.similarity(frase_ref)
        print(similitud)
        if similitud > mejor_similitud and similitud > 0.6:  # Umbral de similitud
            mejor_similitud = similitud
            intencion_detectada = intencion
    
    return intencion_detectada.lower()

# Función para extraer entidades
def extraer_entidades(texto):
    doc = nlp(texto)
    entidades = {}
    
    # Extraer entidades nombradas (NER de spaCy)
    for ent in doc.ents:
        entidades[ent.label_] = ent.text
    
    # Buscar sinónimos clave
    for tipo, palabras in sinonimos.items():
        for token in doc:
            if token.text.lower() in palabras:
                entidades[tipo.upper()] = token.text
    print(entidades)    
    return entidades

# Función principal del chatbot
#def chatbot_cobosis():

def encontrar_respuesta(pregunta_usuario):
    connection.close()
    if pregunta_usuario.lower() in ['salir', 'exit', 'quit']:
        respuesta = "¡Hasta luego! Fue un placer ayudarte."
        return respuesta
        
    # Procesar la entrada del usuario
    intencion = reconocer_intencion(pregunta_usuario)
    print(intencion)
    entidades = extraer_entidades(pregunta_usuario)
    print(entidades)
        
    # Manejar contexto conversacional
    """     if contexto_anterior == "SERVICIOS" and "tienda" in pregunta_usuario.lower():
        intencion = "TIENDA_VIRTUAL" """
        
    # Generar respuesta
    if intencion in knowledge_base:
        print("intencion en base de conocimiento")
        respuesta = random.choice(knowledge_base[intencion])
    else:
        respuesta = random.choice(knowledge_base["default"])
        
    # Respuestas contextuales
    """ if intencion == "PRECIOS" and "tienda" in entidades:
        respuesta = "El precio de una tienda virtual básica comienza en $500 USD. ¿Te gustaría agendar una cita?"
        contexto_anterior = intencion """
    
    return respuesta        
    

        
    """ preguntas_faq = FAQ.objects.all()
    mejor_coincidencia = None
    mejor_puntaje = 0

    doc_usuario = nlp(pregunta_usuario.lower())
    print(pregunta_usuario)
    
    for faq in preguntas_faq:
        doc_faq = nlp(faq.pregunta.text.lower())
        puntaje = doc_usuario.similarity(doc_faq)
        print(faq.pregunta.text.lower())
        print(puntaje)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_coincidencia = faq
    
    return mejor_coincidencia.respuesta.text if mejor_coincidencia and mejor_puntaje > 0.6 else "Lo siento, no tengo información sobre eso. ¿Deseas contactar con un agente?" """

