dk = True
while dk:
    try:
        N = int(input("Nhap N: "))
        if N > 0:
            break
    except ValueError:
        print("Loi kieu du lieu!")

i = 1
while i <= N:
    print(f"{i}", end= " ")
    i+= 1
