# =========================
# HOAT DONG 3
# DINH DANH & PEP8
# =========================

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("===== HOAT DONG 3 =====")
print("Ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)


# =========================
# HOAT DONG 5
# TOAN TU
# =========================

print("\n===== HOAT DONG 5 =====")

# Bai 5.1 - Toan tu so hoc

print("\n--- Bai 5.1 ---")

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# Bai 5.2 - Toan tu so sanh va logic

print("\n--- Bai 5.2 ---")

diem = 6.5
tuoi = 20

loai_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60

print("Diem dat loai Kha:", loai_kha)
print("Tuoi duoi 18 hoac tren 60:", chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien tren:", not chua_du_18_hoac_tren_60)


# Bai 5.3 - Toan tu gan va toan tu dac biet

print("\n--- Bai 5.3 ---")

x = 10
print("Gia tri ban dau:", x)

x += 5
print("Sau += 5:", x)

x -= 3
print("Sau -= 3:", x)

x *= 2
print("Sau *= 2:", x)

x /= 4
print("Sau /= 4:", x)

x //= 2
print("Sau //= 2:", x)

x **= 2
print("Sau **= 2:", x)

danh_sach = [1, 2, 3, "python"]

print("3 co trong danh_sach:", 3 in danh_sach)

bien_1 = danh_sach
bien_2 = danh_sach

print("bien_1 is bien_2:", bien_1 is bien_2)


# Bai 5.4 - Do uu tien toan tu

print("\n--- Bai 5.4 ---")

# Du doan:
# Dong 1: 50
# Dong 2: 80
# Dong 3: True

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)


# =========================
# HOAT DONG 6
# BIEN & DYNAMIC TYPING
# =========================

print("\n===== HOAT DONG 6 =====")

# Bai 6.1 - Dynamic typing

print("\n--- Bai 6.1 ---")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))


# Bai 6.2 - Bai toan tong hop

print("\n--- Bai 6.2 ---")

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi:", la_gioi)
print("Dat loai Kha:", la_kha)
print("Dat loai Trung binh:", la_trung_binh)
print("Dat loai Yeu:", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))