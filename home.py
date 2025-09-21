import streamlit as st
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
/* Background gambar Samsat dengan overlay gelap */
.stApp {
    background: linear-gradient(rgba(10,10,30,0.75), rgba(10,10,30,0.85)),
                url("https://raw.githubusercontent.com/Veen20/HomeDashboard/main/OIP.webp");
    background-size: cover;
    background-attachment: fixed;
    background-position: center top;
}

/* Judul utama */
h1 {
    color: #FFD700;
    font-weight: bold;
    text-align: center;
    text-shadow: 3px 3px 8px rgba(0,0,0,0.7);
    font-size: 40px;
    margin-bottom: 10px;
}
p {
    text-align: center;
    font-size: 18px;
    color: #f1f1f1;
}

/* Tombol dashboard */
button {
    background: linear-gradient(135deg, #FFD700, #FFA500);
    color: #222;
    padding: 18px 30px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.3);
    transition: all 0.3s ease-in-out;
    width: 90%;
}
button:hover {
    background: linear-gradient(135deg, #FFA500, #FFD700);
    transform: translateY(-3px) scale(1.05);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(255, 249, 230, 0.95);
    border-right: 2px solid #FFD700;
}

/* Footer */
.footer {
    text-align:center;
    color:#ddd;
    font-size:14px;
    padding:12px;
    border-radius:8px;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# Logo kiri atas + judul
col1, col2 = st.columns([1, 8])
with col1:
    st.image("LOGO UNSRI.png", width=90)
with col2:
    st.markdown("<h1>🎉 Portal Multi-Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p>Klik tombol di bawah untuk membuka dashboard masing-masing tim</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.title("📂 Menu Dashboard")
st.sidebar.info("Gunakan menu ini untuk akses cepat ke tiap dashboard.")

# Dashboard + ikon + tooltip (hanya 4)
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
            <div style='text-align:center; margin:20px'>
                <a href='{info["url"]}' target='_blank' title='{info["tooltip"]}'>
                    <button>{name}</button>
                </a>
            </div>
            """, unsafe_allow_html=True
        )
    i += 1

st.markdown("<div class='footer'>🌟 Semua dashboard berjalan mandiri. Klik tombol untuk membuka di tab baru.</div>", unsafe_allow_html=True)
