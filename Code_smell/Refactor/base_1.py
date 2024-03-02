import math


class BaseEquationSolver:
    """
    Умеет решить линейные, квадратные и кубические уравнения

    ax+b=c
    ax^2+bx+c=d
    ax^3+bx^2+cx+d=e
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, eq_type=""):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.eq_type = eq_type
        self.result = []

    def solve(self):
        methods = {
            'linear': self.solve_linear,
            'square': self.solve_square,
            'cube': self.solve_cube,
        }
        methods[self.eq_type]()
        self.show_result()
        return self.result

    def solve_cube(self):
        x = -60
        step = 0.1
        new_d = self.d - self.e

        while x < 10 ** 6:  # BRUTEFORCE
            r = math.fabs(self.a * x ** 3 + self.b * x ** 2 + self.c * x + new_d)
            if r <= 10 ** -6:
                self.result.append(x)
            x = x + step

    def solve_square(self):
        new_c = self.c - self.d
        discriminant = self.b * self.b - 4 * self.a * new_c
        if discriminant == 0:
            self.result = [-self.b / (2 * self.a), ]
        elif discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            self.result = [x1, x2, ]
        else:
            self.result = []

    def solve_linear(self):
        self.result = [(self.c - self.b) / self.a, ]

    def show_result(self):
        print('Результат: ', len(self.result), "корней")
        for value in self.result:
            print(value, end='')
        print('')


def main():
    eq_type = input('Введите тип: ')

    if eq_type not in ['linear', 'square', 'cube']:
        print("Type Error!")
        return
    try:
        options = {}.fromkeys(["a", "b", "c", "d", "e"])
        for name in options:
            value = input(f'Введите {name}: ')
            options[name] = int(value)
        qqq = BaseEquationSolver(**options, eq_type=eq_type)
        qqq.solve()
    except ValueError:
        print("Value Error!")


if __name__ == "__main__":
    main()
