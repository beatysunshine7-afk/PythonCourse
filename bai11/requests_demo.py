import requests


# Bài 5.1: Gọi API GitHub và đọc dữ liệu JSON
print("=== BAI 5.1: THONG TIN REPOSITORY GITHUB ===")

try:
    response = requests.get(
        "https://api.github.com/repos/python/cpython",
        timeout=20
    )

    if response.status_code == 200:
        du_lieu = response.json()

        print("Ten repository:", du_lieu["full_name"])
        print("So luot gan sao (stars):", du_lieu["stargazers_count"])
        print("Ngon ngu chinh:", du_lieu["language"])
    else:
        print("Goi API that bai, ma loi:", response.status_code)

except requests.exceptions.RequestException as loi:
    print("Loi ket noi API GitHub:", loi)

except ValueError:
    print("Du lieu tra ve khong phai JSON hop le.")


# Bài 5.2: Gọi API tỷ giá ngoại tệ
print("\n=== BAI 5.2: TY GIA USD SANG VND ===")

try:
    response = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=20
    )

    if response.status_code == 200:
        du_lieu = response.json()

        ty_gia_vnd = du_lieu["rates"]["VND"]
        print(f"1 USD = {ty_gia_vnd:,.0f} VND")
    else:
        print("Khong lay duoc ty gia, ma loi:", response.status_code)

except requests.exceptions.RequestException as loi:
    print("Loi ket noi API ty gia:", loi)

except ValueError:
    print("Du lieu tra ve khong phai JSON hop le.")