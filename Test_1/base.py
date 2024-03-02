from math import sqrt


def square_eq_solver(a, b, c):
    """Поиск решений квадратного уравнения a*x**2 + b*x + c = 0

    :param a: параметр при x**2
    :param b: параметр при x
    :param c: свободный параметр
    :return: список корней
    """

    rez = []
    d = b * b - 4 * a * c
    if d == 0:
        rez.append(-b / (2 * a))
    else:
        rez.append((-b + sqrt(d)) / (2 * a))
        rez.append((-b - sqrt(d)) / (2 * a))
    return rez
