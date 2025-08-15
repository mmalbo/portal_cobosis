# chatbot/utils.py
import spacy
from enlac_preg.models import FAQ
nlp = spacy.load("es_core_news_md")
from django.db import connection

def encontrar_respuesta(pregunta_usuario):
    connection.close()

    preguntas_faq = FAQ.objects.all()
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
    
    return mejor_coincidencia.respuesta.text if mejor_coincidencia and mejor_puntaje > 0.6 else "Lo siento, no tengo información sobre eso. ¿Deseas contactar con un agente?"

