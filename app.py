# -----------------------------------------------------------------
# NAMA FILE: app.py
# (Portal Utama Tugas Deep Learning)
# -----------------------------------------------------------------
import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Portal Tugas Deep Learning", layout="wide")

# --- Gaya Kustom (CSS) ---
st.markdown("""
    <style>
    /* Background gradient */
    body {
        background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 50%, #BBDEFB 100%);
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Kontainer utama */
    .main {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 30px 50px;
        border-radius: 20px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        text-align: center;
        margin-top: 50px;
    }

    h1 {
        color: #ffffff;
        font-size: 3em;
        font-weight: 700;
        margin-bottom: 10px;
    }

    h3 {
        color: #E3F2FD;
        font-size: 1.4em;
        font-weight: 400;
        margin-bottom: 40px;
    }

    .link-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        margin-top: 30px;
    }

    .link-button {
        display: block;
        width: 80%;
        max-width: 500px;
        padding: 18px;
        background: linear-gradient(90deg, #1976D2, #42A5F5);
        color: white;
        text-align: center;
        text-decoration: none;
        font-size: 22px;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }

    .link-button:hover {
        background: linear-gradient(90deg, #0D47A1, #2196F3);
        transform: scale(1.05);
        box-shadow: 0px 6px 25px rgba(0, 0, 0, 0.3);
        text-shadow: 0px 0px 8px #BBDEFB;
    }

    footer {
        margin-top: 50px;
        font-size: 14px;
        color: #E3F2FD;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Judul Utama ---
st.markdown("""
    <div class="main">
        <h1>🌟 Portal Tugas Deep Learning 🌟</h1>
        <h3>Oleh: <b>Farhan Ahmad Alvaro</b></h3>
        <hr style="width: 50%; margin: auto; border: 1px solid #E3F2FD;">
    </div>
""", unsafe_allow_html=True)

# --- URL (Edit Sesuai Tugasmu) ---
URL_TUGAS_1 = "http://faalvaro.pythonanywhere.com/"
URL_TUGAS_2 = "https://tugas-generate-text.streamlit.app/"
URL_TUGAS_3 = "https://tugas-prediksi-saham.streamlit.app/"

# --- Tombol Navigasi Tugas ---
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
