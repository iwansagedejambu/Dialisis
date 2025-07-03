```python
import streamlit as st

def hitung_ktv(qb, durasi_jam, bb_kering):
    clearance = 0.7 * qb  # mL/menit
    waktu_menit = durasi_jam * 60
    v = 0.55 * bb_kering * 1000  # Total cairan tubuh dalam mL
    ktv = (clearance * waktu_menit) / v
    return round(ktv, 2)

st.set_page_config(page_title="Kalkulator Kt/V HD", layout="centered")

st.title("🔢 Kalkulator Sederhana Kt/V untuk Hemodialisis")
st.markdown("""
Apa itu Kt/V?  
Kt/V menunjukkan seberapa efektif racun dalam darah dibersihkan selama cuci darah (HD).  
Nilai Kt/V ≥ 1.7 dianggap cukup baik untuk hasil yang optimal.  
""")

qb = st.number_input("💉 Laju Aliran Darah (Qb) - mL/menit", min_value=100, max_value=500, value=220)
durasi_jam = st.number_input("⏱ Durasi Dialisis (jam)", min_value=1.0, max_value=6.0, value=4.0)
bb_kering = st.number_input("⚖ Berat Badan Kering (kg)", min_value=20.0, max_value=120.0, value=48.5)

if st.button("Hitung Kt/V"):
    ktv = hitung_ktv(qb, durasi_jam, bb_kering)
        st.success(f"Perkiraan Kt/V Anda: {ktv}")
    if ktv >= 1.7:
        st.info("✅ Target Kt/V tercapai. Proses dialisis sudah efektif.")
    else:
        st.warning("⚠ Kt/V masih di bawah target. Pertimbangkan tambah waktu atau Qb (jika aman).")
