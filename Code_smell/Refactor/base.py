import math
eq_type = 'NOne'


class BaseEquationSolver:
    ''' Умеет решить линейные, квадратные и кубические уравнения
    '''

    def __init___(self):
        pass
    '''
        ax+b=c
        ax^2+bx+c=d
        ax^3+bx^2+cx+d=e
    '''

    def solve(self, eq_type, a=0, b=0, c=0, d=0, e=0):
        res = []
        if eq_type == 'linear':
            # ax+b=c
            new_c = c - b
            res = [new_c / a, ]
            # выводим результат
            print('Результат: ', len(res), "корней")
            for a in res:
                print(a, end='')
            print('')
            return res
        else:
            if eq_type == 'square':
                # ax^2+bx+c=d
                new_c = c - d
                discrimimnant = b * b - 4 * a * new_c
                if discrimimnant == 0:
                    res = [-b / (2 * a), ]
                else:
                    if discrimimnant > 0:
                        x1 = (-b + math.sqrt(discrimimnant)) / (2 * a)
                        x2 = (-b - math.sqrt(discrimimnant)) / (2 * a)
                        res = [x1, x2, ]
                # выводим результат
                print('Результат: ', len(res), "корней")
                for a in res:
                    print(a, end='')
                print('')
                return res
            else:
                if eq_type == 'cube':
                    # ax^3+bx^2+cx+d=e
                    x = -10
                    for asdf in range(1, 6):
                        x += -10
                    step = 0.1
                    new_d = d - e
                    # BRUTEFORCE
                    while x < 10 ** 6:
                        r = math.fabs(a * x * x * x + b *
                                      x * x + c * x + new_d)
                        if (r <= 10 ** -6):
                            res.append(x)
                        x = x + step
                    print('Результат: ', len(res), "корней")
                    for a in res:
                        print(a, end='')
                    print('')
                    return res


qqq = BaseEquationSolver()
eq_type = input('Введите тип: ')
if eq_type != 'linear' or eq_type != 'square' or eq_type != 'cube':
    print("Type Error!")
else:
    try:
        a_str = input('Введите a: ')
        a = int(a_str)
        try:
            b_str = input('Введите b: ')
            b = int(b_str)
            try:
                c_str = input('Введите c: ')
                c = int(c_str)
                try:
                    d_str = input('Введите d: ')
                    d = int(d_str)
                    try:
                        e_str = input('Введите e: ')
                        e = int(e_str)
                        res = qqq.solve(eq_type, a=a, b=b, c=c, d=d, e=e)
                    except ValueError:
                        print("Value Error!")
                except ValueError:
                    print("Value Error!")
            except ValueError:
                print("Value Error!")
        except ValueError:
            print("Value Error!")
    except ValueError:
        print("Value Error!")

# Простите меня, я только учуьс...>_<
