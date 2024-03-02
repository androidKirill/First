class JustExample:
    def __init__(self):
        self.value = 42


# Без шаблона
class SimpleSingletonExample:
    __instance = None

    def __init__(self):
        if SimpleSingletonExample.__instance is None:
            self.value = 55
            SimpleSingletonExample.__instance = self
        else:
            raise RuntimeError

    @staticmethod
    def get_instance():
        if SimpleSingletonExample.__instance is None:
            SimpleSingletonExample()
        return SimpleSingletonExample.__instance


# C шаблоном
class SingletonPythonStyle:
    __instance = None

    def __init__(self):
        self.value = 55

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


def main():
    test_1 = JustExample()
    test_2 = JustExample()
    print(id(test_1))
    print(id(test_2))
    print(test_1.value)
    print(test_2.value)

    # -----------------
    test_3 = SimpleSingletonExample.get_instance()
    test_4 = SimpleSingletonExample.get_instance()
    print(id(test_3))
    print(id(test_4))
    print(test_3.value)
    print(test_4.value)

    # -----------------
    test_5 = SingletonPythonStyle()
    test_6 = SingletonPythonStyle()
    print(id(test_5))
    print(id(test_6))
    print(test_5.value)
    print(test_6.value)


if __name__ == "__main__":
    main()
