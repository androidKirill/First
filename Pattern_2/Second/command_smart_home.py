from abc import ABC, abstractmethod


# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретная команда для включения света
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


# Конкретная команда для выключения света
class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Конкретная команда для включения кондиционера
class TurnOnACCommand(Command):
    def __init__(self, air_conditioner):
        self.air_conditioner = air_conditioner

    def execute(self):
        self.air_conditioner.turn_on()


# Конкретная команда для выключения кондиционера
class TurnOffACCommand(Command):
    def __init__(self, air_conditioner):
        self.air_conditioner = air_conditioner

    def execute(self):
        self.air_conditioner.turn_off()


# Класс светильника
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")


# Класс кондиционера
class AirConditioner:
    def turn_on(self):
        print("Кондиционер включен")

    def turn_off(self):
        print("Кондиционер выключен")


# Класс пульта управления
class RemoteControl:
    def __init__(self):
        self.command_on = None
        self.command_off = None

    def set_commands(self, command_on, command_off):
        self.command_on = command_on
        self.command_off = command_off

    def press_power_button(self):
        self.command_on.execute()

    def press_power_off_button(self):
        self.command_off.execute()


# Создаем объекты устройств и команд, а также объект пульта управления
light = Light()
ac = AirConditioner()

turn_on_light_command = TurnOnLightCommand(light)
turn_off_light_command = TurnOffLightCommand(light)

turn_on_ac_command = TurnOnACCommand(ac)
turn_off_ac_command = TurnOffACCommand(ac)

remote_light = RemoteControl()
remote_light.set_commands(turn_on_light_command, turn_off_light_command)

remote_ac = RemoteControl()
remote_ac.set_commands(turn_on_ac_command, turn_off_ac_command)

# Имитируем нажатие кнопок на пультах
remote_light.press_power_button()  # Включаем свет
remote_light.press_power_off_button()  # Выключаем свет

remote_ac.press_power_button()  # Включаем кондиционер
remote_ac.press_power_off_button()  # Выключаем кондиционер
