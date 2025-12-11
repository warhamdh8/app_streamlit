import streamlit as st
import math

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write('[ini halaman untuk menghitung luas persegi]:ballon::ballon:')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9ltS7MZ5Kdy8xK8r7QKr9JVqRvhFrsPhjPQ&s', caption='gambar persegi')
    def luasPersegi(a):
        return a*a
    sisi = st.number_input('silahkan masukan sisi', min_value=0,)

    if st.button('hitung'):
        luas = luasPersegi(sisi)
        st.write(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga') 
    st.image('https://awsimages.detik.net.id/community/media/visual/2023/01/30/contoh-soal-segitiga-sama-kaki-2_169.png?w=620', caption='gambar segitiga')
    alas = st.number_input('masukan alas segitiga',min_value=0)
    tinggi = st.number_input('masukan tinggi segitiga',min_value=0)

    if st.button('hitung'):
        luas = 0,5 * alas * tinggi
        st.success (f'luas segitiga adalah {luas}')
else :
        st.write ('ini halaman untuk menghitung luas lingkaran')
        st.image('https://i.pinimg.com/736x/a6/af/60/a6af60f7c5c00908b44dfd4939e74d72.jpg', caption='gambar lingkaran')
        r = st.number_input('masukan jari-jari lingkaran',min_value=0)

        if st.button ('hitung_lingkaran') :
             luas_lingkaran = math.pi * (r**2)
             st.success (f'luas lingkaran adalah {luas_lingkaran}')