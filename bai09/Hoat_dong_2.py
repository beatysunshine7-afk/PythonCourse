import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Radiobutton")
cua_so.geometry("300x200")

# Gia tri mac dinh la ca nhan
bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Label(
    cua_so,
    text="Chon loai tai khoan:",
    font=("Arial", 12)
).pack(pady=10)

tk.Radiobutton(
    cua_so,
    text="Ca nhan",
    variable=bien_loai_tai_khoan,
    value="ca_nhan"
).pack(anchor="w", padx=30)

tk.Radiobutton(
    cua_so,
    text="Doanh nghiep",
    variable=bien_loai_tai_khoan,
    value="doanh_nghiep"
).pack(anchor="w", padx=30)


def xem_loai_tai_khoan():
    nhan_ket_qua.config(
        text=f"Ban da chon: {bien_loai_tai_khoan.get()}"
    )


tk.Button(
    cua_so,
    text="Xac nhan",
    command=xem_loai_tai_khoan
).pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()