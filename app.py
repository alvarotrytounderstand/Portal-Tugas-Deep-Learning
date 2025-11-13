# -----------------------------------------------------------------
# NAMA FILE: app.py
# (Portal Utama Tugas Deep Learning - Versi Elegan Tanpa Background Biru)
# -----------------------------------------------------------------
import streamlit as st

st.set_page_config(page_title="Portal Tugas Deep Learning", layout="wide")

# --- CSS untuk tampilan elegan ---
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        font-family: 'Segoe UI', sans-serif;
    }

    .main {
        text-align: center;
        margin-top: 60px;
        color: white;
    }

    h1 {
        font-size: 3em;
        font-weight: 700;
        margin-bottom: 5px;
    }

    h3 {
        font-size: 1.3em;
        color: #b0bec5;
        margin-bottom: 40px;
    }

    .link-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        margin-top: 20px;
    }

    .link-button {
        display: block;
        width: 80%;
        max-width: 500px;
        padding: 20px;
        color: #e3f2fd;
        text-align: center;
        text-decoration: none;
        font-size: 22px;
        font-weight: 600;
        border: 2px solid #42A5F5;
        border-radius: 15px;
        background-color: transparent;
        transition: all 0.3s ease;
        box-shadow: 0px 0px 10px rgba(66,165,245,0.2);
    }

    .link-button:hover {
        color: #ffffff;
        border-color: #90CAF9;
        background-color: rgba(66,165,245,0.1);
        transform: scale(1.04);
        box-shadow: 0px 0px 25px rgba(66,165,245,0.4);
        text-shadow: 0px 0px 8px #BBDEFB;
    }

    footer {
        margin-top: 60px;
        text-align: center;
        color: #78909c;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Judul ---
st.markdown("""
    <div class="main">
        <h1>🧠 Portal Tugas Deep Learning</h1>
        <h3>Oleh: <b>Farhan Ahmad Alvaro</b></h3>
        <hr style="width: 40%; margin: auto; border: 1px solid #42A5F5;">
    </div>
""", unsafe_allow_html=True)

# --- URL Tugas ---
URL_TUGAS_1 = "http://faalvaro.pythonanywhere.com/"
URL_TUGAS_2 = "https://tugas-generate-text.streamlit.app/"
URL_TUGAS_3 = "https://tugas-prediksi-saham.streamlit.app/"

# --- Tombol Navigasi ---
st.markdown(f"""
    <div class="link-container">
        <a href="{URL_TUGAS_1}" target="_blank" class="link-button">
            🧮 Tugas 1: Logic Calculator
        </a>
        <a href="{URL_TUGAS_2}" target="_blank" class="link-button">
            ✍️ Tugas 2: Generate Text
        </a>
        <a href="{URL_TUGAS_3}" target="_blank" class="link-button">
            📈 Tugas 3: Prediksi Saham
        </a>
    </div>

    <footer>
        © 2025 | Farhan Ahmad Alvaro — Universitas Anda
    </footer>
""", unsafe_allow_html=True)
