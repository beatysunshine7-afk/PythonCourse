def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return


def chia_lay_thuong_du(a, b):
    return a // b, a % b


in_loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)

print(f"Thuong: {thuong}, du: {du}")