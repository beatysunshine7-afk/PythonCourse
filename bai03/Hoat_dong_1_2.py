ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")
ten_sv.insert(1, "Em")
print(ten_sv)

ten_sv.remove("Chi")
pop_ra = ten_sv.pop()
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()
print(ten_sv)

ten_sv.reverse()
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print(ten_sv)