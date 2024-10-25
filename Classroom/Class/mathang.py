import pickle
from init import MatHang


def addmh(file_name, mat_hang):
    try:
        with open(file_name, "ab") as f:
            pickle.dump(mat_hang, f)
    except Exception as e:
        print("Error: ", e)


def readmh(file_name):
    try:
        with open(file_name, "rb") as f:
            while True:
                try:
                    mat_hang = pickle.load(f)
                    print(vars(mat_hang))
                except EOFError:
                    break
    except FileNotFoundError:
        print("Chưa có mặt hàng nào.")
    except Exception as e:
        print("Lỗi khi đọc danh sách mặt hàng:", e)

#Bui Ngoc Thien - B22DCCN822