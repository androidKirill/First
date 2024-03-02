class BaseState:
    state_data = []

    def set_context(self, context):
        for i in range(len(context)):
            context[i].set_enabled(self.state_data[i])


class RedState(BaseState):
    def __init__(self):
        self.state_data = [1, 0, 0]


class YellowState(BaseState):
    def __init__(self):
        self.state_data = [0, 1, 0]


class GreenState(BaseState):
    def __init__(self):
        self.state_data = [0, 0, 1]


class SortedDataStorage:
    def __init__(self, data):
        self.data = data
        data.sort()

    def get_lower_of_equal(self, key):
        i = 0
        while i < len(self.data) and self.data[i][0] <= key:
            i += 1
        return self.data[i - 1][1]


class StateChanger:
    __change_data = SortedDataStorage([
        [0, GreenState],
        [3, YellowState],
        [4, RedState],
    ])

    @staticmethod
    def get_state_by_time(time):
        return StateChanger.__change_data.get_lower_of_equal(time % 6)


class Section:
    color = None

    def __init__(self, color):
        self.color = color
        self.enabled = False

    def set_enabled(self, value):
        self.enabled = bool(value)

    def __str__(self):
        return self.color if self.enabled else None


class TrafficLight:
    def __init__(self):
        self.sections = [
            Section("RED"),
            Section("YELLOW"),
            Section("GREEN"),
        ]
        self.time = 0
        self.state = None
        self.__set_state()

    def __set_state(self):
        self.state = StateChanger.get_state_by_time(self.time)()
        self.state.set_context(self.sections)

    def past_time(self, time):
        self.time += time
        self.__set_state()

    def __str__(self):
        return "-".join([str(state) for state in self.sections if state.enabled])


def main():
    tr = TrafficLight()
    t = int(input())
    tr.past_time(t)
    print(tr)


if __name__ == "__main__":
    main()
