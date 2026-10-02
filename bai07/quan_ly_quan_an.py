danh_sach_mon = [
    {"ma_mon": "M01", "ten_mon": "Com rang", "gia": 35000},
    {"ma_mon": "M02", "ten_mon": "Pho bo", "gia": 45000},
    {"ma_mon": "M03", "ten_mon": "Bun cha", "gia": 40000},
    {"ma_mon": "M04", "ten_mon": "Tra da", "gia": 5000}
]

danh_sach_ban = [
    {"ma_ban": "B01", "don_hang": []},
    {"ma_ban": "B02", "don_hang": []},
    {"ma_ban": "B03", "don_hang": []},
    {"ma_ban": "B04", "don_hang": []}
]

lich_su_hoa_don = []


def nhap_so_nguyen_duong(loi_nhac):
    while True:
        try:
            so = int(input(loi_nhac))
            if so > 0:
                return so
            print("-> Phai nhap so lon hon 0.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap so nguyen.")


def nhap_chuoi(loi_nhac):
    while True:
        chuoi = input(loi_nhac).strip()
        if chuoi:
            return chuoi
        print("-> Khong duoc de trong.")


def tim_mon(ma_mon):
    for mon in danh_sach_mon:
        if mon["ma_mon"] == ma_mon:
            return mon
    return None


def tim_ban(ma_ban):
    for ban in danh_sach_ban:
        if ban["ma_ban"] == ma_ban:
            return ban
    return None


def hien_thi_thuc_don():
    print("\n" + "=" * 50)
    print(f"{'Ma mon':<10}{'Ten mon':<25}{'Gia (VND)':>15}")
    print("-" * 50)

    for mon in danh_sach_mon:
        print(f"{mon['ma_mon']:<10}{mon['ten_mon']:<25}{mon['gia']:>15,}")

    if not danh_sach_mon:
        print("Thuc don chua co mon an.")

    print("=" * 50)


def them_mon():
    ma_mon = nhap_chuoi("Nhap ma mon moi: ").upper()

    if tim_mon(ma_mon) is not None:
        print("-> Ma mon da ton tai.")
        return

    ten_mon = nhap_chuoi("Nhap ten mon: ")
    gia = nhap_so_nguyen_duong("Nhap gia mon: ")

    danh_sach_mon.append({
        "ma_mon": ma_mon,
        "ten_mon": ten_mon,
        "gia": gia
    })

    print("-> Them mon thanh cong.")


def sua_mon():
    ma_mon = nhap_chuoi("Nhap ma mon can sua: ").upper()
    mon = tim_mon(ma_mon)

    if mon is None:
        print("-> Khong tim thay mon.")
        return

    mon["ten_mon"] = nhap_chuoi("Nhap ten mon moi: ")
    mon["gia"] = nhap_so_nguyen_duong("Nhap gia moi: ")

    print("-> Sua mon thanh cong.")


def xoa_mon():
    ma_mon = nhap_chuoi("Nhap ma mon can xoa: ").upper()
    mon = tim_mon(ma_mon)

    if mon is None:
        print("-> Khong tim thay mon.")
        return

    xac_nhan = input("Xac nhan xoa (y/n): ").strip().lower()

    if xac_nhan == "y":
        danh_sach_mon.remove(mon)
        print("-> Xoa mon thanh cong.")
    else:
        print("-> Da huy xoa.")


def tim_kiem_mon():
    tu_khoa = nhap_chuoi("Nhap ma hoac ten mon can tim: ").lower()
    tim_thay = False

    for mon in danh_sach_mon:
        if (
            tu_khoa in mon["ma_mon"].lower()
            or tu_khoa in mon["ten_mon"].lower()
        ):
            print(
                f"{mon['ma_mon']} - {mon['ten_mon']} - "
                f"{mon['gia']:,} VND"
            )
            tim_thay = True

    if not tim_thay:
        print("-> Khong tim thay mon phu hop.")


def hien_thi_ban():
    print("\n--- DANH SACH BAN ---")

    for ban in danh_sach_ban:
        trang_thai = "Dang phuc vu" if ban["don_hang"] else "Trong"
        print(f"{ban['ma_ban']} - {trang_thai}")


def goi_mon():
    ma_ban = nhap_chuoi("Nhap ma ban: ").upper()
    ban = tim_ban(ma_ban)

    if ban is None:
        print("-> Khong tim thay ban.")
        return

    hien_thi_thuc_don()
    ma_mon = nhap_chuoi("Nhap ma mon can goi: ").upper()
    mon = tim_mon(ma_mon)

    if mon is None:
        print("-> Khong tim thay mon.")
        return

    so_luong = nhap_so_nguyen_duong("Nhap so luong: ")

    for chi_tiet in ban["don_hang"]:
        if (
            chi_tiet["ma_mon"] == ma_mon
            and chi_tiet["ten_mon"] == mon["ten_mon"]
            and chi_tiet["gia"] == mon["gia"]
        ):
            chi_tiet["so_luong"] += so_luong
            print("-> Da them mon vao don hang.")
            return

    ban["don_hang"].append({
        "ma_mon": mon["ma_mon"],
        "ten_mon": mon["ten_mon"],
        "gia": mon["gia"],
        "so_luong": so_luong
    })

    print("-> Goi mon thanh cong.")


def in_don_hang(ban):
    print(f"\n--- DON HANG BAN {ban['ma_ban']} ---")
    print(
        f"{'STT':<5}{'Ten mon':<22}{'SL':>5}"
        f"{'Don gia':>12}{'Thanh tien':>15}"
    )

    tong_tien = 0

    for stt, chi_tiet in enumerate(ban["don_hang"], start=1):
        thanh_tien = chi_tiet["gia"] * chi_tiet["so_luong"]
        tong_tien += thanh_tien

        print(
            f"{stt:<5}{chi_tiet['ten_mon']:<22}"
            f"{chi_tiet['so_luong']:>5}"
            f"{chi_tiet['gia']:>12,}{thanh_tien:>15,}"
        )

    print(f"TONG TIEN: {tong_tien:,} VND")
    return tong_tien


def xem_don_hang():
    ma_ban = nhap_chuoi("Nhap ma ban: ").upper()
    ban = tim_ban(ma_ban)

    if ban is None:
        print("-> Khong tim thay ban.")
        return

    if not ban["don_hang"]:
        print("-> Ban chua goi mon.")
        return

    in_don_hang(ban)


def huy_mon():
    ma_ban = nhap_chuoi("Nhap ma ban: ").upper()
    ban = tim_ban(ma_ban)

    if ban is None:
        print("-> Khong tim thay ban.")
        return

    if not ban["don_hang"]:
        print("-> Ban chua goi mon.")
        return

    in_don_hang(ban)
    stt = nhap_so_nguyen_duong("Nhap STT mon can huy: ")

    if stt > len(ban["don_hang"]):
        print("-> STT khong hop le.")
        return

    chi_tiet = ban["don_hang"][stt - 1]
    so_luong = nhap_so_nguyen_duong("Nhap so luong can huy: ")

    if so_luong > chi_tiet["so_luong"]:
        print("-> So luong huy vuot qua so luong da goi.")
        return

    chi_tiet["so_luong"] -= so_luong

    if chi_tiet["so_luong"] == 0:
        ban["don_hang"].remove(chi_tiet)

    print("-> Huy mon thanh cong.")


def thanh_toan():
    ma_ban = nhap_chuoi("Nhap ma ban can thanh toan: ").upper()
    ban = tim_ban(ma_ban)
    if ban is None:
        print("-> Khong tim thay ban.")
        return

    if not ban["don_hang"]:
        print("-> Ban chua co don hang.")
        return

    tong_tien = in_don_hang(ban)
    xac_nhan = input("Xac nhan da thanh toan (y/n): ").strip().lower()

    if xac_nhan != "y":
        print("-> Chua thanh toan.")
        return

    lich_su_hoa_don.append({
        "ma_hoa_don": f"HD{len(lich_su_hoa_don) + 1:03}",
        "ma_ban": ma_ban,
        "chi_tiet": [chi_tiet.copy() for chi_tiet in ban["don_hang"]],
        "tong_tien": tong_tien
    })

    ban["don_hang"].clear()
    print("-> Thanh toan thanh cong. Ban da tro ve trang thai trong.")


def thong_ke_doanh_thu():
    if not lich_su_hoa_don:
        print("-> Chua co hoa don da thanh toan.")
        return

    tong_doanh_thu = 0
    print("\n--- LICH SU HOA DON ---")

    for hoa_don in lich_su_hoa_don:
        print(
            f"{hoa_don['ma_hoa_don']} - {hoa_don['ma_ban']} - "
            f"{hoa_don['tong_tien']:,} VND"
        )
        tong_doanh_thu += hoa_don["tong_tien"]

    print("So hoa don:", len(lich_su_hoa_don))
    print(f"TONG DOANH THU: {tong_doanh_thu:,} VND")


def hien_thi_menu():
    print("\n========== QUAN LY QUAN AN ==========")
    print("1. Hien thi thuc don")
    print("2. Them mon an")
    print("3. Sua mon an")
    print("4. Xoa mon an")
    print("5. Tim kiem mon an")
    print("6. Hien thi danh sach ban")
    print("7. Goi mon cho ban")
    print("8. Xem don hang cua ban")
    print("9. Huy mon cua ban")
    print("10. Thanh toan")
    print("11. Thong ke doanh thu")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon: ").strip()

        if lua_chon == "1":
            hien_thi_thuc_don()
        elif lua_chon == "2":
            them_mon()
        elif lua_chon == "3":
            sua_mon()
        elif lua_chon == "4":
            xoa_mon()
        elif lua_chon == "5":
            tim_kiem_mon()
        elif lua_chon == "6":
            hien_thi_ban()
        elif lua_chon == "7":
            goi_mon()
        elif lua_chon == "8":
            xem_don_hang()
        elif lua_chon == "9":
            huy_mon()
        elif lua_chon == "10":
            thanh_toan()
        elif lua_chon == "11":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()