import streamlit as st
import numpy as np

st.header('Aplikasi Penetapan Kekentalan Metode Laju Alir Oswald/Engler', divider='rainbow')

densitas_sampel = st.number_input('masukkan densitas sampel')
st.write('the first number is',densitas_sampel)

X̅laju_alir_sampel = st.number_input ('masukkan X̅laju alir sampel')
st.write('the second number is',X̅laju_alir_sampel)

densitas_air = st.number_input ('masukkan densitas air')
st.write('the second number is',densitas_air)

X̅laju_alir_air = st.number_input('masukkan X̅laju alir air')
st.write('the second number is',X̅laju_alir_air)

viskositas_aquadest = st.number_input('masukkan viskositas aquadest')
st.write('the second number is',viskositas_aquadest)

st.image('tabel viskositas.jpg')
tabel_viskositas_jpg= st.file_uploader('upload a tabel viskositas jpg', type='jpg')
if tabel_viskositas_jpg is not None:
   img_array=np.array('image') 

viskositas = 0

if X̅laju_alir_air != 0 and densitas_air != 0:
    viskositas = (densitas_sampel * X̅laju_alir_sampel) / (densitas_air * X̅laju_alir_air) * viskositas_aquadest
    st.text(f"Nilai Viskositas sampel adalah : ({densitas_sampel} * {X̅laju_alir_sampel} / {densitas_air} * {X̅laju_alir_air}) * {viskositas_aquadest} = {viskositas}")
