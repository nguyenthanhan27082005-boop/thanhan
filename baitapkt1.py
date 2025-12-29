try:
    toan = float(input("Nhập điểm toán: "))
    van = float(input("Nhập điểm văn: "))
    anh = float(input("Nhập điểm anh: "))
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")
    exit(1)

if toan < 0 or toan > 10 or van < 0 or van > 10 or anh < 0 or anh > 10:
    print("Lỗi: Điểm phải nằm trong khoảng 0 đến 10.")
else:
    dtk = (toan * 2 + van + anh) / 4

    if dtk >= 9.0:
        bac = 4
    elif dtk >= 8.0:
        bac = 3
    elif dtk >= 7.0:
        bac = 2
    else:
        bac = 1

    danh_sach_loai = {
        4: ("Xuất sắc", 5000000),
        3: ("Giỏi", 3000000),
        2: ("Khá", 1000000),
        1: ("Trung bình", 0),
    }
    xep_loai, hoc_bong = danh_sach_loai[bac]

    if toan < 4.0 or van < 4.0 or anh < 4.0:
        if bac > 1:
            bac -= 1
            xep_loai, hoc_bong = danh_sach_loai[bac]
        else:
            xep_loai, hoc_bong = danh_sach_loai[1]

    print("-" * 30)
    print(f"Điểm tổng: {dtk:.2f}")
    print(f"Xếp loại: {xep_loai}")
    print(f"Số tiền học bổng: {hoc_bong} VND")
