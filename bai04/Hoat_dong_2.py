diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

# Duyet cac khoa
for mon in diem_mon_hoc.keys():
    print(mon)

# Duyet cac gia tri
for diem in diem_mon_hoc.values():
    print(diem)

# Duyet ca khoa va gia tri
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# Tinh diem trung binh
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))