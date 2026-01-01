import streamlit as st
import math

# =========================
# Konfigurasi halaman
# =========================
st.set_page_config(
    page_title="Kalkulator Kt/V Hemodialisis (Daugirdas II)",
    layout="centered"
)

# =========================
# Fungsi Kt/V Daugirdas II (AMAN)
# =========================
def hitung_ktv_daugirdas2(
    bun_pre,       # mg/dL
    bun_post,      # mg/dL
    durasi_jam,    # jam
    uf_liter,      # liter
    bb_post        # kg
):
    # Validasi dasar
    if bun_pre <= 0 or bun_post <= 0 or bb_post <= 0:
        return None, "Input tidak valid."

    R = bun_post / bun_pre
    t = durasi_jam
    UF = uf_liter
    W = bb_post

    nilai_log = R - 0.008 * t

    # Validasi matematis WAJIB
    if nilai_log <= 0:
        return None, (
            "Perhitungan tidak valid:\n"
            "R − 0.008 × t ≤ 0.\n\n"
            "Periksa kembali nilai BUN dan durasi dialisis."
        )

    ktv = -math.log(nilai_log) + (4 - 3.5 * R) * (UF / W)
    return round(ktv, 2), None


# =========================
# Judul & deskripsi
# =========================
st.title("💉 Kalkulator Kt/V Hemodialisis (Daugirdas II)")
st.markdown("""
Kt/V digunakan untuk menilai **kecukupan hemodialisis (HD)**.  
Aplikasi ini menggunakan **rumus Daugirdas II**, yang merupakan **standar klinis internasional**.

🎯 **Target Kt/V ≥ 1.7**
""")

# =========================
# Input pengguna
# =========================
st.header("📥 Masukkan Parameter Dialisis")

col1, col2 = st.columns(2)

with col1:
    bun_pre = st.number_input(
        "🧪 BUN Pre Dialisis (mg/dL)",
        min_value=10.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )

    bun_post = st.number_input(
        "🧪 BUN Post Dialisis (mg/dL)",
        min_value=2.0,
        max_value=100.0,
        value=15.0,
        step=1.0
    )

    durasi_jam = st.number_input(
        "⏱️ Durasi Dialisis (jam)",
        min_value=1.0,
        max_value=6.0,
        value=4.0,
        step=0.25
    )

with col2:
    uf_liter = st.number_input(
        "💧 Ultrafiltrasi (liter)",
        min_value=0.0,
        max_value=5.0,
        value=2.5,
        step=0.1
    )

    bb_post = st.number_input(
        "⚖️ Berat Badan Post Dialisis (kg)",
        min_value=20.0,
        max_value=150.0,
        value=60.0,
        step=0.5
    )

# =========================
# Tombol hitung
# =========================
if st.button("🔍 Hitung Kt/V"):
    ktv, error_msg = hitung_ktv_daugirdas2(
        bun_pre=bun_pre,
        bun_post=bun_post,
        durasi_jam=durasi_jam,
        uf_liter=uf_liter,
        bb_post=bb_post
    )

    if error_msg:
        st.error(error_msg)
        st.stop()

    st.subheader(f"Hasil Kt/V Anda: **{ktv}**")

    if ktv >= 1.7:
        st.success("✅ Kt/V tercapai. Dialisis adekuat.")
    elif 1.4 <= ktv < 1.7:
        st.warning("⚠ Kt/V borderline. Perlu evaluasi durasi, UF, atau akses vaskular.")
    else:
        st.error("❌ Kt/V tidak adekuat. Risiko underdialysis.")

# =========================
# Penjelasan rumus
# =========================
with st.expander("📌 Penjelasan Rumus Daugirdas II"):
    st.markdown("""
**Rumus Daugirdas II (single-pool Kt/V):**

> **Kt/V = −ln(R − 0.008 × t) + (4 − 3.5 × R) × (UF / W)**

**Keterangan:**
- **R** = BUN post / BUN pre  
- **t** = durasi dialisis (jam)  
- **UF** = ultrafiltrasi (liter)  
- **W** = berat badan post dialisis (kg)

📌 Rumus ini:
- Memperhitungkan **urea rebound**
- Memasukkan efek **ultrafiltrasi**
- Digunakan luas dalam praktik klinis HD
""")

st.caption(
    "🧠 Alat bantu edukasi. Tidak menggantikan evaluasi medis oleh dokter atau unit hemodialisis."
)
