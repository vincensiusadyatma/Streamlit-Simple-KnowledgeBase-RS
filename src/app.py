import streamlit as st
import pandas as pd
from data import phoneData  
from data import laptopData  
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

# Menampilkan aturan perhitungan similarity score
st.markdown("### Aturan Similarity Score")
st.write("""
1. **Budget**: 1 poin jika perbedaan kurang dari atau sama dengan 50 USD, 0 jika tidak.
2. **Screen Size**: 1 poin jika perbedaan kurang dari atau sama dengan 0.5 inch, 0 jika tidak.
3. **Battery Capacity**: 1 poin jika perbedaan kurang dari atau sama dengan 500 mAh, 0 jika tidak.
4. **Preferred Brand**: 1 poin jika sesuai dengan preferensi pengguna, 0 jika tidak.
""")


# Fungsi untuk menghitung similarity score pada case based
def hitung_similarity_score(input_data: pd.DataFrame, phoneData: pd.DataFrame) -> dict:
    scores = {}
    
    for row in range(len(phoneData)):
        score = 0
        
        # Budget similarity
        if abs(input_data.iloc[0]["Budget $"] - phoneData.iloc[row]["Budget $"]) <= 50:
            score += 1
        
        # Screen Size similarity
        if abs(input_data.iloc[0]["Screen Size (inch)"] - phoneData.iloc[row]["Screen Size (inch)"]) <= 0.5:
            score += 1
        
        # Battery Capacity similarity
        if abs(input_data.iloc[0]["Battery Capacity (mAh)"] - phoneData.iloc[row]["Battery Capacity (mAh)"]) <= 500:
            score += 1
        
        # Preferred Brand similarity
        if input_data.iloc[0]["Preferred Brand"] == phoneData.iloc[row]["Preferred Brand"]:
            score += 1
        
       
        scores["Case " + str(row+1)] = score  
    
    return scores



# Menambahkan tombol streamlit
if st.button("Dapatkan Rekomendasi"):
    st.success("Berikut adalah rekomendasi ponsel berdasarkan preferensi Anda:")
    st.dataframe(hitung_similarity_score(user_df, phoneData), use_container_width=True)
    


st.subheader("Constraint Based")



# Menampilkan DataFrame dari phoneData
st.markdown("### Data Ponsel yang Tersedia")
st.dataframe(laptopData, use_container_width=True)




# Fungsi untuk menghitung similarity score pada constraint based
def hitung_similarity_score_contraint(laptopdata: pd.DataFrame) -> dict:
    scores = {}
    
    for row in range(len(laptopData)):
        score = 0
        
        # Budget similarity
        if abs(laptopData.iloc[row]["Budget $"]) <= 700:
            score += 1
        
        # Screen Size similarity
        if abs(laptopData.iloc[row]["Ram"]) >= 8:
            score += 1
        
        # Battery Capacity similarity
        if abs(laptopData.iloc[row]["Storage"]) >= 256:
            score += 1
        
        # Preferred Brand similarity
        if  laptopData.iloc[row]["Battery Life"] >= 8:
            score += 1
        
       
        scores["Laptop" + str(row+1)] = score  
    
    return scores

def find_best_similarity(RecommendationDict : dict) ->dict :
    best_value = max(RecommendationDict.values())

    best_list = {}

    for item in RecommendationDict:
        if(RecommendationDict[item] == best_value):
            best_list[item] = RecommendationDict[item]
    
    return best_list

# Menampilkan aturan perhitungan similarity score
st.markdown("### Aturan Similarity Score")
st.write("""
1. **Budget**: 1 poin jika perbedaan kurang dari atau sama dengan 50 USD, 0 jika tidak.
2. **Screen Size**: 1 poin jika perbedaan kurang dari atau sama dengan 0.5 inch, 0 jika tidak.
3. **Battery Capacity**: 1 poin jika perbedaan kurang dari atau sama dengan 500 mAh, 0 jika tidak.
4. **Preferred Brand**: 1 poin jika sesuai dengan preferensi pengguna, 0 jika tidak.
""")

# Menambahkan tombol untuk rekomendasi
if st.button("Dapatkan Rekomendasi2"):
    st.success("Berikut adalah rekomendasi ponsel berdasarkan preferensi Anda:")
    st.dataframe(find_best_similarity(hitung_similarity_score_contraint(laptopData)), use_container_width=True)
    
# footer
st.markdown("---")


