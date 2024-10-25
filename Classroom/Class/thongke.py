import pickle


def sort_name(file_name):
    try:
        with open(file_name, "rb") as f:
            danh_sach = []
            while True:
                try:
                    ban_hang = pickle.load(f)
                    danh_sach.append(ban_hang)
                except EOFError:
                    break

            danh_sach.sort(
                key=lambda x: x.ma_nv
            )  # Sắp xếp theo mã NV (giả sử tên liên quan mã NV)
            for ban_hang in danh_sach:
                print(vars(ban_hang))
    except Exception as e:
        print("Error :", e)


def sort_group(file_name):
    try:
        with open(file_name, "rb") as f:
            danh_sach = []
            while True:
                try:
                    ban_hang = pickle.load(f)
                    danh_sach.append(ban_hang)
                except EOFError:
                    break

            danh_sach.sort(key=lambda x: x.ma_hang)  # Sắp xếp theo mã hàng
            for ban_hang in danh_sach:
                print(vars(ban_hang))
    except Exception as e:
        print("Error :", e)


def bang_ke(file_ban_hang, file_mat_hang):
    doanh_thu = {}
    try:
        with open(file_ban_hang, "rb") as f_bh, open(file_mat_hang, "rb") as f_mh:
            danh_sach_bh = []
            while True:
                try:
                    ban_hang = pickle.load(f_bh)
                    danh_sach_bh.append(ban_hang)
                except EOFError:
                    break

            mat_hang_dict = {}
            while True:
                try:
                    mat_hang = pickle.load(f_mh)
                    mat_hang_dict[mat_hang.ma_hang] = mat_hang.gia_ban
                except EOFError:
                    break

            for bh in danh_sach_bh:
                gia_ban = mat_hang_dict.get(bh.ma_hang, 0)
                if bh.ma_nv in doanh_thu:
                    doanh_thu[bh.ma_nv] += bh.so_luong_ban * gia_ban
                else:
                    doanh_thu[bh.ma_nv] = bh.so_luong_ban * gia_ban

        for ma_nv, dt in doanh_thu.items():
            print(f"Mã NV: {ma_nv}, Doanh thu: {dt}")
    except Exception as e:
        print("Lỗi khi lập bảng kê doanh thu:", e)


# Bui Ngoc Thien - B22DCCN822
