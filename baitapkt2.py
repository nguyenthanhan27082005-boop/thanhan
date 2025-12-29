import random
def game_hiep_si():
    MAX_LUOT = 10
    TARGET_DAME = 400
    diem = 0
    for luot in range(1, MAX_LUOT + 1):
        print(f"Lượt {luot}:")
        ti_le_trung = random.random()
        if ti_le_trung < 0.7:
            sat_thuong = random.randint(50, 100)
            diem += sat_thuong
            print(f"Trúng đích! Gây sát thương: {sat_thuong} điểm. Tổng sát thương: {diem}")
            if diem >= TARGET_DAME:
                print("Quái vật bị tiêu diệt! Hiệp sĩ thắng!")
                break
        else:
            diem -= 20
            if diem < 0:
                diem = 0
            print(f"Trượt đích! Mất 20 điểm. Tổng sát thương: {diem}")
        print()
    else:
        print("Hết 10 lượt chưa tiêu diệt quái vật! Hiệp sĩ thua!")
if __name__ == '__main__':
    game_hiep_si()