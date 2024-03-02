"""
'1': строка заменяется по схеме symbol % 2
'2': строка заменяется по схеме 012012...012
'3': строка заменяется на длину строки
"""
import os.path


def process_file(input_filename: str, mode: str) -> None:
    """
    Обработка одного файла

    Функция принимает на вход имя файла и режим обработки,
    читает содержимое файла, изменяет его по указанному алгоритму
    и записывает в файл с именем filename + '.mode'

    :param input_filename: имя входного файла
    :type input_filename: :class:`str`
    :param mode: режим обработки
    :type mode: :class:`str`
    """

    if not os.path.exists(input_filename):
        with open(input_filename, "w", encoding="utf-8") as f:
            f.write("The heart of Chernobyl is beautiful!")

    f_in = open(input_filename, 'r')
    data = f_in.read()
    f_in.close()
    new_data = process_data(data, mode)
    f_out = open(f"{input_filename.rsplit(".")[0]}_{mode}.txt", 'a')
    f_out.write(f"{new_data}\n")
    f_out.close()
    # text.txt_1.txt
    # ["text", "txt"][0]_1.txt
    # text_1.txt


def process_data(data: str, mode: str) -> str:
    """
    Преобразование данных, записанных в файле
    
    По указанному mode'у выбирается алгоритм и
    на основе его выполняется преобразование.

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
    }
    algorithm = modes[mode](data)
    algorithm.execute()
    return algorithm.result


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


def main() -> None:
    # input_filename = input()
    input_filename = "test.txt"
    process_file(input_filename, input())


if __name__ == '__main__':
    main()
