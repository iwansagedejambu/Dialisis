import streamlit as st

# Fungsi untuk menghitung Kt/V
def hitung_ktv(qb, durasi_jam, bb_kering):
    clearance = 0.7 * qb  # mL/menit
    waktu_menit = durasi_jam * 60
    v = 0.55 * bb_kering * 1000  # Volume distribusi dalam mL
    ktv = (clearance * waktu_menit) / v
    return round(ktv, 2)

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Kalkulator Kt/V Hemodialisis", layout="centered")

# Judul dan deskripsi
st.title("💉 Kalkulator Kt/V Sederhana untuk Hemodialisis")
st.markdown("""
Kt/V adalah parameter yang digunakan untuk menilai **efektivitas proses hemodialisis (HD)**.  
Semakin tinggi nilainya, semakin banyak racun dalam darah yang berhasil disaring.  
**Target Kt/V ≥ 1.7** menandakan dialisis yang memadai.
""")

# Input pengguna
st.header("📥 Masukkan Parameter Dialisis Anda")
col1, col2 = st.columns(2)
with col1:
    qb = st.number_input("🔄 Laju Aliran Darah (Qb) - mL/menit", min_value=100, max_value=500, value=220)
    bb_kering = st.number_input("⚖️ Berat Badan Kering (kg)", min_value=20.0, max_value=150.0, value=48.5)
with col2:
    durasi_jam = st.number_input("⏱️ Durasi Dialisis (jam)", min_value=1.0, max_value=6.0, value=4.0)

# Tombol untuk menghitung
if st.button("🔍 Hitung Kt/V Sekarang"):
    ktv = hitung_ktv(qb, durasi_jam, bb_kering)
    st.subheader(f"Hasil Perhitungan Kt/V Anda: **{ktv}**")
    
    # Interpretasi hasil
    if ktv >= 1.7:
        st.success("✅ Kt/V tercapai. Proses dialisis sudah cukup efektif.")
    elif 1.4 <= ktv < 1.7:
        st.warning("⚠ Kt/V mendekati target, namun masih perlu dievaluasi lebih lanjut.")
    else:
        st.error("❌ Kt/V di bawah target. Pertimbangkan menambah waktu dialisis atau Qb jika memungkinkan.")

# Catatan perhitungan
with st.expander("📌 Penjelasan dan Rumus yang Digunakan"):
    st.markdown("""
    **Rumus Perhitungan Sederhana Kt/V:**

    \n> Kt/V = (Clearance × Waktu) / Volume Distribusi
    
    **Dengan asumsi:**
    - Clearance = 0.7 × Qb (mL/menit)
    - Waktu = Durasi dialisis (jam) × 60 (menit)
    - Volume distribusi = 0.55 × Berat Badan Kering (kg) × 1000 (mL)

    **Keterangan:**
    - Nilai Kt/V ≥ 1.7 menunjukkan proses dialisis cukup optimal.
    - Nilai < 1.7 bisa berarti waktu atau aliran darah kurang — konsultasikan ke dokter.
    - Perhitungan ini adalah pendekatan kasar, **tidak menggantikan evaluasi medis** dari lab dan dokter.
    """)

st.caption("🧠 Kalkulator ini hanya alat bantu. Konsultasikan hasilnya dengan tim medis Anda.")
