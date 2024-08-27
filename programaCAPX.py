import streamlit as st

# Función para validar si todas las respuestas fueron contestadas
def validar_respuestas(respuestas):
    for respuesta in respuestas.values():
        if not respuesta:
            return False
    return True

# Creación del formulario
st.title("Formulario para Agencia de Marketing")

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

# Botón de registro
if st.button("Registrar"):
    if validar_respuestas(respuestas):
        # Llama a la función para enviar los datos a Google Docs
        st.write("Formulario enviado correctamente.")
    else:
        st.warning("Por favor, contesta todas las preguntas.")

