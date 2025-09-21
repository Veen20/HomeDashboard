

import streamlit as st

# ==============================
# Konfigurasi Layout
# ==============================
st.set_page_config(
    page_title="Portal Multi-Dashboard 🚀",
    layout="wide",
    page_icon="📊"
)

# ==============================
# Inject Font Awesome + CSS
# ==============================
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
/* Background dengan overlay */
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
    color: #222 !important;
}
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] span, 
[data-testid="stSidebar"] li {
    color: #222 !important;
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

/* Logo pojok kanan atas */
.top-right-logos {
    position: absolute;
    top: 15px;
    right: 25px;
    display: flex;
    gap: 15px;
}
.top-right-logos img {
    height: 55px;  /* ubah ukuran logo di sini */
    object-fit: contain;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# State navigasi
# ==============================
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# ==============================
# Sidebar
# ==============================
st.sidebar.markdown("<h2><i class='fas fa-folder-open'></i> Menu</h2>", unsafe_allow_html=True)
if st.sidebar.button("🏠 Halaman Utama"):
    st.session_state["page"] = "home"
if st.sidebar.button("ℹ️ Tentang"):
    st.session_state["page"] = "about"

# ==============================
# Header Logo di pojok kanan atas
# ==============================
st.markdown("""
<div class="top-right-logos">
    <img src="logo unsri.png">
    <img src="logo samsat.png">
    <img src="logo fasilkom.png">
    st.image("logo fasilkom.png", width=100)

    
</div>
col1, col2, col3 = st.columns(3)

with col1:
    st.image("logo unsri.png", width=80)
with col2:
    st.image("logo samsat.png", width=80)
with col3:
    st.image("logo fasilkom.png", width=80)

""", unsafe_allow_html=True)

# ==============================
# Halaman Utama
# ==============================
if st.session_state["page"] == "home":
    col1, col2 = st.columns([1, 8])
    with col1:
        st.image("logo unsri.png", width=100)
    with col2:
        st.markdown("""
            <div class="title-box">
                <h1>Portal Analisis Sentimen Samsat UPTB Palembang 1</h1>
                <p><b>Pilih salah satu dashboard di bawah untuk melihat hasil analisis secara lebih detail.</b></p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    dashboards = {
        "<i class='fas fa-map-marked-alt'></i> Analisis Sentimen Ulasan Gmaps": {
            "url": "https://dashboard1.streamlit.app",
            "tooltip": "Lihat pendapat masyarakat tentang layanan Samsat"
        },
        "<i class='fab fa-google-play'></i> Ulasan Play Store": {
            "url": "https://e4ca85lwpgeyxjmxjjab7f.streamlit.app/",
            "tooltip": "Tampilan data ulasan aplikasi di Play Store"
        },
        "<i class='fab fa-youtube'></i> Ulasan YouTube": {
            "url": "https://dashboard3.streamlit.app",
            "tooltip": "Analisis komentar & sentimen di YouTube"
        },
        "<i class='fas fa-chart-pie'></i> Gabungan": {
            "url": "https://dashboard4.streamlit.app",
            "tooltip": "Kombinasi analisis semua platform"
        }
    }

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

    st.markdown(
        "<div class='footer'> Semua dashboard berjalan mandiri. Klik tombol untuk membuka di tab baru.</div>",
        unsafe_allow_html=True
    )

# ==============================
# Halaman Tentang
# ==============================
elif st.session_state["page"] == "about":
    st.markdown("""
        <div class="title-box">
            <h1>ℹ️ Tentang Aplikasi</h1>
            <p>Informasi mengenai aplikasi ini, tim pengembang, dan instansi terkait.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("### 📌 Identitas Aplikasi")
    st.write("- **Nama**: Portal Analisis Sentimen Samsat UPTB Palembang 1")
    st.write("- **Versi**: 1.0")
    st.write("- **Dibuat oleh**: Tim Pengembang Fasilkom Unsri")

    st.write("### 🏢 Identitas Instansi")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("logo unsri.png", caption="Universitas Sriwijaya", use_container_width=True)
    with col2:
        st.image("logo samsat.png", caption="Samsat UPTB Palembang 1", use_container_width=True)
    with col3:
        st.image("logo fasilkom.png", caption="Fasilkom Unsri", use_container_width=True)

    st.write("### 👨‍💻 Tim Pengembang")
    st.write("- Nama 1")
    st.write("- Nama 2")
    st.write("- Nama 3")
