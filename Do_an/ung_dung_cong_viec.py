import sqlite3
import tkinter as tk
from datetime import date, datetime
from tkinter import ttk, messagebox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_cong_viec as db


CAC_MUC_UU_TIEN = ["Thấp", "Trung bình", "Cao"]


class UngDungCongViec(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quản lý công việc cá nhân")
        self.geometry("960x600")
        self.minsize(850, 550)

        self.id_dang_chon = None

        self.ten_var = tk.StringVar()
        self.han_var = tk.StringVar(value=date.today().isoformat())
        self.uu_tien_var = tk.StringVar(value="Trung bình")
        self.tong_hop_var = tk.StringVar()

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28)
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        ttk.Label(
            self,
            text="QUẢN LÝ CÔNG VIỆC CÁ NHÂN",
            font=("Arial", 18, "bold")
        ).pack(pady=(15, 10))

        khung_nhap = ttk.LabelFrame(
            self, text="Thông tin công việc", padding=12
        )
        khung_nhap.pack(fill="x", padx=15, pady=5)
        khung_nhap.columnconfigure(1, weight=1)

        ttk.Label(
            khung_nhap, text="Tên công việc:"
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.o_nhap_ten = ttk.Entry(
            khung_nhap, textvariable=self.ten_var
        )
        self.o_nhap_ten.grid(
            row=0, column=1, columnspan=3,
            sticky="ew", padx=(10, 0), pady=5
        )

        ttk.Label(
            khung_nhap, text="Hạn hoàn thành:"
        ).grid(row=1, column=0, sticky="w", pady=5)

        ttk.Entry(
            khung_nhap,
            textvariable=self.han_var,
            width=18
        ).grid(
            row=1, column=1, sticky="w",
            padx=(10, 0), pady=5
        )

        ttk.Label(
            khung_nhap, text="YYYY-MM-DD"
        ).grid(row=1, column=2, padx=10)

        ttk.Label(
            khung_nhap, text="Mức ưu tiên:"
        ).grid(row=2, column=0, sticky="w", pady=5)

        ttk.Combobox(
            khung_nhap,
            textvariable=self.uu_tien_var,
            values=CAC_MUC_UU_TIEN,
            state="readonly",
            width=16
        ).grid(
            row=2, column=1, sticky="w",
            padx=(10, 0), pady=5
        )

        khung_nut = ttk.Frame(self)
        khung_nut.pack(fill="x", padx=15, pady=10)

        cac_nut = [
            ("Thêm", self.xu_ly_them),
            ("Sửa", self.xu_ly_sua),
            ("Xóa", self.xu_ly_xoa),
            ("Đánh dấu hoàn thành", self.xu_ly_hoan_thanh),
            ("Làm mới", self.lam_moi),
            ("Thống kê", self.xu_ly_thong_ke)
            ]

        for cot, (ten_nut, ham_xu_ly) in enumerate(cac_nut):
            ttk.Button(
                khung_nut,
                text=ten_nut,
                command=ham_xu_ly
            ).grid(row=0, column=cot, padx=(0, 8))

        khung_bang = ttk.Frame(self)
        khung_bang.pack(
            fill="both", expand=True, padx=15, pady=5
        )

        cac_cot = (
            "id", "ten", "han", "uu_tien", "trang_thai"
        )

        self.bang = ttk.Treeview(
            khung_bang,
            columns=cac_cot,
            show="headings",
            selectmode="browse"
        )

        self.bang.heading("id", text="Mã")
        self.bang.heading("ten", text="Tên công việc")
        self.bang.heading("han", text="Hạn hoàn thành")
        self.bang.heading("uu_tien", text="Ưu tiên")
        self.bang.heading("trang_thai", text="Trạng thái")

        self.bang.column(
            "id", width=50, minwidth=40,
            anchor="center", stretch=False
        )
        self.bang.column("ten", width=320, minwidth=180)
        self.bang.column(
            "han", width=140, anchor="center",
            stretch=False
        )
        self.bang.column(
            "uu_tien", width=100, anchor="center",
            stretch=False
        )
        self.bang.column(
            "trang_thai", width=170, anchor="center",
            stretch=False
        )

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.bang.yview
        )
        self.bang.configure(
            yscrollcommand=thanh_cuon.set
        )

        thanh_cuon.pack(side="right", fill="y")
        self.bang.pack(
            side="left", fill="both", expand=True
        )

        self.bang.tag_configure(
            "hoan_thanh", foreground="#27803b"
        )
        self.bang.bind(
            "<<TreeviewSelect>>", self.chon_cong_viec
        )

        ttk.Label(
            self,
            textvariable=self.tong_hop_var,
            font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=15, pady=(8, 15))

    def tai_lai_danh_sach(self):
        danh_sach = db.lay_toan_bo_cong_viec()

        for dong in self.bang.get_children():
            self.bang.delete(dong)

        so_da_xong = 0

        for cong_viec in danh_sach:
            ma, ten, han, uu_tien, da_xong = cong_viec

            trang_thai = (
                "Đã hoàn thành"
                if da_xong == 1
                else "Chưa hoàn thành"
            )

            nhan = ("hoan_thanh",) if da_xong else ()

            self.bang.insert(
                "",
                tk.END,
                iid=str(ma),
                values=(
                    ma, ten, han, uu_tien, trang_thai
                ),
                tags=nhan
            )

            so_da_xong += da_xong

        tong = len(danh_sach)

        self.tong_hop_var.set(
            f"Tổng công việc: {tong}    |    "
            f"Đã hoàn thành: {so_da_xong}    |    "
            f"Chưa hoàn thành: {tong - so_da_xong}"
        )

        self.id_dang_chon = None

    def chon_cong_viec(self, event=None):
        lua_chon = self.bang.selection()

        if not lua_chon:
            self.id_dang_chon = None
            return

        dong = lua_chon[0]
        gia_tri = self.bang.item(dong, "values")

        self.id_dang_chon = int(dong)
        self.ten_var.set(gia_tri[1])
        self.han_var.set(gia_tri[2])
        self.uu_tien_var.set(gia_tri[3])

    def lay_du_lieu_nhap(self):
        ten = self.ten_var.get().strip()
        han = self.han_var.get().strip()
        uu_tien = self.uu_tien_var.get()

        if not ten or not han:
            messagebox.showerror(
                "Lỗi",
                "Vui lòng nhập đầy đủ tên công việc "
                "và hạn hoàn thành."
            )
            return None

        try:
            ngay = datetime.strptime(
                han, "%Y-%m-%d"
            ).date()

            if ngay.isoformat() != han:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Lỗi",
                "Ngày không hợp lệ. "
                "Hãy nhập theo dạng YYYY-MM-DD, "
                "ví dụ: 2026-12-20."
            )
            return None

        if uu_tien not in CAC_MUC_UU_TIEN:
            messagebox.showerror(
                "Lỗi", "Vui lòng chọn mức ưu tiên hợp lệ."
            )
            return None

        return ten, han, uu_tien

    def lam_moi(self):
        self.tai_lai_danh_sach()
        self.ten_var.set("")
        self.han_var.set(date.today().isoformat())
        self.uu_tien_var.set("Trung bình")
        self.o_nhap_ten.focus_set()

    def xu_ly_them(self):
        du_lieu = self.lay_du_lieu_nhap()

        if du_lieu is None:
            return

        try:
            db.them_cong_viec(*du_lieu)
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi dữ liệu", str(loi)
            )
            return

        self.lam_moi()
        messagebox.showinfo(
            "Thành công", "Đã thêm công việc."
        )

    def xu_ly_sua(self):
        if self.id_dang_chon is None:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn công việc cần sửa."
            )
            return

        du_lieu = self.lay_du_lieu_nhap()

        if du_lieu is None:
            return

        try:
            db.sua_cong_viec(
                self.id_dang_chon, *du_lieu
            )
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi dữ liệu", str(loi)
            )
            return

        self.lam_moi()
        messagebox.showinfo(
            "Thành công", "Đã cập nhật công việc."
        )

    def xu_ly_xoa(self):
        if self.id_dang_chon is None:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn công việc cần xóa."
            )
            return

        dong = str(self.id_dang_chon)
        ten = self.bang.item(dong, "values")[1]

        xac_nhan = messagebox.askyesno(
            "Xác nhận xóa",
            f"Bạn có muốn xóa công việc:\n{ten}?"
        )

        if not xac_nhan:
            return

        try:
            db.xoa_cong_viec(self.id_dang_chon)
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi dữ liệu", str(loi)
            )
            return

        self.lam_moi()

    def xu_ly_hoan_thanh(self):
        if self.id_dang_chon is None:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn công việc "
                "cần đánh dấu hoàn thành."
            )
            return

        try:
            db.danh_dau_hoan_thanh(
                self.id_dang_chon
            )
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi dữ liệu", str(loi)
            )
            return

        self.lam_moi()

    def xu_ly_thong_ke(self):
        try:
            du_lieu = db.thong_ke_theo_trang_thai()
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi dữ liệu", str(loi)
            )
            return

        if not du_lieu:
            messagebox.showinfo(
                "Thông báo",
                "Chưa có công việc để thống kê."
            )
            return

        thong_ke = dict(du_lieu)

        nhan = [
            "Chưa hoàn thành",
            "Đã hoàn thành"
        ]
        so_luong = [
            thong_ke.get(0, 0),
            thong_ke.get(1, 0)
        ]
        fig, ax = plt.subplots(figsize=(7, 4))

        cac_cot = ax.bar(
            nhan,
            so_luong,
            color=["#f0ad4e", "#5cb85c"]
        )

        for cot in cac_cot:
            cao = int(cot.get_height())
            ax.annotate(
                str(cao),
                (

                    cot.get_x() + cot.get_width() / 2,
                    cao
                ),
                xytext=(0, 5),
                textcoords="offset points",
                ha="center"
            )

        ax.set_title("THỐNG KÊ CÔNG VIỆC THEO TRẠNG THÁI")
        ax.set_xlabel("Trạng thái")
        ax.set_ylabel("Số lượng công việc")
       
        cao_nhat = max(so_luong)
        ax.set_ylim(0, cao_nhat + 1)
       
        from matplotlib.ticker import MaxNLocator
        ax.yaxis.set_major_locator(
            MaxNLocator(integer=True)
        )

        fig.tight_layout()

        duong_dan_anh = (
            db.TEN_FILE_CSDL.parent / "thong_ke_cong_viec.png"
        )

        try:
            fig.savefig(
                duong_dan_anh,
                dpi=150,
                bbox_inches="tight"
            )
        except OSError as loi:
            messagebox.showerror(
                "Lỗi lưu ảnh",
                f"Không thể lưu biểu đồ:\n{loi}"
            )
            plt.close(fig)
            return

        plt.show()
if __name__ == "__main__":
    ung_dung = UngDungCongViec()
    ung_dung.mainloop()
       