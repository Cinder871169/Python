import tkinter as tk
from tkinter import messagebox
import os


# Hàm thực hiện tính toán
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Sử dụng eval để tính toán biểu thức
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        save_result(expression, result)
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Biểu thức không hợp lệ!\n{e}")


# Hàm lưu kết quả vào file
def save_result(expression, result):
    if not os.path.exists("results.txt"):
        with open("results.txt", "w") as f:
            f.write("Lịch sử tính toán:\n")
    with open("results.txt", "a") as f:
        f.write(f"{expression} = {result}\n")


# Hàm xóa kết quả
def clear_entry():
    entry.delete(0, tk.END)


# Tạo giao diện
root = tk.Tk()
root.title("Máy Tính Cá Nhân")
root.geometry("420x450")  # Kích thước cửa sổ

# Khung nhập biểu thức với giao diện tùy chỉnh
entry = tk.Entry(
    root,
    font=("Arial", 24, "bold"),  # Font chữ lớn và đậm
    justify="right",  # Căn phải
    bd=10,  # Độ dày viền
    relief="sunken",  # Hiệu ứng chìm
    bg="lightyellow",  # Màu nền
    fg="black",  # Màu chữ
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Danh sách các nút
buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "C",
    "0",
    "=",
    "+",
]

# Thêm nút vào giao diện với tùy chỉnh
row = 1
col = 0
for button in buttons:

    def cmd(x=button):  # Hàm lệnh cho mỗi nút
        if x == "=":
            calculate()
        elif x == "C":
            clear_entry()
        else:
            entry.insert(tk.END, x)

    tk.Button(
        root,
        text=button,
        font=("Arial", 16, "bold"),  # Font chữ đậm
        command=cmd,
        width=6,
        height=2,
        bg="lightblue",  # Màu nền
        fg="black",  # Màu chữ
        bd=5,  # Độ dày viền
        relief="raised",  # Hiệu ứng nổi
    ).grid(
        row=row, column=col, padx=5, pady=5
    )  # Khoảng cách giữa các nút
    col += 1
    if col > 3:
        col = 0
        row += 1

# Chạy giao diện chính
root.mainloop()
