import math

def f(t, u):
    return math.sin(u)

def stormer_method(t0, u0, v0, T, h):
    t = t0
    u = u0
    v = v0

    n = int(T / h)  # Количество шагов

    for i in range(2, n+1):
        t_prev = t
        u_prev = u
        v_prev = v

        t = i * h

        # Вычисление нового значения u
        u = (12 * h**2 * f(t_prev, u_prev) - v_prev * h - 12 * u_prev) / (-10)

        # Вычисление нового значения v
        v = (-2 * v_prev + 13 * f(t, u) * h + 10 * f(t_prev, u_prev) * h) / 12

        print(f"t = {t:.2f}, u = {u:.6f}")

    return t, u

# Параметры задачи
t0 = 0.0  # Начальное время
u0 = 1.0  # Начальное значение u
v0 = 0.0  # Начальное значение v
T = 4 * math.pi  # Конечное время
h = 0.1  # Шаг интегрирования

# Решение задачи
t, u = stormer_method(t0, u0, v0, T, h)

print(f"\nРешение при t = {t:.2f}: u = {u:.6f}")