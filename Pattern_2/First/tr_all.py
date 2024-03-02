'''
Работа светофора для водителей запрограммирована следующим образом: начиная с начала каждого часа, в течение трёх минут горит зелёный сигнал, затем в течение одной минуты — жёлтый, в течение двух минут — красный, в течение трёх минут — опять зелёный и т.д.

Дано число t, означающее время в минутах, прошедшее с начала очередного часа. Определите, сигнал какого цвета горит для водителей в этот момент.

Доп. условие: состояния и секции могут часто меняться - в этом варианте они как раз добавлены.
'''
from abc import ABC


# --- State design pattern implementation ---

class BaseState(ABC):
    state_data = []

    def set_context(self, context):
        for i in range(len(context)):
            context[i].set_enabled(self.state_data[i])


class RedState(BaseState):
    def __init__(self):
        self.state_data = [1, 0, 0, 0]


class YellowState(BaseState):
    def __init__(self):
        self.state_data = [0, 1, 0, 0]


class GreenState(BaseState):
    def __init__(self):
        self.state_data = [0, 0, 1, 0]


class GreenArrowState(BaseState):
    def __init__(self):
        self.state_data = [0, 0, 1, 1]


class RedYellowState(BaseState):
    def __init__(self):
        self.state_data = [1, 1, 0, 0]


# --- State design pattern implementation end ---

# --- State switcher classes: storage and state machine implementation ---

class SortedDataStorage:
    def __init__(self, data):
        self.data = data
        data.sort(key=lambda item: item[0])

    def get_lower_of_equal(self, key):  # todo: migrate to binary search
        i = 0
        while i < len(self.data) and self.data[i][0] <= key:
            i += 1
        return self.data[i - 1][1]


class StateChanger:
    __change_data = SortedDataStorage(
        [
            [0, GreenState],
            [1, GreenArrowState],
            [3, YellowState],
            [4, RedState],
            [5, RedYellowState],
        ]
    )

    @staticmethod
    def get_state_by_time(time):
        return StateChanger.__change_data.get_lower_of_equal(time % 6)


# --- State switcher classes: storage and state machine implementation end ---

# --- Task classes ---
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
            Section('RED'),
            Section('YELLOW'),
            Section('GREEN'),
            Section('GREEN_ARROW'),
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
        return '-'.join([str(state) for state in self.sections if state.enabled])


# --- Task classes end ---


if __name__ == '__main__':
    tr = TrafficLight()
    t = int(input())
    tr.past_time(t)
    print(tr)
