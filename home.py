import streamlit as st

# Atur layout dan title
st.set_page_config(
    page_title="Portal Multi-Dashboard 🚀",
    layout="wide",
    page_icon="📊"
)

# CSS kustom
st.markdown("""
<style>
/* Background gambar Samsat */
html, body, .stApp {
    background: url("https://github.com/Veen20/HomeDashboard/blob/main/OIP.webp?raw=true");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center top;
    color: #f8f9fa; /* teks default terang */
}

/* Overlay gelap tipis biar teks lebih kebaca */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45); /* transparansi hitam */
    z-index: -1;
}

/* Judul utama */
h1 {
    color: #ffd700; /* emas */
    font-weight: bold;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
}

/* Subjudul */
.subtitle {
    font-size: 18px;
    color: #ffffff;
    padding: 8px 15px;
    background: rgba(0,0,0,0.5);
    border-radius: 10px;
    display: inline-block;
}

/* Tombol dashboard */
button {
    background: linear-gradient(135deg, #ffcc00, #ff9900);
    color: black;
    padding: 15px 25px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
}
button:hover {
    background: linear-gradient(135deg, #ffdb4d, #ff6600);
    transform: scale(1.07);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.9);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

# Logo kiri atas + judul
col1, col2 = st.columns([1, 8])
with col1:
    st.image("LOGO UNSRI.png", width=80)  # ganti dengan logo tim/universitas kamu
with col2:
    st.markdown("""
        <h1 style='margin-top:15px;'>🎉 Portal Multi-Dashboard</h1>
        <p class='subtitle'>Klik tombol di bawah untuk membuka dashboard masing-masing tim</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.title("📂 Menu Dashboard")
st.sidebar.info("Pilih dashboard yang ingin dibuka dengan cepat lewat menu ini.")

# Dashboard + ikon + tooltip
dashboards = {
    "🚗 Dashboard 1 (Peni)": {
        "url": "https://dashboard-ndkjpx2acq4tqkxlrhbuao.streamlit.app/#dashboard-analisis-sentimen-ulasan-publik-samsat-uptb-palembang-1",
        "tooltip": "Analisis Sentimen Ulasan Publik Samsat"
    },
    "📊 Dashboard 2 (Teman 1)": {
        "url": "https://dashboard2.streamlit.app",
        "tooltip": "Dashboard Data Statistik"
    },
    "📈 Dashboard 3 (Teman 2)": {
        "url": "https://dashboard3.streamlit.app",
        "tooltip": "Visualisasi Pertumbuhan"
    },
    "🛠️ Dashboard 4 (Teman 3)": {
        "url": "https://dashboard4.streamlit.app",
        "tooltip": "Monitoring Sistem & Tools"
    }
}

# Tampilkan tombol dalam grid (2 kolom)
cols = st.columns(2)
i = 0
for name, info in dashboards.items():
    with cols[i % 2]:
        st.markdown(
            f"""
            <div style='text-align:center; margin:15px'>
                <a href='{info["url"]}' target='_blank' title='{info["tooltip"]}'>
                    <button>{name}</button>
                </a>
            </div>
            """, unsafe_allow_html=True
        )
    i += 1

st.markdown("---")
st.markdown("""
<div style='text-align:center; color:white; font-size:14px; background:rgba(0,0,0,0.6); padding:10px; border-radius:8px;'>
    🌟 Semua dashboard berjalan mandiri. Klik tombol untuk membuka di tab baru.
</div>
""", unsafe_allow_html=True)
