import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os
import matplotlib.pyplot as plt
import hashlib
import time

# =========================
# AUTO REFRESH (1 MENIT)
# =========================
st_autorefresh(interval=60000, key="refresh")

st.set_page_config(page_title="Dashboard APAR", layout="wide")

def convert_sheet_url(url):

    sheet_id = url.split("/d/")[1].split("/")[0]

    return (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv"
    )

# =========================================
# LOGIN CHECK
# =========================================
if "login" not in st.session_state:
    st.session_state.login = False


# =========================================
# JIKA BELUM LOGIN
# =========================================
if not st.session_state.login:

    # =========================================
    # CSS
    # =========================================
    st.markdown("""
    <style>

    /* HIDE STREAMLIT LOAD */
    [data-testid="stDecoration"]{
        display:none;
    }

    [data-testid="stToolbar"]{
        display:none;
    }

    /* SMOOTH RENDER */
    html, body, [class*="css"]{
        font-family:'Inter',sans-serif;
    }

    /* HILANGKAN FLASH PUTIH */
    .stApp{
        background:#FFFFFF;
    }

    /* TRANSISI HALUS */
    section.main{
        transition:all .15s ease-in-out;
    }

    /* HIDE IMAGE FLASH */
    .stImage img{
        opacity:1;
        transition:opacity .2s ease;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    .stApp{
        background:#FFFFFF;
    }

    #MainMenu,
    header,
    footer{
        visibility:hidden;
    }

    .block-container{
        padding-top:0.3rem;
        max-width:430px;
        margin:auto;
    }

    .login-title{
        text-align:center;
        font-size:27px;
        font-weight:800;
        color:#1E3A8A;
        margin-top:2px;
        margin-bottom:6px;
        line-height:1.2;
    }

    .login-desc{
        text-align:center;
        font-size:12px;
        color:#64748B;
        line-height:1.6;
        margin-bottom:20px;
    }

    label{
        font-size:13px !important;
        font-weight:500 !important;
        color:#334155 !important;
        margin-bottom:8px !important;
    }

    .stTextInput{
        margin-bottom:16px !important;
    }

    .stTextInput > div > div > input{
        height:48px !important;
        border-radius:14px !important;
        border:1px solid #E2E8F0 !important;
        background:#F8FAFC !important;
        padding-left:14px !important;
        font-size:14px !important;
    }

    .stButton > button{
        width:100%;
        height:46px;
        border:none;
        border-radius:14px;
        background:#2563EB;
        color:white;
        font-size:15px;
        font-weight:700;
        margin-top:6px;
    }

    .stButton > button:hover{
        background:#1D4ED8;
    }

    .footer{
        position:fixed;
        bottom:12px;
        left:0;
        right:0;
        text-align:center;
        color:#94A3B8;
        font-size:11px;
    }

    /* LOGIN CONTAINER */
    .block-container{
        padding-top:2rem !important;
        max-width:430px;
        margin:auto;
    }

    /* HILANGKAN SPACE ATAS */
    [data-testid="stVerticalBlock"]{
        gap:0rem !important;
    }

    /* LOGO */
    .login-logo{
        margin-top:-40px;
        margin-bottom:-20px;
    }

    </style>
    """, unsafe_allow_html=True)


    # =========================================
    # LOGO
    # =========================================
    c1,c2,c3 = st.columns([0.5,3,0.5])

    with c2:

        st.image(
            "images.png",
            width=1000
        )


    # =========================================
    # TITLE
    # =========================================
    st.markdown("""
    <div class="login-title">
    Dashboard Maintenance APAR
    </div>

    <div class="login-desc">
    Website Maintenance <br>
    Alat Pemadam Api Ringan secara real-time.
    </div>
    """, unsafe_allow_html=True)


    # =========================================
    # PASSWORD
    # =========================================
    USERNAME = st.secrets["USERNAME"]
    PASSWORD = st.secrets["PASSWORD"]

    # =========================================
    # HASH FUNCTION
    # =========================================
    def hash_password(password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()


    # =========================================
    # INPUT
    # =========================================
    username = st.text_input(
        "👤 Username",
        placeholder="Masukkan username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Masukkan password"
    )


    # =========================================
    # LOGIN BUTTON
    # =========================================
    if st.button("Login"):

        if (
            username == USERNAME and
            hash_password(password) == PASSWORD
        ):

            st.session_state.login = True
            with st.spinner("Membuka dashboard..."):

                st.session_state.login = True

                time.sleep(0.3)

                st.rerun()
        else:

            st.error(
                "Username atau password salah"
            )


    # =========================================
    # FOOTER
    # =========================================
    st.markdown("""
    <div class="footer">
    © 2026 Dashboard Maintenance Alat Pemadam Api Ringan
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# =========================================
# SHEET VERIFICATION
# =========================================
if "sheet_verified" not in st.session_state:
    st.session_state.sheet_verified = False

if st.session_state.login and not st.session_state.sheet_verified:

    # =========================================
    # CSS
    # =========================================
    st.markdown("""
    <style>

    .stApp{
        background:#FFFFFF;
    }

    #MainMenu,
    header,
    footer{
        visibility:hidden;
    }

    .block-container{
        padding-top:0.3rem;
        max-width:430px;
        margin:auto;
    }

    .login-title{
        text-align:center;
        font-size:27px;
        font-weight:800;
        color:#1E3A8A;
        margin-top:2px;
        margin-bottom:6px;
        line-height:1.2;
    }

    .login-desc{
        text-align:center;
        font-size:12px;
        color:#64748B;
        line-height:1.6;
        margin-bottom:10px;
    }

    label{
        font-size:13px !important;
        font-weight:600 !important;
        color:#334155 !important;
    }

    .stTextInput > div > div > input{
        height:46px;
        border-radius:14px;
        border:1px solid #E2E8F0;
        background:#F8FAFC;
        padding-left:14px;
        font-size:14px;
    }

    .stButton > button{
        width:100%;
        height:46px;
        border:none;
        border-radius:14px;
        background:#2563EB;
        color:white;
        font-size:15px;
        font-weight:700;
        margin-top:6px;
    }

    .stButton > button:hover{
        background:#1D4ED8;
    }

    .footer{
        position:fixed;
        bottom:12px;
        left:0;
        right:0;
        text-align:center;
        color:#94A3B8;
        font-size:11px;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================================
    # LOGO
    # =========================================
    c1,c2,c3 = st.columns([0.5,3,0.5])

    with c2:
        st.image(
            "images.png",
            width=1000
        )

    # =========================================
    # TITLE
    # =========================================
    st.markdown("""
    <div class="login-title">
    Verifikasi Dashboard Maintenance APAR
    </div>

    <div class="login-desc">
    Website Maintenance <br>
    Alat Pemadam Api Ringan secara real-time.
    </div>
    """, unsafe_allow_html=True)

    # =========================================
    # INPUT
    # =========================================
    sheet_url = st.text_input(
        "Link Spreadsheet",
        placeholder="Masukkan link spreadsheet"
    )

    # =========================================
    # BUTTON
    # =========================================
    if st.button("Verifikasi"):

        try:

            csv_url = convert_sheet_url(sheet_url)

            df_test = pd.read_csv(csv_url)

            # =========================================
            # VALIDASI DATA
            # =========================================
            required_cols = ["AREA", "Lokasi"]

            missing_cols = [
                col for col in required_cols
                if col not in df_test.columns
            ]

            if missing_cols:

                st.error(
                    "Format spreadsheet tidak sesuai format."
                )

            else:

                st.session_state.SHEET_URL = csv_url

                st.session_state.sheet_verified = True

                st.rerun()

        except Exception as e:

            st.error(
                "Link spreadsheet tidak valid atau tidak dapat diakses."
            )

            st.exception(e)
            
    # =========================================
    # FOOTER
    # =========================================
    st.markdown("""
    <div class="footer">
    © 2026 Dashboard Maintenance Alat Pemadam Api Ringan
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# =========================
# CSS
# =========================
st.markdown("""
<style>
            
/* mentokin isi sidebar */
[data-testid="stSidebarContent"]{
    padding-top:0rem !important;
    margin-top:-35px !important;
}

/* hilangin jarak container sidebar */
section[data-testid="stSidebar"] > div{
    padding-top:0rem !important;
}

/* hapus padding atas sidebar */
[data-testid="stSidebarContent"]{
    padding-top:0rem;
}

/* GLOBAL */
.block-container{
    padding-top:1rem;
}

/* TITLE */
.main-title{
    font-size:25px;
    font-weight:800;
    color:#0F172A;
    line-height:1.1;
    margin-bottom:6px;
}

.main-subtitle{
    font-size:13px;
    color:#64748B;
    font-weight:500;
}

/* DATE TIME */
.datetime-box{
    background:white;
    padding:10px 14px;
    border-radius:14px;
    border:1px solid #E5E7EB;
    text-align:center;
    width:140px;
    margin-left:auto;
    box-shadow:0 3px 10px rgba(0,0,0,0.04);
}

.datetime-date{
    font-size:13px;
    color:#64748B;
    font-weight:500;
    margin-bottom:3px;
}

.datetime-time{
    font-size:24px;
    font-weight:800;
    color:#111827;
    line-height:1;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
col1, col2 = st.columns([3,1])

# TITLE
with col1:

    st.markdown("""
    <div class="main-title">
        Dashboard APAR PT Garudafood Putra Putri Jaya Tbk
    </div>

    <div class="main-subtitle">
        Monitoring data Alat Pemadam Api Ringan secara realtime PT Garudafood Putra Putri Jaya, Tbk BU Gresik
    </div>
    """, unsafe_allow_html=True)

# DATE TIME
with col2:

    now = datetime.now()

    tanggal = now.strftime("%d %b %Y")
    jam = now.strftime("%H:%M")

    html = f"""
    <div class="datetime-box">
        <div class="datetime-date">{tanggal}</div>
        <div class="datetime-time">{jam}</div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)

st.write("")

# =========================
# FUNCTION REMINDER
# =========================
def apar_reminder(df):

    if "EXP" not in df.columns:
        return df

    df["EXP_DATE"] = pd.to_datetime(
        df["EXP"],
        errors="coerce"
    )

    today = datetime.now()

    df["SISA_HARI"] = (
        df["EXP_DATE"] - today
    ).dt.days

    WARNING_HARI = 60

    def status_apar(hari):

        if pd.isna(hari):
            return "TIDAK ADA DATA"

        elif hari < 0:
            return "EXPIRED"

        elif hari <= WARNING_HARI:
            return "WARNING"

        else:
            return "AMAN"

    df["STATUS"] = df["SISA_HARI"].apply(status_apar)

    expired = (df["STATUS"] == "EXPIRED").sum()
    warning = (df["STATUS"] == "WARNING").sum()

    # 🚨 EXPIRED
    if expired > 0:

        st.markdown(f"""
        <div style="
        background-color:#f8d7da;
        padding:15px;
        border-radius:10px;
        margin-bottom:10px;
        ">
        <b style="color:#842029;">
        🚨 {expired} APAR SUDAH EXPIRED!
        </b>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Lihat Data EXPIRED", key="exp_btn"):

            st.session_state.show_expired = True
            st.session_state.show_warning = False

    # ⚠️ WARNING
    if warning > 0:

        st.markdown(f"""
        <div style="
        background-color:#fff3cd;
        padding:15px;
        border-radius:10px;
        margin-bottom:10px;
        ">
        <b style="color:#664d03;">
        ⚠️ {warning} APAR AKAN EXPIRED (< 2 bulan)
        </b>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Lihat Data WARNING", key="warn_btn"):

            st.session_state.show_warning = True
            st.session_state.show_expired = False

    return df
# =========================
# WARNA STATUS
# =========================
def warna_status(val):
    if val == "EXPIRED":
        return "background-color:red; color:white;"
    elif val == "WARNING":
        return "background-color:orange;"
    elif val == "AMAN":
        return "background-color:green; color:white;"
    return ""

# =========================
# INIT SESSION STATE
# =========================
if "show_expired" not in st.session_state:
    st.session_state.show_expired = False

if "show_warning" not in st.session_state:
    st.session_state.show_warning = False

# =========================
# GOOGLE SHEETS SOURCE
# =========================

sheet_url = st.session_state["SHEET_URL"]

df = pd.DataFrame()

try:

    df = pd.read_csv(sheet_url)

    # 🔥 bersihin kolom kayak sebelumnya
    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]

    df.columns = [
        f"TANGGAL_{i}" if pd.isna(col) or str(col).strip() == ""
        else str(col).strip()
        for i, col in enumerate(df.columns)
    ]

except Exception as e:
    st.error("❌ Gagal ambil data dari Google Sheets")
    st.exception(e)
    df = pd.DataFrame()

# =========================
# 📊 DASHBOARD APAR (FINAL - FIX UI)
# =========================
if not df.empty:

    # 🔥 CLEAN DULU
    df.columns = [col.upper() for col in df.columns]
    df = df.loc[:, ~df.columns.duplicated()]
    df = df.apply(lambda x: x.astype(str).str.strip())

    # 🔥 CLEAN KAPASITAS SUPER AMAN
    if "KAPASITAS" in df.columns:
        df["KAPASITAS"] = (
            df["KAPASITAS"]
            .astype(str)
            .str.extract(r'(\d+)', expand=False)  # ambil angka saja
        )

    if "NO APAR" in df.columns:
        df["NO APAR"] = df["NO APAR"].str.replace(r"\.0$", "", regex=True)

    # =========================
    # DATA DASHBOARD
    # =========================
    total_apar = len(df)

    jenis_count = df["JENIS"].value_counts() if "JENIS" in df.columns else pd.Series()
    kapasitas_count = df["KAPASITAS"].value_counts() if "KAPASITAS" in df.columns else pd.Series()
    # =========================
    # LAYOUT
    # =========================
    left, right = st.columns([1,2])

    # =========================
    # 🧯 KIRI (TOTAL APAR)
    # =========================
    with left:
        st.markdown(
            f"""
            <div style='text-align:center; padding:30px;'>
                <div style='font-size:90px;'>🧯</div>
                <div style='font-size:16px; font-weight:bold;'>Total APAR</div>
                <div style='font-size:42px; color:#d9534f;'>{total_apar}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # 📊 KANAN (GRAFIK - DI ATAS ALERT)
    # =========================
    with right:

        col1, col2 = st.columns(2)

        # 🥧 PIE CHART WARNA TERANG
        with col1:
            if not jenis_count.empty:
                st.markdown("""
                <div style="
                    font-size:16px;
                    font-weight:700;
                    color:#111827;
                    margin-bottom:8px;
                    text-align:center;
                ">
                    Distribusi Jenis
                </div>
                """, unsafe_allow_html=True)

                fig1, ax1 = plt.subplots(figsize=(25,25))

                # 🎨 warna terang (pastel/bright)
                colors = [
                    '#FF9999',  # merah muda
                    '#66B2FF',  # biru terang
                    '#99FF99',  # hijau muda
                    '#FFCC99',  # oranye pastel
                    '#C2C2F0',  # ungu muda
                    '#FFD700',  # kuning emas terang
                    '#FFB6C1'   # pink light
                ]

                ax1.pie(
                    jenis_count,
                    labels=jenis_count.index,
                    autopct='%1.1f%%',
                    colors=colors,
                    textprops={'fontsize': '50'},
                    labeldistance=1.1,
                    pctdistance=0.8,
                    startangle=90
                )

                st.pyplot(fig1, use_container_width=True)

        # 📊 BAR CHART (MERAH + ADA ANGKA)
        with col2:

            if not kapasitas_count.empty:

                st.markdown("""
                <div style="
                    font-size:16px;
                    font-weight:700;
                    color:#111827;
                    margin-bottom:8px;
                    text-align:center;
                ">
                    Distribusi Kapasitas
                </div>
                """, unsafe_allow_html=True)

                fig2, ax2 = plt.subplots(figsize=(5,5))

                labels = [
                    f"{int(x)} kg"
                    for x in kapasitas_count.index
                    if pd.notna(x)
                ]

                bars = ax2.bar(
                    labels,
                    kapasitas_count.values,
                    color="#99CCFF"
                )

                # angka di atas bar
                for bar in bars:

                    yval = bar.get_height()

                    ax2.text(
                        bar.get_x() + bar.get_width()/2,
                        yval,
                        int(yval),
                        ha='center',
                        va='bottom'
                    )

                plt.xticks(rotation=20)

                st.pyplot(fig2, use_container_width=True)
                
    # =========================
    # 🔥 BARU SETELAH GRAFIK → REMINDER
    # =========================
    df = apar_reminder(df)
    
# =========================
# SIDEBAR LOGO
# =========================

st.sidebar.image(
    "images2.png",
    use_container_width=True
)

st.sidebar.markdown("""
<div style="
font-size:16px;
font-weight:500;
color:#111827;
margin-top:-5px;
margin-bottom:4px;
">
Filter Dashboard
</div>

<hr style="
border:0.5px solid #E5E7EB;
margin-top:0;
margin-bottom:15px;
">
""", unsafe_allow_html=True)

is_empty = df.empty

def get_filter(col):
    if not is_empty and col in df.columns:
        values = sorted(df[col].dropna().unique())

        # 🔥 khusus kapasitas → kasih "kg"
        if col == "KAPASITAS":
            display = [f"{v} kg" for v in values]

            selected_display = st.sidebar.multiselect(col, display)

            # 🔥 balikin lagi ke angka asli
            selected = [
                v.replace(" kg", "")
                for v in selected_display
            ]
            return selected

        return st.sidebar.multiselect(col, values)

    return st.sidebar.multiselect(col, [], disabled=True)
    
status_filter = st.sidebar.multiselect(
    "STATUS", [] if is_empty else ["AMAN", "WARNING", "EXPIRED"], disabled=is_empty
)

area = get_filter("AREA")
lokasi = get_filter("LOKASI")
kode = get_filter("KODE APAR")
jenis = get_filter("JENIS")
kapasitas = get_filter("KAPASITAS")
aktif = get_filter("MASIH AKTIF")
exp = get_filter("EXP")

# =========================
# FILTER LOGIC
# =========================
df_filter = df.copy()

if not df.empty:
    if status_filter:
        df_filter = df_filter[df_filter["STATUS"].isin(status_filter)]
    if area:
        df_filter = df_filter[df_filter["AREA"].isin(area)]
    if lokasi:
        df_filter = df_filter[df_filter["LOKASI"].isin(lokasi)]
    if kode:
        df_filter = df_filter[df_filter["KODE APAR"].isin(kode)]
    if jenis:
        df_filter = df_filter[df_filter["JENIS"].isin(jenis)]
    if kapasitas:
        df_filter = df_filter[df_filter["KAPASITAS"].isin(kapasitas)]
    if aktif:
        df_filter = df_filter[df_filter["MASIH AKTIF"].isin(aktif)]
    if exp:
        df_filter = df_filter[df_filter["EXP"].isin(exp)]

# =========================
# OUTPUT
# =========================
if df.empty:
    st.info("Silakan upload file Excel terlebih dahulu")

else:

    # ======================
    # 🚨 TAMPILKAN EXPIRED
    # ======================
    if st.session_state.show_expired:
        df_expired = df[df["STATUS"] == "EXPIRED"]
        st.subheader("🚨 DATA APAR EXPIRED")
        st.dataframe(df_expired, use_container_width=True)

    # ======================
    # ⚠️ TAMPILKAN WARNING
    # ======================
    if st.session_state.show_warning:
        df_warning = df[df["STATUS"] == "WARNING"]
        st.subheader("⚠️ DATA APAR WARNING (< 2 BULAN)")
        st.dataframe(df_warning, use_container_width=True)

    # ======================
    # 📋 DATA UTAMA
    # ======================
    st.markdown("""
    <div style="
        font-size:23px;
        font-weight:800;
        color:#111827;
        margin-bottom:4px;
    ">
        Data APAR
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        color:#6B7280;
        font-size:15px;
        margin-bottom:14px;
    ">
        Total data: <b>{len(df_filter)}</b>
    </div>
    """, unsafe_allow_html=True)

if "STATUS" in df_filter.columns:

    styled_df = df_filter.style.map(
        warna_status,
        subset=["STATUS"]
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )
else:

    st.dataframe(
        df_filter,
        use_container_width=True
    )