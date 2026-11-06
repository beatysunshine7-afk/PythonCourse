import sqlite3
import sys
from pathlib import Path


# Xác định thư mục lưu dữ liệu
if getattr(sys, "frozen", False):
    THU_MUC = Path(sys.executable).resolve().parent
else:
    THU_MUC = Path(__file__).resolve().parent

TEN_FILE_CSDL = THU_MUC / "cong_viec.db"


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()

    try:
        ket_noi.execute("""
            CREATE TABLE IF NOT EXISTS cong_viec (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_cong_viec TEXT NOT NULL,
                han_hoan_thanh TEXT NOT NULL,
                muc_uu_tien TEXT NOT NULL,
                da_hoan_thanh INTEGER NOT NULL DEFAULT 0
                    CHECK (da_hoan_thanh IN (0, 1))
            )
        """)
        ket_noi.commit()
    finally:
        ket_noi.close()


def them_cong_viec(
    ten_cong_viec, han_hoan_thanh, muc_uu_tien
):
    ket_noi = ket_noi_csdl()

    try:
        ket_noi.execute("""
            INSERT INTO cong_viec (
                ten_cong_viec,
                han_hoan_thanh,
                muc_uu_tien,
                da_hoan_thanh
            )
            VALUES (?, ?, ?, 0)
        """, (
            ten_cong_viec,
            han_hoan_thanh,
            muc_uu_tien
        ))
        ket_noi.commit()
    finally:
        ket_noi.close()


def lay_toan_bo_cong_viec():
    ket_noi = ket_noi_csdl()

    try:
        con_tro = ket_noi.execute("""
            SELECT
                id,
                ten_cong_viec,
                han_hoan_thanh,
                muc_uu_tien,
                da_hoan_thanh
            FROM cong_viec
            ORDER BY da_hoan_thanh, han_hoan_thanh, id
        """)
        return con_tro.fetchall()
    finally:
        ket_noi.close()


def sua_cong_viec(
    id_cong_viec,
    ten_cong_viec,
    han_hoan_thanh,
    muc_uu_tien
):
    ket_noi = ket_noi_csdl()

    try:
        ket_noi.execute("""
            UPDATE cong_viec
            SET ten_cong_viec = ?,
                han_hoan_thanh = ?,
                muc_uu_tien = ?
            WHERE id = ?
        """, (
            ten_cong_viec,
            han_hoan_thanh,
            muc_uu_tien,
            id_cong_viec
        ))
        ket_noi.commit()
    finally:
        ket_noi.close()


def xoa_cong_viec(id_cong_viec):
    ket_noi = ket_noi_csdl()

    try:
        ket_noi.execute(
            "DELETE FROM cong_viec WHERE id = ?",
            (id_cong_viec,)
        )
        ket_noi.commit()
    finally:
        ket_noi.close()


def danh_dau_hoan_thanh(id_cong_viec):
    ket_noi = ket_noi_csdl()

    try:
        ket_noi.execute("""
            UPDATE cong_viec
            SET da_hoan_thanh = 1
            WHERE id = ?
        """, (id_cong_viec,))
        ket_noi.commit()
    finally:
        ket_noi.close()


def thong_ke_theo_trang_thai():
    ket_noi = ket_noi_csdl()

    try:
        con_tro = ket_noi.execute("""
SELECT da_hoan_thanh, COUNT(*)
            FROM cong_viec
            GROUP BY da_hoan_thanh
            ORDER BY da_hoan_thanh
        """)
        return con_tro.fetchall()
    finally:
        ket_noi.close()