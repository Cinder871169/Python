import numpy as np
import matplotlib.pyplot as plt

# Thiết lập tín hiệu, mức nhiễu, và ngưỡng nhiễu
original_signal = np.array([1, -1, 1, -1, -1, 1, -1, 1])  # Mã Manchester cho "HELLO!"
N_MAX = 0.5  # Giả sử N_MAX là 0.5


# Hàm kiểm tra nhiễu tác động lên tín hiệu
def add_noise(signal, noise_level):
    noise = np.random.normal(0, noise_level, len(signal))
    return noise, signal + noise


# Mô phỏng các trường hợp với nhiễu
def simulate_cases():
    cases = {}

    # Case a: N < N_MAX
    noise_a, noisy_signal_a = add_noise(original_signal, N_MAX - 0.1)
    cases["a"] = (noise_a, noisy_signal_a)

    # Case b: N > N_MAX, mã đường phát hiện lỗi
    noise_b, noisy_signal_b = add_noise(original_signal, N_MAX + 0.6)
    cases["b"] = (noise_b, noisy_signal_b)

    # Case c: N > N_MAX, mã đường không phát hiện lỗi nhưng mã kiểm soát lỗi phát hiện lỗi
    noise_c, noisy_signal_c = add_noise(original_signal, N_MAX + 0.3)
    cases["c"] = (noise_c, noisy_signal_c)

    return cases


# Vẽ sơ đồ tín hiệu cho từng trường hợp
def plot_signal_cases(cases):
    plt.figure(figsize=(12, 8))

    # Case a: N < N_MAX
    plt.subplot(3, 1, 1)
    plt.plot(
        original_signal, marker="o", linestyle="-", color="blue", label="Tín hiệu NRZ-I"
    )
    plt.plot(
        cases["a"][1], marker="o", linestyle="-", color="orange", label="Tín hiệu Nhiễu"
    )
    plt.title("Tín hiệu NRZ-I với Mức Điện Áp (Case a)")
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.legend()

    # Case b: N > N_MAX, mã đường phát hiện lỗi
    plt.subplot(3, 1, 2)
    plt.plot(
        original_signal, marker="o", linestyle="-", color="blue", label="Tín hiệu NRZ-I"
    )
    plt.plot(
        cases["b"][1], marker="o", linestyle="-", color="orange", label="Tín hiệu Nhiễu"
    )
    plt.title("Tín hiệu Nhiễu với Mức Điện Áp (Case b)")
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.legend()

    # Case c: N > N_MAX, mã đường không phát hiện lỗi nhưng mã kiểm soát lỗi phát hiện lỗi
    plt.subplot(3, 1, 3)
    plt.plot(
        original_signal, marker="o", linestyle="-", color="blue", label="Tín hiệu NRZ-I"
    )
    plt.plot(
        cases["c"][1], marker="o", linestyle="-", color="orange", label="Tín hiệu Nhiễu"
    )
    plt.title("Tổng Mức Điện Áp và Nhiễu (Case c)")
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# Chạy mô phỏng và vẽ các đồ thị tín hiệu
cases = simulate_cases()
plot_signal_cases(cases)
