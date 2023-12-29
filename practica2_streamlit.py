# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:36:10 2023

@author: User
"""

import streamlit as st
import joblib
import numpy as np 
from PIL import Image
import sklearn

st.set_page_config(page_icon='🐕‍🦺',page_title='PET PLANET')

model_filename = 'arnes.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)
print("Hemos Cargado el modelo...")

st.title('PET PLANET')
image = Image.open('perrodenieve.jpg')
nuevo_tamano_img=(960,350)
image_redimensionada=image.resize(nuevo_tamano_img)
st.image(image_redimensionada, caption='La llamada de lo salvaje')
st.header("Los mejores accesorios para tu mascota.")
st.image('MarcaEMPRESA ML-JPG.jpg',width=100)
#se me ha ocurrido colocar un combo box para seleccionar un articulo
option = st.selectbox(
    'Selecciona un accesorio',
    ('Arnés','Correas','Cestas', 'Bebederos'))

#st.write('A seleccionado', option)
if option=='Arnés':
    arnes = st.text_input(label='Tamaño del arnés:',value=0)#value=0, es el valor por default
    bota = st.text_input(label='Tamaño de bota:',value=0)#value=0, es el valor por default

    try:
        arnes = int(arnes)
        bota=int(bota)
        if st.button("Ejecutar modelo"):
            inputs=[[arnes]]
            predicted_boot_size = loaded_model.predict(inputs)[0]
            predicted_model=round(predicted_boot_size)
            #st.write("El tamaño de bota sugerido es: ",round(predicted_boot_size))
            st.info(f'El tamaño de bota sugerido es: {predicted_model}',icon="ℹ️")
            if bota>predicted_model:
                st.warning('Warning: ¡La talla de bota elegida es probablemente muy grande!', icon="🚨") 
            elif bota==predicted_model:
                st.success('La talla de bota seleccionada es la más adecuada', icon="✅")
            elif bota<predicted_model:
                st.warning('Warning: ¡La talla de bota elegida es probablemente muy pequeña!', icon="🚨")           
    except ValueError: 
        st.error('Los campos solo permiten ingresar números', icon="🚨")        
else:
    st.info('No existe implemetación para esta opción', icon="ℹ️")

