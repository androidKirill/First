class MemoryPage:
    PAGE_SIZE = 1024

    def __init__(self):
        self.data = [0] * self.PAGE_SIZE

    def reset(self):
        for i in range(len(self.data)):
            self.data[i] = 0


class RAM:  # Пул объектов
    MAX_OBJECTS = 1000
    __instance = None

    def __new__(cls, *args, **kwargs):  # реализация singleton
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.object = [MemoryPage() for i in range(self.MAX_OBJECTS)]

    def acquire(self):
        return self.object.pop()

    def release(self, reusable):
        # этой памятью попользовался,
        # она мне больше не нужна
        # освобождаем её
        reusable.reset()
        self.object.append(reusable)


def main():
    r1 = RAM()
    r2 = RAM()
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
