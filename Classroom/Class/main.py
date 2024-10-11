from mathang import addmh, readmh
from nhanvien import addnv, readnv
from banhang import lap_bang_ban_hang, doc_bang_ban_hang
from thongke import (
    sort_name,
    sort_group,
    bang_ke,
)
from init import MatHang, NhanVien, BanHang

# Thêm mặt hàng
addmh("MH.DAT", MatHang(1001, "Tivi", "Điện tử", 12000000, 5))
readmh("MH.DAT")

# Thêm nhân viên
addnv("NV.DAT", NhanVien(1001, "Nguyen Van A", "Hà Nội", "0123456789"))
readnv("NV.DAT")

# Thêm bán hàng
lap_bang_ban_hang("QLBH.DAT", BanHang(1001, 1001, 2))
doc_bang_ban_hang("QLBH.DAT")

# Sắp xếp theo tên và nhóm mặt hàng
sort_name("QLBH.DAT")
sort_group("QLBH.DAT")

# Lập bảng kê doanh thu
bang_ke("QLBH.DAT", "MH.DAT")
