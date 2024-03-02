# -*- coding: utf-8 -*-
# Примеры кода для autopep8

def example_function(x,y):
    result = x * 2 + y
    return result


class ExampleClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


def calculate_sum(a, b):
    return a + b


def function_with_long_arguments(argument1, argument2, argument3, argument4, argument5):
    result = argument1 + argument2 + argument3 + argument4 + argument5
    return result


long_string = "This is a very long string that exceeds the maximum string length set in PEP 8.                          "


def another_function():
    value=42
    return value


import os,sys

if True:
  print("This block of code has incorrect indentation")

def first_function():
    return "The first function"

def second_function():
    return "The second function"


def function_with_long_argument_list(
    argument1, argument2, argument3, argument4, argument5,
    argument6, argument7, argument8, argument9, argument10
):
    return argument1 * argument2 + argument3 - argument4 / argument5 + argument6 - argument7 * argument8


import os
import sys

def function_with_blank_lines():
    variable = "Example of a string"
    result = variable * 2

    return result


def yet_another_function():
    value = 10
    return value * 2


result   =   calculate_sum(3,   5)
print(result)


result = calculate_sum(3,5)
print(result)





