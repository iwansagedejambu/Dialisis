import streamlit as st

def calculate_ktv(qb, duration_hr, dry_weight_kg):
    clearance = 0.7 * qb  # mL/min
    time_min = duration_hr * 60
    v = 0.55 * dry_weight_kg * 1000  # Total body water in mL
    ktv = (clearance * time_min) / v
    return round(ktv, 2)

st.title("Simplified Kt/V Calculator for Hemodialysis")

qb = st.number_input("Blood Flow Rate (Qb) in mL/min", min_value=100, max_value=500, value=220)
duration_hr = st.number_input("Dialysis Duration (hours)", min_value=1.0, max_value=6.0, value=4.0)
dry_weight_kg = st.number_input("Dry Body Weight (kg)", min_value=20.0, max_value=120.0, value=48.5)

if st.button("Calculate Kt/V"):
    ktv = calculate_ktv(qb, duration_hr, dry_weight_kg)
    st.success(f"Kt/V Estimate: {ktv}")
    if ktv >= 1.7:
        st.info("Target Kt/V Achieved ✅")
    else:
        st.warning("Kt/V Below Target ⚠ Consider increasing Qb or duration.")
