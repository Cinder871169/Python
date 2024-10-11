import pickle
from init import BanHang


def lap_bang_ban_hang(file_name, ban_hang):
    try:
        with open(file_name, "ab") as f:
            pickle.dump(ban_hang, f)
    except Exception as e:
        print("Error :", e)


def doc_bang_ban_hang(file_name):
    try:
        with open(file_name, "rb") as f:
            while True:
                try:
                    ban_hang = pickle.load(f)
                    print(vars(ban_hang))
                except EOFError:
                    break
    except FileNotFoundError:
        print("Chưa có dữ liệu bán hàng.")
    except Exception as e:
        print("Lỗi khi đọc danh sách bán hàng:", e)
