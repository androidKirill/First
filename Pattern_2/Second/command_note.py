from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class InsertCommand(Command):
    def __init__(self, editor, text, position):
        self.editor = editor
        self.text = text
        self.position = position
        self.previous_text = None

    def execute(self):
        self.previous_text = self.editor.get_text()
        self.editor.insert_text(self.text, self.position)

    def undo(self):
        self.editor.set_text(self.previous_text)


class DeleteCommand(Command):
    def __init__(self, editor, position, length):
        self.editor = editor
        self.position = position
        self.length = length
        self.deleted_text = None

    def execute(self):
        self.deleted_text = self.editor.get_text(
        )[self.position:self.position + self.length]
        self.editor.delete_text(self.position, self.length)

    def undo(self):
        self.editor.insert_text(self.deleted_text, self.position)


class TextEditor:
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def insert_text(self, text, position):
        self.text = self.text[:position] + text + self.text[position:]

    def delete_text(self, position, length):
        self.text = self.text[:position] + self.text[position + length:]


class Invoker:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()


editor = TextEditor()
invoker = Invoker()

insert_command = InsertCommand(editor, "Hello, ", 3)
invoker.execute_command(insert_command)
print("Текст после вставки:", editor.get_text())

insert_command = InsertCommand(editor, "Hello, ", 3)
invoker.execute_command(insert_command)
print("Текст после вставки:", editor.get_text())

delete_command = DeleteCommand(editor, 0, 7)
invoker.execute_command(delete_command)
print("Текст после удаления:", editor.get_text())

print(invoker.commands)
invoker.undo_last_command()
print("Текст после отмены:", editor.get_text())
invoker.undo_last_command()
print("Текст после отмены:", editor.get_text())
print(invoker.commands)
