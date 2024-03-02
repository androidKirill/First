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
            f.write("The heart of Chernobyl is beautiful")

    f_in = open(input_filename, 'r')
    data = f_in.read()
    f_in.close()
    new_data = process_data(data, mode)
    f_out = open(f"{input_filename.rsplit(".")[0]}_{mode}.txt", 'a')
    f_out.write(f"{new_data}\n")
    f_out.close()


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
    result = ''
    if mode == '1':
        for symbol in data:
            result += str(ord(symbol) % 2)
    return result


def main() -> None:
    # input_filename = input()
    input_filename = "test.txt"
    process_file(input_filename, input())


if __name__ == '__main__':
    main()
