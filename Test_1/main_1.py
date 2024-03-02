from math import sqrt
import unittest


class SquareEqSolverTestCase(unittest.TestCase):
    def test_simple(self):
        """
        x ** 2 = 4
        :return:
        """
        estimated_result = [2.0, -2.0]
        real_result = square_eq_solver(1, 0, -4)
        self.assertEqual(real_result, estimated_result)

    def test_no_roots(self):
        estimated_result = []
        real_result = square_eq_solver(10, 1, 10)
        self.assertEqual(real_result, estimated_result)

    def test_invalid_args(self):
        # estimated_result = []
        # real_result = square_eq_solver("-1", "ку-ку", 12)
        # self.assertEqual(real_result, estimated_result)
        self.assertRaises(ValueError, square_eq_solver, "-1", "ку-ку", 12)

    def test_not_exists(self):
        self.assertRaises(RuntimeError, square_eq_solver, 0, 0, 0)

    def test_normal(self):
        estimated_result = [2.0]
        real_result = square_eq_solver(1, -4, 4)
        self.assertEqual(len(real_result), 1)
        self.assertEqual(real_result, estimated_result)


def square_eq_solver(a, b, c):
    """Поиск решений квадратного уравнения a*x**2 + b*x + c = 0

    :param a: параметр при x**2
    :param b: параметр при x
    :param c: свободный параметр
    :return: список корней
    """

    # if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
    #     return []
    a, b, c = map(int, [a, b, c])
    check_type(int, a, b, c)

    if a == b == c == 0:
        raise RuntimeError("Such an equation does not exist.")

    rez = []
    d = b * b - 4 * a * c
    if d == 0:
        rez.append(-b / (2 * a))
    elif d > 0:
        rez.append((-b + sqrt(d)) / (2 * a))
        rez.append((-b - sqrt(d)) / (2 * a))
    return rez


def check_type(type_check, *args):
    for i in args:
        if not isinstance(i, type_check):
            raise ValueError


if __name__ == '__main__':
    a, b, c = input().split()
    res = square_eq_solver(a, b, c)
    print(res)
    # unittest.main()
