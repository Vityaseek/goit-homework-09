import sys
from collections import defaultdict

contact = defaultdict()
lst_bey = ["good bye", "close", "exit"]


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Please write Name and Phone, though a space"
    return inner


def unknown_command(*args):
    return "Unknown command"


def phones(*args):
    if len(args) > 1:
        return "Please write only username"
    return contact[args[0]]


def show():
    string = ''
    x = ''
    for i, c in contact.items():
        for p in c:
            string = f"{i}: {p}"
            x += string + '\n'
            string = ""
    return x.strip('\n')


@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    if name and phone:
        contact[name] = [phone]

    return "Add success"


def hello(*args):
    return "How can i help you?"


@input_error
def change(*args):
    contact[args[0]] = args[1]
    return "Change success"


def parser_text(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith('add'):
        return add, text.replace("add", ' ').strip().split()
    elif text.startswith('hello'):
        return hello, text
    elif text.startswith('change'):
        return change, text.replace('change', ' ').strip().split()
    elif text.startswith('phone'):
        return phones, text.replace('phone', ' ').strip().split()
    elif text.startswith('show all'):
        return show, text.replace('show all', ' ').strip().split()
    return unknown_command, text


def main():
    while True:
        user_input = input(">>>").casefold()
        if user_input in lst_bey:
            print("Good bye!")
            break
        command, data = parser_text(user_input)
        result = command(*data)
        print(result)


if __name__ == "__main__":
    main()
