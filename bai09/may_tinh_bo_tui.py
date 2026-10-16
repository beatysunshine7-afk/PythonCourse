import tkinter as tk
from tkinter import messagebox


def bam_nut(ky_tu):
    bien_bieu_thuc.set(bien_bieu_thuc.get() + ky_tu)


def xoa():
    bien_bieu_thuc.set("")


def tinh_ket_qua():
    bieu_thuc = bien_bieu_thuc.get()

    if not bieu_thuc:
        messagebox.showerror("Loi", "Vui long nhap phep tinh.")
        return

    try:
        ket_qua = eval(bieu_thuc, {"__builtins__": {}}, {})
        bien_bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
    except (SyntaxError, TypeError, ValueError):
        messagebox.showerror("Loi", "Phep tinh khong hop le.")


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

o_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_bieu_thuc,
    font=("Arial", 18),
    justify="right",
    width=20,
    state="readonly"
)
o_hien_thi.grid(
    row=0, column=0, columnspan=4, padx=10, pady=10
)

cac_nut = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"]
]

for hang, danh_sach_nut in enumerate(cac_nut, start=1):
    for cot, ky_tu in enumerate(danh_sach_nut):
        if ky_tu == "C":
            lenh = xoa
        else:
            lenh = lambda k=ky_tu: bam_nut(k)

        tk.Button(
            cua_so,
            text=ky_tu,
            font=("Arial", 14),
            width=5,
            height=2,
            command=lenh
        ).grid(row=hang, column=cot, padx=3, pady=3)

tk.Button(
    cua_so,
    text="=",
    font=("Arial", 14),
    command=tinh_ket_qua
).grid(
    row=5, column=0, columnspan=4,
    padx=5, pady=10, sticky="ew"
)

cua_so.mainloop()