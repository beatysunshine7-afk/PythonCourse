import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

cac_diem = [(0, 0), (3, 4), (6, 8)]

for x, y in cac_diem:
    khoang_cach_goc = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach tu {(x, y)} den (0, 0) la: {round(khoang_cach_goc, 2)}")