import streamlit as st
import requests
import json

# Configuración de la URL de la API Flask
API_URL = "http://localhost:5000"

# Página principal de Streamlit
st.title("Gestión de Activos Empresariales")

# Crear un nuevo documento
st.header("Crear Documento")
with st.form(key='create_form'):
    nombre = st.text_input("Nombre")
    direccion = st.text_input("Dirección")
    telefono = st.text_input("Teléfono")
    submit_button = st.form_submit_button(label='Crear')
    if submit_button:
        payload = {
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono
        }
        response = requests.post(f"{API_URL}/create", json=payload)
        st.write(response.json())

# Leer todos los documentos
st.header("Leer Todos los Documentos")
if st.button('Leer Todos'):
    response = requests.get(f"{API_URL}/read")
    documents = response.json()
    st.write(documents)

# Leer documento por ID
st.header("Leer Documento por ID")
id_to_read = st.text_input("ID del Documento")
if st.button('Leer por ID'):
    response = requests.get(f"{API_URL}/read/{id_to_read}")
    document = response.json()
    st.write(document)

# Actualizar un documento
st.header("Actualizar Documento")
update_id = st.text_input("ID del Documento a Actualizar")
update_nombre = st.text_input("Nuevo Nombre")
update_direccion = st.text_input("Nueva Dirección")
update_telefono = st.text_input("Nuevo Teléfono")
if st.button('Actualizar'):
    payload = {
        "Nombre": update_nombre,
        "Dirección": update_direccion,
        "Teléfono": update_telefono
    }
    response = requests.put(f"{API_URL}/update/{update_id}", json=payload)
    st.write(response.json())

# Eliminar un documento
st.header("Eliminar Documento")
delete_id = st.text_input("ID del Documento a Eliminar")
if st.button('Eliminar'):
    response = requests.delete(f"{API_URL}/delete/{delete_id}")
    st.write(response.json())
