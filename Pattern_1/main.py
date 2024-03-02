"""
'1': строка заменяется по схеме symbol % 2
'2': строка заменяется по схеме 012012...012
'3': строка заменяется на длину строки
'in': к каждому слову добавляется 'in'
'number': каждое слово заменяется на сумму цифр, присутствующих в этом слове
'analytics': в начало добавляется длина строки.
             В середину добавляется количество слов.
             В конец добавляется средняя длина слова.
"""


def process_file(input_filename: str, mode: str) -> None:
    """
    Обработка одного файла

    Функция принимает на вход имя файла и режим обработки, читает содержимое файла, изменяет его по указанному алгоритму
    и записывает в файл с именем filename + '.mode'
    :param input_filename: имя входного файла
    :type input_filename: :class:`str`
    :param mode: режим обработки
    :type mode: :class:`str`
    """
    f_in = open(input_filename, 'r')
    data = f_in.read()
    f_in.close()
    new_data = process_data(data, mode)
    f_out = open(f"{input_filename}_{mode}.txt," 'w')
    f_out.write(new_data)
    f_out.close()


class BaseAlgo:
    def __init__(self, data):
        self.data = data
        self.result = ""

    def execute(self):
        raise NotImplementedError


class Algo1(BaseAlgo):
    def execute(self):
        for symbol in self.data:
            self.result += str(ord(symbol) % 2)


class Algo2(BaseAlgo):
    def execute(self):
        i = 0
        for _ in self.data:
            self.result += str(i)
            i = (i + 1) % 3


class Algo3(BaseAlgo):
    def execute(self):
        self.result = str(len(self.data))


class AlgoIn(BaseAlgo):
    def execute(self):
        words = self.data.split()
        words = [word + 'in' for word in words]
        self.result = ' '.join(words)


class AlgoNumber(BaseAlgo):
    def execute(self):
        words = self.data.split()
        nums = []
        for word in words:
            num = 0
            for symbol in word:
                if symbol.isnumeric():
                    num += int(symbol)
            nums.append(num)
        nums = [str(num) for num in nums]
        self.result = ' '.join(nums)


class AlgoAnalytic(BaseAlgo):
    def execute(self):
        self.result = self.data[:]
        self.result = str(len(self.data)) + self.result
        self.result = self.result[:len(self.result) // 2 + 1] \
            + str(len(self.data.split())) + \
            self.result[len(self.result) // 2 + 1:]
        avg = 0
        for word in self.data.split():
            avg += len(word)
        avg /= len(self.data.split())
        self.result += str(avg)


def process_data(data: str, mode: str) -> str:
    """
    Преобразование данных, записанных в файле

    По указанному mode'у выбирается алгоритм и на основе его выполняется преобразование.
    :param data: входные данные
    :type data: :class:`str`
    :param mode: режим работы
    :type mode: :class:`str`
    :return: преобразованные данные
    :rtype: :class:`str`
    """

    modes = {
        '1': Algo1,
        '2': Algo2,
        '3': Algo3,
        'in': AlgoIn,
        'number': AlgoNumber,
        'analitytic': AlgoAnalytic,
    }

    algorithm = modes[mode](data)
    algorithm.execute()
    return algorithm.result


def main() -> None:
    DEBUG = True
    if DEBUG:
        input_filename = 'data.txt'
        mode = 'number'
    else:
        input_filename = input()
        mode = input()
    process_file(input_filename, mode)


if __name__ == '__main__':
    main()
