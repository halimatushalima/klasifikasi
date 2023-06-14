import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('kampus.sav', 'rb'))

st.title('Prediksi Siswa Melanjutkan Ke Perkuliahan')
c1, c2 = st.columns(2)

with c1:
    type_school = st.number_input('Tipe Sekolah (0: SMA, 1: SMK)')
    gender = st.number_input('Jenis Kelamin (0: Perempuan, 1: Laki-laki)')
    residence = st.number_input('Jenis tempat tinggal')
    parent_salary = st.number_input('Gaji orangtua/bln (IDR)')
    average_grades = st.number_input('Nilai rata-rata')

with c2:
    school_accreditation = st.number_input('Akreditasi Sekolah (0: A, 1: B)')
    interest = st.number_input('Tertarik melanjutkan kuliah')
    parent_age = st.number_input('Usia orangtua')
    house_area = st.number_input('Luas rumah')
    parent_was_in_college = st.number_input('Orangtua pernah kuliah')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[type_school, school_accreditation, gender, interest, residence, parent_age,
                               parent_salary, house_area, average_grades, parent_was_in_college]])

    if (prediksi [0] == 0):
        prediksi = ('Siswa tersebut tidak melanjutkan ke perkuliahan')
    else:
        prediksi = ('Siswa tersebut melanjutkan ke perkuliahan')
st.success(prediksi)