def chuanHoa(ten):
    return " ".join(ten.strip().title().split())


def calc(dt, kv):
    ut = 0
    if kv == "1":
        ut += 1.5
    elif kv == "2":
        ut += 1
    if dt != "Kinh":
        ut += 1.5
    return ut


def ketqua(total, diem_chuan):
    return "Do" if total >= diem_chuan else "Truot"


def sapXep(ds):
    return sorted(ds, key=lambda x: (-x["total"], x["id"]))


def xuLy(n, diem_chuan=20.5):
    lst = []
    for i in range(n):
        id = f"TS{str(i+1).zfill(2)}"
        name = chuanHoa(input())
        diem_thi = float(input())
        dt = input().strip()
        kv = input().strip()

        ut = calc(dt, kv)
        total = round(diem_thi + ut, 1)
        trang_thai = ketqua(total, diem_chuan)

        lst.append(
            {
                "id": id,
                "name": name,
                "dt": dt,
                "kv": kv,
                "total": total,
                "trang_thai": trang_thai,
            }
        )

    lst_sap_xep = sapXep(lst)

    for thi_sinh in lst_sap_xep:
        print(
            f"{thi_sinh['id']} {thi_sinh['name']} {thi_sinh['total']} {thi_sinh['trang_thai']}"
        )


n = int(input())
xuLy(n)
