def thong_ke_nhiet_do():
    nhiet_do = [28.5, 30.0, 32.5, 29.0, 31.5, 27.0, 33.0]
    so_luong = len(nhiet_do)
    tong = sum(nhiet_do)
    trung_binh = tong / so_luong if so_luong else 0.0
    print(f"Nhiệt độ trung bình: {trung_binh:.2f}°C")

    if nhiet_do:
        max_val = max(nhiet_do)
        print(f"Nhiệt độ cao nhất: {max_val:.2f}°C")
    else:
        print("Danh sách nhiệt độ rỗng.")

    dem = sum(1 for t in nhiet_do if t > 30)
    print(f"Số lượng ngày có nhiệt độ trên 30°C: {dem}")

    nhiet_do_sap_xep = nhiet_do[:]  
    n = len(nhiet_do_sap_xep)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nhiet_do_sap_xep[j] > nhiet_do_sap_xep[j + 1]:
                nhiet_do_sap_xep[j], nhiet_do_sap_xep[j + 1] = nhiet_do_sap_xep[j + 1], nhiet_do_sap_xep[j]

    print(f"Nhiệt độ sau khi sắp xếp: {nhiet_do_sap_xep}")

if __name__ == "__main__":
    thong_ke_nhiet_do()
