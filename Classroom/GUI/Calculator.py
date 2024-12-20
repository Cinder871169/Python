# Nhóm 13
# Nguyễn Quang Tự B22DCCN774
# Cao Đức Việt B22DCCN894
# Bùi Ngọc Thiện B22DCCN822
# Nguyễn Công Trung B22DCCN870
# Lê Quang Huy B22DCCN382

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
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")  # Hiển thị cửa sổ lỗi
    except Exception as e:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")  # Hiển thị cửa sổ lỗi


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


# Hàm hiển thị lịch sử
def show_history():
    if not os.path.exists("results.txt"):
        messagebox.showinfo("Lịch sử", "Chưa có lịch sử tính toán.")
        return

    # Tạo cửa sổ mới để hiển thị lịch sử
    history_window = tk.Toplevel(root)
    history_window.title("Lịch sử Tính Toán")
    history_window.geometry("400x300")

    # Khung hiển thị lịch sử
    with open("results.txt", "r") as f:
        history = f.read()

    history_text = tk.Text(history_window, wrap=tk.WORD, font=("Arial", 12))
    history_text.insert(tk.END, history)
    history_text.configure(state="disabled")  # Chỉ cho phép đọc
    history_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Nút đóng
    tk.Button(
        history_window, text="Đóng", font=("Arial", 12), command=history_window.destroy
    ).pack(pady=5)


# Tạo giao diện
root = tk.Tk()
root.title("Máy Tính Cá Nhân")
root.geometry("420x500")  # Kích thước cửa sổ

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

# Nút Lịch sử
tk.Button(
    root,
    text="History",
    font=("Arial", 16, "bold"),
    command=show_history,
    width=10,
    height=2,
    bg="lightblue",
    fg="black",
    bd=5,
    relief="raised",
).grid(row=row + 1, column=0, columnspan=4, pady=10)

# Chạy giao diện chính
root.mainloop()
