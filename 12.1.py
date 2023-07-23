import numpy as np

def rk4_step(f, t, x, h):
    """Один шаг метода Рунге-Кутта 4-го порядка"""
    k1 = f(t, x)
    k2 = f(t + h/2, x + h/2*k1)
    k3 = f(t + h/2, x + h/2*k2)
    k4 = f(t + h, x + h*k3)
    return x + h/6*(k1 + 2*k2 + 2*k3 + k4)

def solve_ivp(f, t_span, x0, tol=1e-6, h0=1e-3):
    """Решение задачи Коши для системы ОДУ методом Рунге-Кутта 4-го порядка
    с адаптивным шагом"""
    t0, tf = t_span
    t = [t0]
    x = [x0]
    h = [h0]
    while t[-1] < tf:
        # Вычисляем два шага с h и один шаг с h/2
        x1 = rk4_step(f, t[-1], x[-1], h[-1])
        x11 = rk4_step(f, t[-1], x[-1], h[-1]/2)
        x12 = rk4_step(f, t[-1] + h[-1]/2, x11, h[-1]/2)
        # Вычисляем оценку погрешности
        e = np.linalg.norm(x1 - x12) / 15
        # Вычисляем новый шаг по формуле из задания
        h_new = 0.9 * h[-1] * (tol / e) ** (1/4)
        # Добавляем новые значения
        if h_new > h[-1]:
            t.append(t[-1] + h[-1])
            x.append(x1)
            h.append(h_new)
        else:
            h_new = h[-1] / 2
            continue
    return np.array(t), np.array(x)
