zodiac = {
    1: (20, "Ma Ket", "Bao Binh"),
    2: (19, "Bao Binh", "Song Ngu"),
    3: (21, "Song Ngu", "Bach Duong"),
    4: (20, "Bach Duong", "Kim Nguu"),
    5: (21, "Kim Nguu", "Song Tu"),
    6: (21, "Song Tu", "Cu Giai"),
    7: (23, "Cu Giai", "Su Tu"),
    8: (23, "Su Tu", "Xu Nu"),
    9: (23, "Xu Nu", "Thien Binh"),
    10: (23, "Thien Binh", "Thien Yet"),
    11: (23, "Thien Yet", "Nhan Ma"),
    12: (22, "Nhan Ma", "Ma Ket"),
}

for t in range(int(input())):
    d, m = [int(x) for x in input().split()]
    pos, a, b = zodiac[m]
    if d < pos:
        print(a)
    else:
        print(b)
