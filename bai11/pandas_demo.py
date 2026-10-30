import pandas as pd
from pathlib import Path


# Bài 2.1: Đọc CSV và xem tổng quan
duong_dan = Path(__file__).with_name("diem_sinh_vien.csv")
df = pd.read_csv(duong_dan)

print("=== BAI 2.1: DOC CSV VA XEM TONG QUAN ===")

# Xem 5 dòng đầu
print(df.head())

# Số dòng, số cột
print("So dong, so cot:", df.shape)

# Danh sách tên cột
print("Cac cot:", df.columns.tolist())


# Bài 2.2: Thống kê theo môn học
print("\n=== BAI 2.2: THONG KE THEO MON HOC ===")

diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)

print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())


# Bài 2.3: Tính điểm trung bình từng sinh viên
print("\n=== BAI 2.3: DIEM TRUNG BINH TUNG SINH VIEN ===")

diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)

# Lọc sinh viên đạt và không đạt
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)