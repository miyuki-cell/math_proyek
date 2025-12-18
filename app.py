import numpy as np
import matplotlib.pyplot as plt

print("PROGRAM VISUALISASI INTEGRAL TENTU")
print("Contoh fungsi: x**2 + 2*x + 1")

fungsi_input = input("Masukkan fungsi f(x): ")
a = float(input("Masukkan batas bawah a: "))
b = float(input("Masukkan batas atas b: "))

def f(x):
    return eval(fungsi_input)

n = 1000
x = np.linspace(a, b, n)
y = f(x)

dx = (b - a) / n
integral = np.sum((y[:-1] + y[1:]) / 2) * dx

print("\nHasil perhitungan:")
print(f"Nilai integral dari {a} sampai {b} adalah: {integral}")

plt.plot(x, y, label="f(x)")
plt.fill_between(x, y, alpha=0.3)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Visualisasi Integral sebagai Luas Daerah di Bawah Kurva")
plt.legend()
plt.show()
