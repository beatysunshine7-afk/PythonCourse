from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# Đọc file CSV cùng thư mục với file Python
thu_muc = Path(__file__).resolve().parent
df = pd.read_csv(thu_muc / "diem_sinh_vien.csv")


# Bài 3.1: Biểu đồ cột - điểm trung bình theo môn học
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

plt.figure(figsize=(6, 4))

plt.bar(
    diem_trung_binh_mon.index,
    diem_trung_binh_mon.values,
    color="skyblue"
)

plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")

plt.tight_layout()
plt.savefig(thu_muc / "bieu_do_cot.png")
plt.show()


# Bài 3.2: Biểu đồ đường - điểm qua các lần kiểm tra
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))

plt.plot(
    lan_kiem_tra,
    diem_qua_cac_lan,
    marker="o",
    color="green"
)

plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")

plt.tight_layout()
plt.savefig(thu_muc / "bieu_do_duong.png")
plt.show()