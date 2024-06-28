# Chatbot Interactivo

Este proyecto es un chatbot interactivo que utiliza la API de Groq para generar respuestas basadas en el contexto de la conversación. El bot puede realizar varias funciones como limpiar la consola, borrar el contexto, y proporcionar ayuda sobre los comandos disponibles.

## Requisitos

- Python 3.7 o superior
- Biblioteca `python-dotenv`
- API Key de Groq

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   #Crear entorno
   python -m venv venv

   #Activar en Linux
   source venv/bin/activate 

   #Activar en Windows
   venv\Scripts\activate
3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
4. Crea un archivo .env en la raíz del proyecto y agrega tu API Key de Groq:
    ```bash
    GROQ_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
5. Ejecutar el script `bot.py` para iniciar el chatbot.
    ```bash
    python bot.py
    
## Comandos Disponible
- !salir: Terminar la conversación
- !limpiar: Limpiar la consola
- !borrar: Borrar el contexto de la conversación
- !ayuda: Mostrar la lista de comandos disponibles

## Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.