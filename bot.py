import os
from groq import Groq
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

##################################################################
################ COMENTAR EL METODO NO UTILIZADO #################

# Variables de entorno:
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# Variables dentro de .env
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

##################################################################

# Array para mantener el contexto de la conversación
mensajes = []

def mostrar_ayuda():
    print("""
Comandos disponibles:
- !salir: Terminar la conversación
- !limpiar: Limpiar la consola
- !borrar: Borrar el contexto de la conversación
- !ayuda: Mostrar esta ayuda
""")

# Mostrar ayuda al inicio
mostrar_ayuda()

nombre_usuario = input("Por favor, dime tu nombre: ")
print(f"Hola, {nombre_usuario}! ¿Cómo puedo ayudarte?")

while True:
    pregunta = input(f"{nombre_usuario}: ")

    
    if pregunta.lower() == '!salir':
        break
    elif pregunta.lower() == '!limpiar':
        os.system("clear")
        continue
    elif pregunta.lower() == '!borrar':
        mensajes = []
        print("El contexto ha sido borrado.")
        continue
    elif pregunta.lower() == '!ayuda':
        mostrar_ayuda()
        continue
    
    # Agregar la pregunta al contexto
    mensajes.append({"role": "user", "content": pregunta})
    
    # Generar la respuesta
    chat_completion = client.chat.completions.create(
        messages=mensajes,
        model="llama3-70b-8192",
    )
    
    # Obtener el contenido de la respuesta
    respuesta = chat_completion.choices[0].message.content
    print(f"IA: {respuesta}")
    
    # Agregar la respuesta al contexto
    mensajes.append({"role": "assistant", "content": respuesta})
