from pathlib import Path
from tempfile import TemporaryDirectory

import csdl_sach as db


def kiem_thu():
    with TemporaryDirectory() as thu_muc_tam:
        # Database riêng dành cho kiểm thử
        db.TEN_FILE_CSDL = Path(thu_muc_tam) / "kiem_thu.db"

        db.tao_bang_neu_chua_co()

        # Bước 1: Thêm 4 sách
        db.them_sach(
            "Doc Vi Nhan Sinh",
            "Robert Cialdini",
            "Ky nang song"
        )

        db.them_sach(
            "Dac Nhan Tam",
            "Dale Carnegie",
            "Ky nang song"
        )

        db.them_sach(
            "Nha Gia Kim",
            "Paulo Coelho",
            "Tieu thuyet"
        )

        db.them_sach(
            "Sapiens",
            "Yuval Noah Harari",
            "Lich su"
        )

        print("Danh sach sach:")
        for sach in db.lay_toan_bo_sach():
            print(sach)

        assert len(db.lay_toan_bo_sach()) == 4

        # Bước 2: Đánh dấu sách ID 1 đã đọc
        db.danh_dau_da_doc(1)

        print("\nSau khi danh dau da doc id=1:")
        for sach in db.lay_toan_bo_sach():
            print(sach)

        assert db.lay_toan_bo_sach()[0][4] == 1

        # Bước 3: Xóa sách ID 3 - Nhà Giả Kim
        db.xoa_sach(3)

        print("\nSau khi xoa sach id=3:")
        for sach in db.lay_toan_bo_sach():
            print(sach)

        assert len(db.lay_toan_bo_sach()) == 3
        assert all(sach[0] != 3 for sach in db.lay_toan_bo_sach())

        # Bước 4: Thống kê theo thể loại
        thong_ke = db.thong_ke_theo_the_loai()

        print("\nThong ke theo the loai:")
        print(thong_ke)

        assert dict(thong_ke) == {
            "Ky nang song": 2,
            "Lich su": 1
        }

        print("\nKIEM THU THANH CONG: Tat ca cac buoc deu dung.")


if __name__ == "__main__":
    kiem_thu()