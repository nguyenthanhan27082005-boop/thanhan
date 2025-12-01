while True:
    try:
        n = int(input("Nhập số dòng: "))
        break
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

for i in range(1, n + 1):
    print('*' * i)