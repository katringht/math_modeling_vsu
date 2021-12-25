from create_sampling import *
from graphs_points import histogram, polygon
from ploting import plot_histogram, plot_polygon, plot_hist_polygon
from math_utils import *
from sampling_value import *

def modeling():
    print("1- MOF\n2-Gauss\n3-Rayleigh")
    request = str(input("Enter a value: "))
    if request == "1": 
        a = int(input("Введите начальное значение интервала:: "))
        b = int(input("Введите конечное знаение интервала: "))

        x, interval = normal_sampling(a, b)
        data_hist_normal, k_normal = histogram(x, interval)
        data_polygon_normal, _ = polygon(x, interval)

        plot_histogram(x, data_hist_normal, k_normal, interval, "Равномерное распределение(Гистограмма)", 1)
        plot_polygon(x, data_polygon_normal, interval, "Равномерное распределение(Полигон)", 1)

        mn = find_mathematical_expectation(x)
        matO = (b + a) / 2
        print("Математическое ожидание равномерного распределения: ", matO)
        print("Дисперсия равномерного распределения", (b - a) ** 2 / 12)
        print("Выборочное математическое ожидание равномерного распределения: ", mn)
        print("Выборочная дисперсия равномерного распределения c известным Мат.Ожидание", find_dispersion(x, matO))
        print("Выборочная дисперсия равномерного распределения c неизвестным Мат.Ожидание", find_dispersion(x, mn))

    if request == "2":

        matO = float(input("Введите мат ожидание для распределения Гаусса: "))  
        d = float(input("Введите дисперсию для распределения Гаусса: "))
        x, interval = create_gauss_sampling(matO, d)
        data_hist_gauss, k = histogram(x, interval)
        data_polygon_gauss, _ = polygon(x, interval)

        plot_histogram(x, data_hist_gauss, k, interval, "Распределение Гаусса(Гистограмма)", 2, m=matO, d=d)
        plot_polygon(x, data_polygon_gauss, interval, "Распределение Гаусса(Полигон)", 2, m=matO, d=d)

        print("Математчисекое ожидание распределения Гаусса: ", matO)
        print("Дисперсия распределения Гаусса: ", d)
        mv = find_mathematical_expectation(x)
        print("Выборочное математическое ожидание распределения Гаусса: ", mv)
        print("Выборочная дисперсия c известным МО распределения Гаусса: ", find_dispersion(x, matO))
        print("Выборочная дисперсия c неизвестным МО распределения Гаусса: ", find_dispersion(x, mv))

    if request == "3":
        sigma = float(input("Введите сигму для релеевского закона: "))
        x_neumann, interval_neumann = create_rayleigh_sampling(sigma, 4)
        data_hist_neumann, k_neumann = histogram(x_neumann, interval_neumann)
        data_polygon_neumann, _ = polygon(x_neumann, interval_neumann)

        plot_histogram(x_neumann, data_hist_neumann, k_neumann, interval_neumann, "Распределение Реле(Гистограмма)", 3,
                    sigma=sigma)
        plot_polygon(x_neumann, data_polygon_neumann, interval_neumann, "Распределение Реле(Полигон)", 3,
                    sigma=sigma)

        m_ne = math.sqrt((math.pi * (sigma ** 2)) / 2)
        print("Математическое ожидание распрееделение Рэле: ", m_ne)
        print("Дисперсия распределения Рэле: ", (2 - math.pi / 2) * (sigma ** 2))
        mk = find_mathematical_expectation(x_neumann)
        print("Выборочное математическое ожидание распределения Рэле: ", mk)
        print("Выборочная дисперсия распределения Рэле с известным Мат.Ожидание: ", find_dispersion(x_neumann, m_ne))
        print("Выборочная дисперсия распределения Рэле с неизвестным Мат.Ожидание: ", find_dispersion(x_neumann, mk))

modeling()
