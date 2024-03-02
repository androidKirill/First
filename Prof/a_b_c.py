from math import sqrt


def read_data():
    return int(input()), int(input()), int(input())


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
    elif d > 0:
        rez.append((-b + sqrt(d)) / (2 * a))
        rez.append((-b - sqrt(d)) / (2 * a))
    return rez


def main():
    a, b, c = read_data()
    res = square_eq_solver(a, b, c)
    print(res)


if __name__ == '__main__':
    main()
    # unittest.main()
