import streamlit as st
import pandas as pd
from data import phoneData  

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Simple Knowledge Based", layout="wide")

# Menambahkan header dan subheader
st.header("Simple Knowledge Based Recommendation System")
st.subheader("Case Based")



# Menampilkan DataFrame dari phoneData
st.markdown("### Data Ponsel yang Tersedia")
st.dataframe(phoneData, use_container_width=True)

# Input pengguna
st.markdown("Input Pengguna")
pengguna = {
    "Case": [1],
    "Budget $": [450],
    "Screen Size (inch)": [6.0],
    "Battery Capacity (mAh)": [4000],
    "Preferred Brand": ["Samsung"],
}

# Menampilkan DataFrame pengguna
user_df = pd.DataFrame(pengguna)
st.dataframe(user_df, use_container_width=True)

# Menambahkan tombol untuk rekomendasi
if st.button("Dapatkan Rekomendasi"):
    st.success("Berikut adalah rekomendasi ponsel berdasarkan preferensi Anda:")

    st.write("Samsung Galaxy A52") 

# Menambahkan footer atau informasi tambahan
st.markdown("---")
st.markdown("### Tentang Aplikasi")
st.write("Aplikasi ini membantu Anda menemukan ponsel terbaik berdasarkan preferensi Anda.")
