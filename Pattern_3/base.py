# В классе учатся n учеников. Известен рост каждого из них в сантиметрах.
# Рост мальчиков по условию задан отрицательными числами.
# Определите средний рост мальчиков и средний рост девочек.
class HeightModel:
    def __init__(self):
        self.men_heights = []
        self.women_heights = []

    def add_men_heights(self, height):
        self.men_heights.append(height)

    def add_women_heights(self, height):
        self.women_heights.append(height)

    @staticmethod
    def get_avg(data):
        return sum(data) / len(data)


class HeightController:
    def __init__(self, a: HeightModel):
        self.model = a

    def append_value(self, value):
        if value > 0:
            self.model.women_heights.append(value)
        elif value < 0:
            self.model.men_heights.append(-value)


class HeightView:
    def __init__(self, m: HeightModel, c: HeightController):
        self.model = m
        self.controller = c
        self.n = 0

    def run(self):
        self.read_values_count()
        self.read_data()
        self.show_answer()

    def read_values_count(self):
        self.n = int(input())

    def read_data(self):
        for _ in range(self.n):
            value = int(input())
            self.controller.append_value(value)

    def show_answer(self):
        result_m = int(self.model.get_avg(self.model.men_heights))
        result_w = int(self.model.get_avg(self.model.women_heights))
        return result_m, result_w


if __name__ == "__main__":
    model = HeightModel()
    controller = HeightController(model)
    view = HeightView(model, controller)
    print(view.run())
