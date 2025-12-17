import os
import requests # Usamos requests estándar, no la SDK de Google
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: No leí la API KEY del archivo .env")
    exit()

print(f"🔑 Probando llave: {api_key[:5]}... (oculta)")

# 1. Petición directa a la API de Google (REST API)
# Esto pregunta directamente a los servidores de Google qué modelos tienes permitidos
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    response = requests.get(url)
    datos = response.json()
    
    if response.status_code == 200:
        print("\n✅ ¡ÉXITO! Tu API Key funciona y Google nos respondió.")
        print("Modelos disponibles para ti:")
        if 'models' in datos:
            for m in datos['models']:
                # Imprimimos el nombre exacto que necesita el código
                print(f" -> {m['name'].replace('models/', '')}")
        else:
            print("⚠️ La llave funciona pero la lista de modelos vino vacía.")
    else:
        print("\n❌ FALLO CRÍTICO: Tu API Key fue rechazada por Google.")
        print(f"Código de error: {response.status_code}")
        print(f"Mensaje: {datos}")

except Exception as e:
    print(f"Error de conexión: {e}")