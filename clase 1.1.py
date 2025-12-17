import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargar variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("¡Error! No se encontró la variable GOOGLE_API_KEY.")

# 2. Configurar SDK
genai.configure(api_key=api_key)

# 3. Selección del Modelo (CORREGIDO PARA TU CUENTA)
# En tu lista aparecía 'gemini-2.5-flash', así que usaremos ese.
# Es mucho más potente que el 1.5.
NOMBRE_MODELO = 'gemini-2.5-flash'

print(f"🔌 Conectando con la nueva generación: {NOMBRE_MODELO}...")

try:
    # Instanciar modelo
    model = genai.GenerativeModel(NOMBRE_MODELO)

    # 4. Prompt
    prompt = "Explica brevemente qué ramas existen de la IA, como ML o DL y cursos para estudiarlos."
    
    print(f"📤 Enviando prompt...")
    
    # 5. Generar
    response = model.generate_content(prompt)

    print("\n--- ✅ Respuesta de Gemini 2.5 ---")
    print(response.text)
    print("----------------------------------")

except Exception as e:
    print(f"\n❌ Error: {e}")