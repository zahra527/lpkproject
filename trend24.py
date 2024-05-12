#import module
import streamlit as st
import numpy as np
import pandas as pd

#tampilan konten aplikasi
tab1,tab2,tab3=st.tabs(['HALAMAN UTAMA','RUMUS','TABEL VISKOSI'])

with tab1:
    st.header('Aplikasi Penetapan Kekentalan Metode Laju Alir Oswald/Engler', divider='rainbow')
    st.markdown('''Hallo Guys''')
    st.markdown('''Selamat Anda Adalah Orang Beruntung Yang Membuka Web Aplikasi Ini''')
    st.markdown(''':blue[ARE YOU READY?? LETS GOO]''')

with tab2:
    st.image('rumus.png')
    densitas_sampel= st.number_input('masukkan densitas sampel g/mL')
    X̅laju_alir_sampel = st.number_input ('masukkan X̅laju alir sampel s')
    densitas_air = st.number_input ('masukkan densitas air g/mL')
    X̅laju_alir_air = st.number_input('masukkan X̅laju alir air s')
    viskositas_aquadest = st.number_input('masukkan viskositas aquadest')
viskositas = 0

if X̅laju_alir_air != 0 and densitas_air != 0:
    viskositas = (densitas_sampel * X̅laju_alir_sampel) / (densitas_air * X̅laju_alir_air) * viskositas_aquadest
    st.text(f"Nilai Viskositas sampel adalah : ({densitas_sampel} * {X̅laju_alir_sampel}) / ({densitas_air} * {X̅laju_alir_air}) * {viskositas_aquadest} = {viskositas}")

with tab3:
    st.header('TABEL VISKOSITAS KINEMATIK')
    st.image('tabel viskositas.jpg')


