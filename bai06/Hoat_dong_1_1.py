def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bscnn(a, b):
    return a * b // uscln(a, b)


def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# Goi thu voi nhieu bo du lieu
print("USCLN:")
print(uscln(24, 36))
print(uscln(18, 30))
print(uscln(15, 25))

print("BSCNN:")
print(bscnn(4, 6))
print(bscnn(8, 12))
print(bscnn(10, 15))

print("Kiem tra so nguyen to:")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(10))
print(kiem_tra_nguyen_to(17))

print("Kiem tra so hoan thien:")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(10))