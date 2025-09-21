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

/* Container judul */
.title-box {
    background: rgba(0,0,0,0.6);
    padding: 20px 30px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 15px;
}

/* Judul utama */
.title-box h1 {
    color: #FFD700;
    font-weight: bold;
    text-shadow: 3px 3px 8px rgba(0,0,0,0.9);
    font-size: 42px;
    margin-bottom: 8px;
}

/* Subjudul */
.title-box p {
    font-size: 18px;
    color: #f1f1f1;
    margin: 0;
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
    font-size: 15px;
    line-height: 1.5;
}

/* Footer */
.footer {
    text-align:center;
    color:#eee;
    font-size:14px;
    padding:12px;
    border-radius:8px;
    margin-top:30px;
    background: rgba(0,0,0,0.5);
}
</style>
""", unsafe_allow_html=True)

# Logo + Judul
col1, col2 = st.columns([1, 8])
with col1:
    st.image("LOGO UNSRI.png", width=90)
with col2:
    st.markdown("""
        <div class="title-box">
            <h1>🎉 Portal Multi-Dashboard</h1>
            <p>Pilih salah satu dashboard di bawah ini untuk melihat data dan informasi dengan mudah</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.title("📂 Menu Dashboard")
st.sidebar.write("""
Portal ini berisi beberapa dashboard yang dibuat oleh tim.  
Gunakan menu atau tombol di halaman utama untuk membuka dashboard.  
Setiap dashboard akan terbuka di tab baru.
""")

# Dashboard + ikon + tooltip (hanya 4)
dashboards = {
    "🚗 Analisis Sentimen Ulasan Gmaps (PENI ILHAMI CUTE)": {
        "url": "http1",
        "tooltip": "Lihat pendapat masyarakat tentang layanan Samsat"
    },
    "📊 ulasan play store ": {
        "url": "https://dashboard2.streamlit.app",
        "tooltip": "Tampilan data dalam bentuk tabel dan grafik sederhana"
    },
    "📈 ulasan youtube": {
        "url": "https://dashboard3.streamlit.app",
        "tooltip": "Visualisasi tren pertumbuhan data"
    },
    "🛠️ Gabungan": {
        "url": "https://dashboard4.streamlit.app",
        "tooltip": "Pantau status dan kinerja sistem secara langsung"
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
