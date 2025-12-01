def so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
while True:
    try:
        n = int(input("Nhập một số nguyên dương: "))
        break
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

if so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")
