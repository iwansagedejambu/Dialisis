def calculate_ktv(qb, duration_hr, dry_weight_kg):
    clearance = 0.7 * qb  # mL/min
    time_min = duration_hr * 60
    v = 0.55 * dry_weight_kg * 1000  # V in mL
    ktv = (clearance * time_min) / v
    return round(ktv, 2)

qb = int(input("Masukkan Qb (mL/min): "))
duration = float(input("Durasi dialysis (jam): "))
dry_weight = float(input("Berat kering (kg): "))
ktv = calculate_ktv(qb, duration, dry_weight)
print(f"Kt/V: {ktv}")

if ktv >= 1.7:
    print("Target Kt/V tercapai.")
else:
    print("Kt/V di bawah target. Pertimbangkan penyesuaian Qb atau durasi.")