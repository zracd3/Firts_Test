import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargar variables de entorno
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("¡No se encontró la API Key! Revisa tu archivo .env")

# 2. Configurar la librería
genai.configure(api_key=api_key)

# 3. Listar modelos disponibles (para verificar conexión)
# Esto ayuda a ver qué versiones tienen acceso (gemini-1.5-flash, gemini-1.5-pro, etc.)
print("Modelos disponibles:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")

# 4. Instanciar el modelo (Usaremos Flash para pruebas rápidas)
model = genai.GenerativeModel('gemini-2.5-flash')

# 5. Generación básica (Hola Mundo)
response = model.generate_content("Explica en una sola frase qué es Python para un niño de 10 años.")

print("\n--- Respuesta de Gemini ---")
print(response.text)

# Texto largo de prueba (simulando un artículo o log)
texto_usuario = "La inteligencia artificial generativa está transformando el desarrollo de software..." * 50

# 1. Contar tokens (Esto NO genera texto, solo calcula)
# Es vital para validar si nos pasamos del límite antes de gastar saldo o tiempo.
conteo = model.count_tokens(texto_usuario)

print(f"Longitud en caracteres: {len(texto_usuario)}")
print(f"Total de Tokens: {conteo.total_tokens}")
print("*"*30)
# Demostración de costo (simbólico) vs caracteres
ratio = len(texto_usuario) / conteo.total_tokens
print(f"Promedio de caracteres por token: {ratio:.2f}")

# Nota: Si intentas enviar más tokens de los que el modelo soporta, la API dará error.

def calcular(lista):
    total = 0
    # Ineficiente y mal nombrado
    for i in range(len(lista)):
        total = total + lista[i]
    return total

