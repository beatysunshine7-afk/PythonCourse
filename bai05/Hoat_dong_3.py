# for voi range()
for i in range(1, 6):
    print(i)

# for duyet list
diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
    print("Diem:", diem)

# for duyet tuple
toa_do = (3, 5)
for gia_tri in toa_do:
    print(gia_tri)

# for duyet dictionary
diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}

for mon, diem in diem_mon.items():
    print(mon, ":", diem)

# for duyet string
ten = "Python"
for ky_tu in ten:
    print(ky_tu)

# Bai tap van dung - Bang cuu chuong
n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")