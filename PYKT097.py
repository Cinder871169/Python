import re
from sys import stdin


def chuan_hoa(line):
    words = re.split(r"\s+", line.lower().strip())
    if re.match(r"^.*[\.!?]$", words[-1]):
        if len(words[-1]) > 1:
            return " ".join(words).capitalize()
        else:
            return " ".join(words[:-1]).capitalize() + words[-1]
    else:
        return " ".join(words).capitalize() + "."


for line in stdin.readlines():
    print(chuan_hoa(line))

# Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
# co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
# muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
# moi    CAC BAN danG ky     thaM giA !
