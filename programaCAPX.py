import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Función para validar si todas las respuestas fueron contestadas
def validar_respuestas(respuestas):
    for respuesta in respuestas.values():
        if not respuesta:
            return False
    return True

# Creación del formulario
st.title("Formulario para CAPX")

# Preguntas del formulario
respuestas = {
    'Nombre de la empresa': st.text_input("Nombre de la empresa"),
    'Giro de la empresa': st.text_input("Giro de la empresa"),
    'Nuestro contacto': st.text_input("Nuestro contacto"),
    'Puesto del contacto': st.text_input("Puesto del contacto"),
    'Descripción de la empresa': st.text_area("Descripción de la empresa"),
    '¿Cómo Monetizan?': st.text_area("¿Cómo Monetizan?"),
    'Costo de su producto o servicio': st.text_input("Costo de su producto o servicio"),
    '¿Manejan el marketing Inhouse o con Agencia?': st.text_input("¿Manejan el marketing Inhouse o con Agencia?"),
    '¿Qué servicios les manejan?': st.text_area("¿Qué servicios les manejan?"),
    '¿Cómo es su embudo de venta?': st.text_area("¿Cómo es su embudo de venta?"),
    '¿Qué tan efectivo es su embudo de venta?': st.slider("¿Qué tan efectivo es su embudo de venta?", 1, 5),
    '¿Cuáles son sus metas?': st.text_area("¿Cuáles son sus metas?"),
    '¿Cuentan con presencia digital?': st.multiselect(
        "¿Cuentan con presencia digital?",
        ["Facebook", "Instagram", "Página Web", "Google", "LinkedIn", "TikTok", "Otro", "No"]
    ),
    '¿Servicios que buscan?': st.multiselect(
        "¿Servicios que buscan?",
        ["Creación de Contenido", "Manejo de Redes Sociales", "Campañas Publicitarias", "Mail Marketing", 
         "Investigación de Mercado", "Plan de Mercadotecnia", "Auditoría", "Página Web", "Otro"]
    ),
    'Facturación Anual o Mensual': st.text_input("Facturación Anual o Mensual"),
    'Presupuesto en Marketing': st.text_input("Presupuesto en Marketing"),
    'Softwares a utilizar': st.multiselect(
        "Softwares a utilizar",
        ["Software 1", "Software 2", "Otro"]
    ),
}

# Base de datos de servicios
servicios_db = {
    "Creación de Contenido": 1000,
    "Manejo de Redes Sociales": 1500,
    "Campañas Publicitarias": 2000,
    "Mail Marketing": 800,
    "Investigación de Mercado": 1200,
    "Plan de Mercadotecnia": 1800,
    "Auditoría": 500,
    "Página Web": 3000,
}

# Calcular el costo total basado en la selección
def calcular_cotizacion(servicios_seleccionados):
    total = 0
    for servicio in servicios_seleccionados:
        if servicio in servicios_db:
            total += servicios_db[servicio]
    return total

# Autenticación y creación del servicio de Google Docs
def crear_servicio_docs():
    credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/documents'])
    service = build('docs', 'v1', credentials=credentials)
    return service

# Función para crear el documento en Google Docs
def enviar_a_google_docs(respuestas):
    service = crear_servicio_docs()

    # Crear el documento en Google Docs
    document = {
        'title': respuestas['Nombre de la empresa']
    }
    doc = service.documents().create(body=document).execute()
    document_id = doc.get('documentId')

    # Inicializa 'contenido' aquí
    contenido = []  

    # Estructura del documento
    contenido.append({'insertText': {'location': {'index': 1}, 'text': respuestas['Nombre de la empresa'] + '\n\n'}})
    contenido.append({'insertText': {'location': {'index': 1}, 'text': f"{respuestas['Giro de la empresa']} | {respuestas['Nuestro contacto']} | {respuestas['Puesto del contacto']}\n\n"}})

    # Añadir preguntas y respuestas
    for pregunta, respuesta in respuestas.items():
        if pregunta not in ['Nombre de la empresa', 'Giro de la empresa', 'Nuestro contacto', 'Puesto del contacto']:
            contenido.append({'insertText': {'location': {'index': 1}, 'text': f"{pregunta}: {respuesta}\n\n"}})

    # Calcular cotización y agregar al documento
    if '¿Servicios que buscan?' in respuestas:
        servicios_seleccionados = respuestas['¿Servicios que buscan?']
        total_cotizacion = calcular_cotizacion(servicios_seleccionados)
        contenido.append({'insertText': {'location': {'index': 1}, 'text': f"Total cotización: ${total_cotizacion}\n\n"}})

    # Actualiza el documento
    service.documents().batchUpdate(documentId=document_id, body={'requests': contenido}).execute()

    return document_id

# Botón de registro
if st.button("Registrar"):
    if validar_respuestas(respuestas):
        doc_id = enviar_a_google_docs(respuestas)
        st.write("Formulario enviado correctamente. Documento creado en Google Docs.")
    else:
        st.warning("Por favor, contesta todas las preguntas.")

