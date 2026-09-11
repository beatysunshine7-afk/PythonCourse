sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

# Them khoa moi
sinh_vien["lop"] = "CNTT01"

# Sua gia tri khoa da co
sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

# Xoa theo khoa, dong thoi lay gia tri vua xoa
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

# Cap nhat / them nhieu khoa cung luc
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

print(sinh_vien)