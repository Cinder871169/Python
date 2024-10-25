import pickle
from init import NhanVien


def addnv(file_name, nhan_vien):
    try:
        with open(file_name, "ab") as f:
            pickle.dump(nhan_vien, f)
    except Exception as e:
        print("Error :", e)


def readnv(file_name):
    try:
        with open(file_name, "rb") as f:
            while True:
                try:
                    nhan_vien = pickle.load(f)
                    print(vars(nhan_vien))
                except EOFError:
                    break
    except FileNotFoundError:
        print("Chưa có nhân viên nào.")
    except Exception as e:
        print("Lỗi khi đọc danh sách nhân viên:", e)


# Bui Ngoc Thien - B22DCCN822
