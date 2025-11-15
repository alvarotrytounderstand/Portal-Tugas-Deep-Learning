import streamlit as st

st.set_page_config(page_title="Portal Tugas Deep Learning", layout="wide")

st.markdown("""
    <style>
    .link-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 40px;
    }
    .link-button {
        display: block;
        width: 80%;
        max-width: 500px;
        padding: 20px;
        background-color: #1E88E5;
        color: white;
        text-align: center;
        text-decoration: none;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        transition: background-color 0.3s;
    }
    .link-button:hover {
        background-color: #0D47A1;
        color: white;
    }
    .link-button.tugas-4 { /* Warna berbeda untuk tugas 4 */
        background-color: #28a745; /* Hijau */
    }
    .link-button.tugas-4:hover {
        background-color: #1a5c2a; /* Hijau tua */
    }
    h1, h3 {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Judul Utama ---
st.markdown("<h1>Web Tugas Deep Learning</h1>", unsafe_allow_html=True)
st.markdown("<h3>Oleh: [Nama Anda Di Sini]</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- URL DARI ANDA (LENGKAP) ---
URL_TUGAS_1 = "http://faalvaro.pythonanywhere.com/"
URL_TUGAS_2 = "https://tugas-generate-text.streamlit.app/"
URL_TUGAS_3 = "https://tugas-prediksi-saham.streamlit.app/"
URL_TUGAS_4 = "https://tugas-cnn-mnist.streamlit.app/" # <-- LINK BARU ANDA

st.markdown(f"""
    <div class="link-container">
        <a href="{URL_TUGAS_1}" target="_blank" class="link-button">
            Tugas 1: Logic Calculator
        </a>
        <a href="{URL_TUGAS_2}" target="_blank" class="link-button">
            Tugas 2: Generate Text
        </a>
        <a href="{URL_TUGAS_3}" target="_blank" class="link-button">
            Tugas 3: Prediksi Saham
        </a>
        <a href="{URL_TUGAS_4}" target="_blank" class="link-button tugas-4">
            Tugas 4: Klasifikasi Angka (CNN)
        </a>
    </div>
    """, unsafe_allow_html=True)
