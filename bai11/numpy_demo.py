import numpy as np


# List Python thuần
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]

# Chuyển sang mảng NumPy
diem_array = np.array(diem_list)

print(type(diem_list), type(diem_array))


# Cộng trực tiếp 0.5 vào toàn bộ phần tử của mảng
diem_cong_them = diem_array + 0.5
print(diem_cong_them)


# Với list Python, cần duyệt từng phần tử
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)


# Thống kê trên mảng điểm ban đầu
print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))


# Tạo ma trận gồm 2 hàng, 3 cột
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])

print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)