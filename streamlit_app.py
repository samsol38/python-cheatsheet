import io
import contextlib
import streamlit as st
from code_editor import code_editor
from typing import Dict
from streamlit_option_menu import option_menu


@st.cache_data
def get_py_code_config():
    return [
        # Variables
        {
            "key": "variables",
            "py_code_config": [
                {
                    "title": "Variables",
                    "py_can_run": True,
                    "code": """name = "John"
age = 25
is_active = True
price = 99.99
items = []
user = {"id": 1, "name": "John"}

print(f"name: {name}")
print(f"age: {age}")
print(f"is_active: {is_active}")
print(f"price: {price}")
print(f"items: {items}")
print(f"user: {user}")""",
                },
                {
                    "title": "Type Hints (Optional in Python)",
                    "py_can_run": True,
                    "code": """name: str = "John"
age: int = 25
is_active: bool = True
price: float = 99.99
items: list[str] = []
user: dict[str, str | int] = {"id": 1, "name": "John"}

print(f"name: {name}")
print(f"age: {age}")
print(f"is_active: {is_active}")
print(f"price: {price}")
print(f"items: {items}")
print(f"user: {user}")""",
                },
                {
                    "title": "Reassignment",
                    "py_can_run": True,
                    "code": """count = 1
count = 2   # allowed
pi = 3.14
pi = 3.15   # allowed

print(f"count: {count}")
print(f"pi: {pi}")""",
                },
            ],
            "py_notes": """- Naming Conventions
    - snake_case for variables and functions
    - PascalCase for classes
    - UPPER_CASE for constants
    - _ is allowed, no $
    - Cannot start with a number
---
- Examples
    - user_name, get_data), UserService, MAX_SIZE""",
        },
        # Data Types
        {
            "key": "data_types",
            "py_code_config": [
                {
                    "title": "int / float",
                    "desc": "Python has separate int (arbitrary precision) and float (double precision).",
                    "py_can_run": True,
                    "code": """int_num: int = 42    # int
float_num: float = 3.14     # float
hex_val: int = 0xff     # int
exp_val: float = 1e5     # 100000.0

print(f"int_num: {int_num}")
print(f"float_num: {float_num}")
print(f"hex_val: {hex_val}")
print(f"exp_val: {exp_val}")""",
                },
                {
                    "title": "str (String)",
                    "desc": "Sequence of Unicode characters.\nUse single, double, or triple quotes.",
                    "py_can_run": True,
                    "code": """s1: str = "Hello"
s2: str = 'John'
s3: str = f"Hello, {s2}"

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")""",
                },
                {
                    "title": "bool (Boolean)",
                    "desc": "Represents True or False (capitalized).",
                    "py_can_run": True,
                    "code": """is_active: bool = True
is_done: bool = False

print(f"is_active: {is_active}")
print(f"is_done: {is_done}")""",
                },
                {
                    "title": "None Type",
                    "desc": "Represents absence of value.",
                    "py_can_run": True,
                    "code": """n = None
print(f"n: {n}")""",
                },
                {
                    "title": "list (List)",
                    "desc": "Ordered list. Can hold mixed types.",
                    "py_can_run": True,
                    "code": """arr: list[int | str | bool | None] = [1, "two", True, None]
nums: list[int] = [1, 2, 3]

print(f"arr: {arr}")
print(f"nums: {nums}")""",
                },
                {
                    "title": "dict (Dictionary)",
                    "desc": "Key-value pairs. Keys can be any immutable type.",
                    "py_can_run": True,
                    "code": """obj = {
    "name": "John",
    "age": 25,
    "is_active": True
}

data = {}
data["id"] = 1
data["name"] = "Sam"

print(f"obj: {obj}")
print(f"data: {data}")""",
                },
                {
                    "title": "set (Set)",
                    "desc": "Collection of unique values.",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3}
s.add(4)
s.add(2)

print(f"s: {s}")""",
                },
            ],
        },
        # Output & Comments
        {
            "key": "output_comments",
            "py_code_config": [
                {
                    "title": "Output / Print to Console",
                    "py_can_run": True,
                    "code": """print("Hello, World!")
print(42)
print(True)
print({"name": "John"})
print("Price: ", 99.99)""",
                },
                {
                    "title": "Single-line Comments",
                    "py_can_run": True,
                    "code": """# This is a single-line comment
x = 10      # Comment after code
print(f"x: {x}")""",
                },
                {
                    "title": "Multi-line / Block Comments",
                    "py_can_run": True,
                    "code": """\"""
    This is a multi-line comment
    that can span multiple lines.
    Useful for documentation.
\"""
                
y = 20
print(f"y: {y}")""",
                },
                {
                    "title": "Commenting Out Code",
                    "py_can_run": True,
                    "code": """# print("This won't run")
#  z = 30
print("This will run")""",
                },
                {
                    "title": "String with Variables (Output)",
                    "py_can_run": True,
                    "code": """name: str = "John"
age = 25
print(f\"""My name is {name}.
I am {age} years old.\""")""",
                },
            ],
        },
        # Operators
        {
            "key": "operators",
            "py_code_config": [
                {
                    "title": "Arithmetic Operators",
                    "py_can_run": True,
                    "code": """a = 5
b = 3

print(f"a : {a}")
print(f"b : {b}")

# 8
print(f"a + b : {a + b}")

# 2
print(f"a - b : {a - b}")

# 15
print(f"a * b : {a * b}")

# 1.6666 (float division)
print(f"a / b : {a / b}")

# 1 (floor division)
print(f"a // b : {a // b}")

# 2 (remainder)
print(f"a % b : {a % b}")

# 125 (exponent)
print(f"a ** b : {a ** b}")

#   No ++ or -- operators
#   Use: x += 1 or x -= 1""",
                },
                {
                    "title": "Comparison Operators",
                    "py_can_run": True,
                    "code": """x = 5

print(f"x : {x}")
                
# True
print(f"x == 5 : {x == 5}")

# False
print(f"x != 5 : {x != 5}")

# False (different types)
print(f"x == '5' : {x == '5'}")

# True
print(f"x != 3 : {x != 3}")

# True
print(f"x > 3 : {x > 3}")

# False
print(f"x < 3 : {x < 3}")

# True
print(f"x >= 5 : {x >= 5}")

# True
print(f"x <= 3 : {x <= 3}")""",
                },
                {
                    "title": "Logical Operators",
                    "py_can_run": True,
                    "code": """# False
print(f"True and False: {True and False}")

# True
print(f"True and True: {True and True}")

# False
print(f"False and False: {False and False}")

# True
print(f"True or False: {True or False}")

# True
print(f"True or True: {True or True}")

# False
print(f"False or False: {False or False}")

# False
print(f"not True: {not True}")

# True
print(f"not False: {not False}")""",
                },
                {
                    "title": "Assignment Operators",
                    "py_can_run": True,
                    "code": """x = 5
print(f"x: {x}")

x += 2
print(f"x += 2: {x}")

x -= 1
print(f"x -= 1: {x}")

x *= 3
print(f"x *= 3: {x}")

x /= 2
print(f"x /= 2: {x}")

x %= 4
print(f"x %= 4: {x}")

x **= 2
print(f"x **= 2: {x}")""",
                },
                {
                    "title": "Membership Operators",
                    "py_can_run": True,
                    "code": """print(f"'a' is 'apple': {'a' is 'apple'}")
                
print(f"'z' is 'apple': {'z' is 'apple'}")

print(f"3 in [1, 2, 3]: {3 in [1, 2, 3]}")

print(f"'id' in {{}}: {'id' in {}}")""",
                },
                {
                    "title": "Bitwise Operators",
                    "py_can_run": True,
                    "code": """a = 5
b = 1

print(f"a : {a}")
print(f"b : {b}")

# 1 (AND)
print(f"a & b : {a & b}")

# 5 (OR)
print(f"a | b : {a | b}")

# 4 (XOR)
print(f"a ^ b : {a ^ b}")

# -6 (NOT)
print(f"~a : {~a}")

# 10 (left shift)
print(f"a << b : {a << b}")

# 2 (right shift)
print(f"a >> b : {a >> b}")""",
                },
            ],
        },
        # Control Flow
        {
            "key": "control_flow",
            "py_code_config": [
                {
                    "title": "If Statement",
                    "py_can_run": True,
                    "code": """x: int = 5;
if x > 5:
    print("x is greater")
elif x == 5:
    print("x is equal")
else:
    print("x is smaller")""",
                },
                {
                    "title": "For Loop",
                    "py_can_run": True,
                    "code": """for i in range(5):
    print(i)""",
                },
                {
                    "title": "While Loop",
                    "py_can_run": True,
                    "code": """count: int = 0
while count < 5:
    print(count)
    count += 1""",
                },
                {
                    "title": "Function / Block Example",
                    "py_can_run": True,
                    "code": """def add(a: int, b: int):
    result: int = a + b
    return result

answer = add(2, 3)
print(f"answer: {answer}")""",
                },
                {
                    "title": "Continue",
                    "py_can_run": True,
                    "code": """for i in range(8):
    if i == 3 or i == 5:
        continue
    print(i)""",
                },
                {
                    "title": "Break",
                    "py_can_run": True,
                    "code": """for i in range(10):
    if i == 4:
        break
    print(i)""",
                },
            ],
        },
        # Import Modules
        {
            "key": "import_modules",
            "py_code_config": [
                {
                    "title": "Import Entire Module",
                    "py_can_run": True,
                    "notes": "All functions/attributes are accessed with the module name (math.sqrt, math.pi, etc.).",
                    "code": """import math

# 4
print(f"math.sqrt(16): {math.sqrt(16)}")""",
                },
                {
                    "title": "Import Specific Items",
                    "notes": "Import specific functions/variables from a module.",
                    "py_can_run": True,
                    "code": """from math import sqrt, pi

# 4
print(f"sqrt(16): {sqrt(16)}")

# 3.141592653589793
print(f"pi: {pi}")""",
                },
                {
                    "title": "No Default Export (Use Direct Import)",
                    "notes": "Python does not have default export. Import the function/class directly.",
                    "py_can_run": False,
                    "code": """# math_utils.py
def add(a: int, b: int):
    return a + b

# ---------------

# main.py
from math.utils import add
print(add(2, 3)) # 5""",
                },
                {
                    "title": "Renaming Imports (Alias)",
                    "notes": "Use 'as' to create an alias.",
                    "py_can_run": False,
                    "code": """import numpy as np
from pandas import DataFrame as DF""",
                },
                {
                    "title": "Import Multiple Modules",
                    "notes": "Each import in its own line (PEP 8 recommended).",
                    "py_can_run": False,
                    "code": """import os
import sys
from datetime import datetime""",
                },
                {
                    "title": "Export in Python (Make Available)",
                    "notes": "All top-level names are accessible when imported.",
                    "py_can_run": False,
                    "code": """# math_utils.py
PI = 3.14159

def area(r: float):
    return PI * r * r

# Everything defined in the file is available
# when imported (no export keypord needed)""",
                },
                {
                    "title": "__init__.py (Package Exports)",
                    "notes": "Expose modules / classes at the package level.",
                    "py_can_run": False,
                    "code": """# package/__init__.py
from .button import Button
from .input import Input""",
                },
                {
                    "title": "Dynamic Import",
                    "notes": "Imports module dynamically at runtime.",
                    "py_can_run": False,
                    "code": """import importlib
module = importlib.import_module("utils")
helper = module.helper""",
                },
            ],
        },
        # String
        {
            "key": "string",
            "py_code_config": [
                {
                    "title": "String Declaration",
                    "py_can_run": True,
                    "code": """single: str = 'Hello'
dbl: str = "Hello"
triple: str = \"""Hello\"""   # multi-line

print(f"single: {single}")
print(f"dbl: {dbl}")
print(f"triple: {triple}")""",
                },
                {
                    "title": "String Immutability",
                    "py_can_run": True,
                    "code": """s: str = "Hi"

# TypeError: 'str' object does not support item assignment
s[0] = 'h'""",
                    "notes": "Strings are immutable.",
                },
                {
                    "title": "Length",
                    "py_can_run": True,
                    "code": """s: str = "Hello"
print(f"length: {len(s)}")""",
                },
                {
                    "title": "Formatting",
                    "py_can_run": True,
                    "code": """s1: str = f"Hello, {"Bob"}"
s2: str = "Hello, {}! {}".format("Alice", "Good Morning")
s3: str = "{0}, {1}, {2} and {1}".format("Toasted Brioche", "Garlic Aioli", "Smoked Turkey")

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")""",
                },
                {
                    "title": "Raw String",
                    "py_can_run": True,
                    "code": """s1: str = f"Hello, {"Bob"}"
s2: str = "Hello, {}! {}".format(repr("Alice"), repr("Good Morning"))

print(f"s1: {repr(s1)}")
print(f"s2: {s2!r}")""",
                },
                {
                    "title": "Indexing",
                    "py_can_run": True,
                    "code": """s: str = "Hello"

# 'H'
print(f"s[0]: {s[0]}")

# 'o'
print(f"s[4]: {s[4]}")""",
                },
                {
                    "title": "Slicing",
                    "py_can_run": True,
                    "code": """s: str = "Hello"

# 'ell'
print(f"s[1:4]: {s[1:4]}")

# 'llo'
print(f"s[2:]: {s[2:]}")

# 'llo'
print(f"s[-3:]: {s[-3:]}")""",
                },
                {
                    "title": "Concatenation",
                    "py_can_run": True,
                    "code": """a: str = "Hello"
b: str = "World"
c: str = a + " " + b

# 'Hello World'
print(f"c: {c}")""",
                },
                {
                    "title": "Repetition",
                    "py_can_run": True,
                    "code": """s: str = "Hi"
r = s * 3

# 'HiHiHi'
print(f"r: {r}")""",
                },
                {
                    "title": "Check Membership",
                    "py_can_run": True,
                    "code": """s: str = "Hello"
c1: bool = "ell" in s
c2: bool = "z" in s

# True
print(f"c1: {c1}")

# False
print(f"c2: {c2}")""",
                },
                {
                    "title": "String Type Check",
                    "py_can_run": True,
                    "code": """s: str = "abc"

# <class 'str'>
print(f"type(s): {type(s)}")

# True
print(f"isinstance(s, str): {isinstance(s, str)}")""",
                },
                {
                    "title": "Change Case",
                    "desc": "Upper | Lower | Title | Capitalize",
                    "py_can_run": True,
                    "code": """# HELLO WORLD
print(f"upper: {'hello world'.upper()}")

# hello
print(f"lower: {'HELLO'.lower()}")

# Hello World
print(f"title: {'hello world'.title()}")

# Hello world
print(f"capitalize: {'hello world'.capitalize()}")""",
                },
                {
                    "title": "Trim Whitespace",
                    "py_can_run": True,
                    "code": """# "hello"
print(f'strip: "{" hello ".strip()}"')

# "hello "
print(f'lstrip: "{" hello ".lstrip()}"')

# " hello"
print(f'rstrip: "{" hello ".rstrip()}"')""",
                },
                {
                    "title": "Replace Substring",
                    "py_can_run": True,
                    "code": """# "a, x, c"
print(f"replace: {'a, b, c'.replace('b', 'x')}")

# "one 2 2"
print(f"replace: {'one two two'.replace('two', '2')}")""",
                },
                {
                    "title": "Split String",
                    "py_can_run": True,
                    "code": """# ['a', 'b', 'c']
print(f"split by ', ': {'a, b, c'.split(', ')}")

# ['one', 'two', 'three']
print(f"split by ' ': {'one two three'.split(' ')}")""",
                },
                {
                    "title": "Join / Concat Parts",
                    "py_can_run": True,
                    "code": """# 'a-b-c'
print(f"join: {'-'.join(['a', 'b', 'c'])}")
                
# 'abc'
print(f"'a' + 'b' + 'c': {'a' + 'b' + 'c'}")""",
                },
                {
                    "title": "Pad / Fill",
                    "py_can_run": True,
                    "code": """# '007'
print(f"rjust: {'7'.rjust(3, '0')}")
                
# '700'
print(f"ljust: {'7'.ljust(3, '0')}")

# '070'
print(f"center: {'7'.center(3, '0')}")""",
                },
                {
                    "title": "Reverse String",
                    "py_can_run": True,
                    "code": """# 'olleh'
print(f"'hello'[::-1]: {'hello'[::-1]}")

# OR

reversed_str: str = ''.join(reversed("hello"))
# 'olleh'
print(f"reversed_str: {reversed_str}")""",
                },
            ],
        },
        # Functions
        {
            "key": "functions",
            "py_code_config": [
                {
                    "title": "Basic Function Declaration",
                    "py_can_run": False,
                    "code": """# Function Definition
def add(a, b):
    return a + b
    
# Typed Hints (Python 3+)
def add(a: int, b: int) -> int:
    return a + b""",
                },
                {
                    "title": "Lambda",
                    "py_can_run": False,
                    "code": """multiply = lambda a, b: a * b
square = lambda x: x * x""",
                    "notes": """_lambda_ is used for small, anonymous functions.
Use _def_ for normal functions.""",
                },
                {
                    "title": "Function Call",
                    "py_can_run": True,
                    "code": """def add(a, b):
    return a + b
    
def multiply(a, b):
    return a * b
    
# Function Call

add_answer = add(2, 3)

# 5
print(f"add_answer: {add_answer}")

multiply_answer = multiply(4, 5)

# 20
print(f"multiply_answer: {multiply_answer}")""",
                },
                {
                    "title": "Default Parameters",
                    "py_can_run": True,
                    "code": """def greet(name="Guest"):
    return f"Hello, {name}"

guest_greeted = greet()
print(f"guest_greeted: {guest_greeted}")

user_greeted = greet('Alice')
print(f"user_greeted: {user_greeted}")""",
                },
                {
                    "title": "Variadic Function",
                    "py_can_run": True,
                    "code": """def sum(*numbers):
    ans = 0
    for num in numbers:
        ans += num
    return ans
    
answer = sum(1, 2, 3, 4)

# 10
print(f"answer: {answer}")""",
                },
                {
                    "title": "Keyword Arguments",
                    "py_can_run": True,
                    "code": """def create_user(name, age):
    return {"name": name, "age": age}

user = create_user(age=25, name='Alice')

# {'name': 'Alice', 'age': 25}
print(f"user: {user}")""",
                },
                {
                    "title": "Arbitary Keyword Arguments (**kwargs)",
                    "py_can_run": True,
                    "code": """def print_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_user(name='Alice', age=25, city='NY')""",
                },
                {
                    "title": "Closures",
                    "py_can_run": True,
                    "code": """def outer(x):
    count = x
    def inner(y):
        nonlocal count
        count += y
        return count
    return inner

fn = outer(10)

answer_1 = fn(5)

# 15
print(f"answer_1: {answer_1}")

answer_2 = fn(3)

# 18
print(f"answer_2: {answer_2}")""",
                },
                {
                    "title": "Positional-Only Parameters",
                    "py_can_run": True,
                    "code": """def divide(a, b, /):
    return a / b
    
answer_1 = divide(10, 2)

# 5.0
print(f"answer_1: {answer_1}")

# TypeError
answer_2 = divide(a=10, b=2)""",
                },
                {
                    "title": "First-Class Function",
                    "py_can_run": True,
                    "code": """def greet(name: str):
    return f"Hello, {name}"
    
say_hi = greet

def run(fn):
    return fn("World")
    
value_str = run(say_hi)

# 'Hello, World'
print(f"value_str: {value_str}")""",
                },
                {
                    "title": "Recursive Function",
                    "py_can_run": True,
                    "code": """def fact(n: int):
    if n <= 1:
        return 1
    return n * fact(n - 1)
    
answer = fact(5)

# 120
print(f"answer: {answer}")""",
                },
                {
                    "title": "Higher-Order Function",
                    "py_can_run": True,
                    "code": """def apply_twice(fn, value):
    return fn(fn(value))
    
def add(x: int):
    return x + 1
    
applied_value = apply_twice(add, 5)

# 7
print(f"applied_value: {applied_value}")


def multiplier(factor: int):
    def inner(x: int):
        return x * factor
    return inner

double_fn = multiplier(2)

double_value = double_fn(5)

# 10
print(f"double_value: {double_value}")""",
                },
                {
                    "title": "Returning Multiple Values",
                    "py_can_run": True,
                    "code": """def get_user():
    return 1, 'Alice' # tuple
    
user_id, user_name = get_user()

# 1
print(f"user_id: {user_id}")

# 'Alice'
print(f"user_name: {user_name}")


# Or return tuple explicitly
def get_point():
    return (10, 20)
    
x, y = get_point()

# 10
print(f"x: {x}")

# 20
print(f"y: {y}")""",
                },
                {
                    "title": "Function Objects / Callable",
                    "py_can_run": True,
                    "code": """def hello():
    return "Hi"

# 'hello'
print(f"hello.__name__: {hello.__name__}")

# True
print(f"callable: {callable(hello)}")""",
                },
            ],
        },
        # List (Array)
        {
            "key": "array_list",
            "py_code_config": [
                {
                    "title": "Create",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]

print(f"lst: {lst}")""",
                },
                {
                    "title": "Access",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]

print(f"lst: {lst}")
print(f"lst[0]: {lst[0]}")
print(f"lst[3]: {lst[3]}")
print(f"lst[-1]: {lst[-1]}")""",
                },
                {
                    "title": "Update",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
print(f"before update - lst: {lst}")

lst[1] = 20
lst[3] = 'hello'
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Delete",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
print(f"before delete - lst: {lst}")

del lst[2]
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Length | Size",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]

print(f"lst: {lst}")
print(f"length: {len(lst)}")""",
                },
                {
                    "title": "Iteration (Index Based)",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
for i in range(len(lst)):
    print(f"lst[{i}]: {lst[i]}")""",
                },
                {
                    "title": "Iteration (Value Based)",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
for item in lst:
    print(f"item: {item}")""",
                },
                {
                    "title": "Iteration (Index & Value Based)",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
for index, item in enumerate(lst):
    print(f"lst[{index}]: {item}")""",
                },
                {
                    "title": "Copy",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
lst2 = lst.copy()
lst3 = lst[:]
lst4 = lst

print(f"lst: {lst}")
print(f"lst2: {lst2}")
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")

print(f"lst is lst2: {lst is lst2}")
print(f"lst is lst3: {lst is lst3}")
print(f"lst is lst4: {lst is lst4}")""",
                },
                {
                    "title": "Reference",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
lst4 = lst
print(f"before update - lst: {lst}")
print(f"lst4: {lst4}\\n")

lst4[0] = 100
print(f"after update - lst: {lst}")
print(f"lst4: {lst4}")
print(f"lst is lst4: {lst is lst4}")""",
                },
                {
                    "title": "Type Check",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 'a', True]
is_list1 = type(lst) is list
is_list2 = isinstance(lst, list)

print(f"is_list1: {is_list1}")
print(f"is_list2: {is_list2}")""",
                },
                {
                    "title": "Empty",
                    "py_can_run": True,
                    "code": """lst = []
is_empty_list = not lst               
print(f"is_empty_list: {is_empty_list}")""",
                },
                {
                    "title": "Add to End",
                    "py_can_run": True,
                    "code": """lst = [1, 2]
print(f"before update - lst: {lst}")

lst.append(3)
lst.extend([4, 5])
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Add to Start",
                    "py_can_run": True,
                    "code": """lst = [3, 4]
print(f"before update - lst: {lst}")

lst.insert(0, 1) # insert(index, element)
lst[:0] = [2]
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Remove from End",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3]
print(f"before update - lst: {lst}")

last = lst.pop()
print(f"after update - lst: {lst}")
print(f"last: {last}")""",
                },
                {
                    "title": "Remove from Start",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3]
print(f"before update - lst: {lst}")

element = lst.pop(0)
print(f"after update - lst: {lst}")
print(f"element: {element}")""",
                },
                {
                    "title": "Merge / Concatenate (Non-Mutating)",
                    "py_can_run": True,
                    "code": """a = [1, 2]
b = [3, 4]
c = a + b + [5, 6]

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Or

print(f"before update - a: {a}")
a.extend(b)
a.extend([5, 6])
print(f"after update - a: {a}")""",
                },
                {
                    "title": "Extract Subarray (Non-Mutating)",
                    "py_can_run": True,
                    "code": """lst = [0, 1, 2, 3, 4]
print(f"before update - lst: {lst}")

lst1 = lst[1:4]
lst2 = lst[2:]
lst3 = lst[:]
lst4 = lst[-3]

print(f"lst1: {lst1}")
print(f"lst2: {lst2}")
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Add / Remove / Replace",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 4]
print(f"before update - lst: {lst}")

del lst[1:3]
print(f"after update - lst: {lst}")

lst[1:1] = ['a', 'b']
print(f"after update - lst: {lst}")

lst[2:3] = ['X']
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Transform Each Element",
                    "py_can_run": True,
                    "code": """nums = [1, 2, 3, 4]
doubled = [n * 2 for n in nums]

print(f"nums: {nums}")
print(f"doubled: {doubled}\\n")

# Or

doubled = list(map(lambda n: n * 2, nums))
print(f"doubled: {doubled}")""",
                },
                {
                    "title": "Filter Elements",
                    "py_can_run": True,
                    "code": """nums = [1, 2, 3, 4, 5]
even_nums = [n for n in nums if n % 2 == 0]

print(f"nums: {nums}")
print(f"even_nums: {even_nums}\\n")

# Or

even_nums = list(filter(lambda n: n % 2 == 0, nums))
print(f"even_nums: {even_nums}")""",
                },
                {
                    "title": "Reduce to Single Value",
                    "py_can_run": True,
                    "code": """from functools import reduce

nums = [1, 2, 3, 4]
sum_ = reduce(lambda acc, n: acc + n, nums, 0)

print(f"nums: {nums}")
print(f"sum: {sum_}")""",
                },
                {
                    "title": "Find First Match",
                    "py_can_run": True,
                    "code": """nums = [5, 12, 8, 130, 44]
first_large = next((n for n in nums if n > 10), None)

print(f"nums: {nums}")
print(f"first_large: {first_large}")""",
                },
                {
                    "title": "Find Index of First Match",
                    "py_can_run": True,
                    "code": """nums = [5, 12, 8, 130, 44]
first_large_index = next((i for i, n in enumerate(nums) if n > 10), -1)

print(f"nums: {nums}")
print(f"first_large_index: {first_large_index}")""",
                },
                {
                    "title": "Check At Least One Match Exist",
                    "py_can_run": True,
                    "code": """nums = [1, 3, 5, 8]
has_even = any(n % 2 == 0 for n in nums)

print(f"nums: {nums}")
print(f"has_even: {has_even}")""",
                },
                {
                    "title": "Check All Elements Matched",
                    "py_can_run": True,
                    "code": """nums = [2, 4, 6, 8]
all_even = all(n % 2 == 0 for n in nums)

print(f"nums: {nums}")
print(f"all_even: {all_even}")""",
                },
                {
                    "title": "Check Element Existence",
                    "py_can_run": True,
                    "code": """nums = [1, 2, 3]
            
print(f"nums: {nums}")
print(f"2 in nums: {2 in nums}")
print(f"5 in nums: {5 in nums}")""",
                },
                {
                    "title": "Index of Value",
                    "py_can_run": True,
                    "code": """nums = [1, 2, 3, 2]
print(f"nums: {nums}")
print(f"index of 2: {nums.index(2)}")

# ValueError
print(f"index of 9: {nums.index(9)}")""",
                },
                {
                    "title": "Sort",
                    "py_can_run": True,
                    "code": """lst = [3, 1, 4, 2]                
print(f"before update - lst: {lst}")

lst.sort()
print(f"after update - lst: {lst}")

words = ['b', 'a', 'd', 'c']
print(f"before update - words: {words}")

words.sort()
print(f"after update - words: {words}")

lst = [3, 1, 4, 2]
print(f"before update - lst: {lst}")

lst.sort(reverse=True)
print(f"after update - reversed lst: {lst}")

words = ['b', 'a', 'd', 'c']
print(f"before update - words: {words}")

sorted_words = sorted(words, reverse=True)
print(f"after update - words: {words}")
print(f"sorted_words: {sorted_words}")""",
                },
                {
                    "title": "Reverse",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 4]
print(f"before update - lst: {lst}")

lst.reverse()
print(f"after update - lst: {lst}")

lst = [1, 2, 3, 4]
print(f"before update - lst: {lst}")

reversed_lst = list(reversed(lst))
print(f"after update - lst: {lst}")
print(f"reversed_lst: {reversed_lst}")""",
                },
                {
                    "title": "Join to String",
                    "py_can_run": True,
                    "code": """lst = ['Hello', 'World']
joined_str1 = " ".join(lst)
joined_str2 = "-".join(lst)

print(f"lst: {lst}")
print(f"joined_str1: {joined_str1}")
print(f"joined_str2: {joined_str2}")""",
                },
                {
                    "title": "Fill with Value",
                    "py_can_run": True,
                    "code": """lst = [0] * 5
print(f"lst: {lst}")

lst[1:4] = [9] * 3
print(f"after update - lst: {lst}")

lst[:] = [7] * len(lst)
print(f"after update - lst: {lst}")""",
                },
                {
                    "title": "Copy Within Array",
                    "py_can_run": True,
                    "code": """lst = [1, 2, 3, 4, 5]
print(f"before update - lst: {lst}")

lst[0:2] = lst[3:]
print(f"after update - lst: {lst}")

lst = [1, 2, 3, 4, 5]
print(f"before update - lst: {lst}")

lst[1:3] = lst[2:4]
print(f"after update - lst: {lst}")""",
                },
            ],
        },
        # Dictionary
        {
            "key": "object_dict",
            "py_code_config": [
                {
                    "title": "Create",
                    "py_can_run": True,
                    "code": """user = {}
user2 = {'name': 'Alice', 'age': 25}
user3: dict[str, str | int] = {'name': 'Bob', 'age': 30}

print(f"user: {user}")
print(f"user2: {user2}")
print(f"user3: {user3}")""",
                },
                {
                    "title": "Create from Keys",
                    "py_can_run": True,
                    "code": """keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
d2 = dict.fromkeys('xyz')

print(f"keys: {keys}")
print(f"d: {d}")
print(f"d2: {d2}")""",
                },
                {
                    "title": "Create from Tuples",
                    "py_can_run": True,
                    "code": """tuples_list = [('a', 1), ('b', 2)]
d = dict(tuples_list)

print(f"tuples_list: {tuples_list}")
print(f"d: {d}")""",
                },
                {
                    "title": "Access",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_name = user['name']
user_age = user['age']

print(f"user_name: {user_name}")
print(f"user_age: {user_age}")""",
                },
                {
                    "title": "Add",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

user['email'] = 'alice@example.com'
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Update",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

user['age'] = 30
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Delete",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

del user['age']
print(f"after update - user: {user}")

# KeyError - 'email' not exist
del user['email']""",
                },
                {
                    "title": "Check Key",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
        
is_name_exist = 'name' in user
is_email_exist = user.get('email') is not None

print(f"user: {user}")
print(f"is_name_exist: {is_name_exist}")
print(f"is_email_exist: {is_email_exist}")""",
                },
                {
                    "title": "Length",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"user: {user}")
print(f"Length: {len(user)}")""",
                },
                {
                    "title": "Iterate Keys",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
for key in user:
    print(f"key: {key}")""",
                },
                {
                    "title": "Iterate Values",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
for value in user.values():
    print(f"value: {value}")""",
                },
                {
                    "title": "Iterate Items",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
for key, value in user.items():
    print(f"{key}: {value}")""",
                },
                {
                    "title": "Default Values",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice'}
user_age = user.get('age', 0)

print(f"user: {user}")
print(f"user_age: {user_age}")""",
                },
                {
                    "title": "Copy / Clone",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
cloned_user = user.copy()
user_ref = user

print(f"user: {user}")
print(f"cloned_user: {cloned_user}")
print(f"user_ref: {user_ref}\\n")
print(f"user is cloned_user: {user is cloned_user}")
print(f"user is user_ref: {user is user_ref}")""",
                },
                {
                    "title": "Access All Keys (List)",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_keys = list(user.keys())

print(f"user: {user}")
print(f"user_keys: {user_keys}")""",
                },
                {
                    "title": "Access All Values (List)",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_values = list(user.values())

print(f"user: {user}")
print(f"user_values: {user_values}")""",
                },
                {
                    "title": "Access All Items (Tuples)",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_items = list(user.items())

print(f"user: {user}")
print(f"user_items: {user_items}")""",
                },
                {
                    "title": "Set Default",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice'}
print(f"before update - user: {user}")

user.setdefault('age', 0)
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Update using new Dictionary",
                    "py_can_run": True,
                    "code": """target = {'a': 1}
print(f"before update - target: {target}")

target.update({'b': 2})
print(f"after update - target: {target}")

target.update(c=3)
print(f"after update - target: {target}")""",
                },
                {
                    "title": "Freezing Dictionary",
                    "py_can_run": True,
                    "code": """from types import MappingProxyType
user = {'name': 'Alice', 'age': 25}
user_proxy = MappingProxyType(user)

print(f"user: {user}")
print(f"user_proxy: {user_proxy}")

# TypeError
user_proxy['name'] = 'Bob'""",
                },
                {
                    "title": "Pop Value",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

user_age = user.pop('age')
print(f"user_age: {user_age}")
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Pop Item",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

user_age_item = user.popitem()
print(f"user_age_item: {user_age_item}")
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Clear",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
print(f"before update - user: {user}")

user.clear()
print(f"after update - user: {user}")""",
                },
                {
                    "title": "Spread Operator",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
extra = {'city': 'NY', 'role': 'Dev'}
merged = {**user, **extra, 'age': 26}
merged2 = user | extra | {'age': 26}

print(f"user: {user}")
print(f"extra: {extra}")
print(f"merged: {merged}")
print(f"merged2: {merged2}")""",
                },
                {
                    "title": "Safe Access",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_city = user.get('address', {}).get('city', 'N/A')

print(f"user: {user}")
print(f"user_city: {user_city}")""",
                },
                {
                    "title": "Get with Default",
                    "py_can_run": True,
                    "code": """user = {'name': 'Alice', 'age': 25}
user_role = user.get('role', 'Guest')
user_role1 = user['role'] if 'role' in user else 'Guest'

print(f"user: {user}")
print(f"user_role: {user_role}")
print(f"user_role1: {user_role1}")""",
                },
            ],
        },
        # Set
        {
            "key": "set",
            "py_code_config": [
                {
                    "title": "Create a Set",
                    "py_can_run": True,
                    "code": """s1 = {1, 2, 3, 'a'}
s2 = set([1, 2, 3, 4, 'a'])
empty_set = set()

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"empty_set: {empty_set}")""",
                },
                {
                    "title": "Set Properties",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3, 2, 1, 'a', 'a'}

print(f"s: {s}")
print(f"type: {type(2)}")
print(f"length: {len(s)}")""",
                },
                {
                    "title": "Add an Item",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3}
                
s.add(4)
s.add(2)

print(f"s: {s}")""",
                },
                {
                    "title": "Update an Item",
                    "py_can_run": True,
                    "code": """s = {1, 2}

s.update([2, 3, 4], {4, 5})

print(f"set: {s}")""",
                },
                {
                    "title": "Remove an Item",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3, 4}

s.remove(3)
print(f"set: {s}")

# KeyError: 9
s.remove(9)""",
                },
                {
                    "title": "Discard an Item",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3, 4}
                
s.discard(2)

# no error
s.discard(9)

print(f"set: {s}")""",
                },
                {
                    "title": "Clear a Set",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3}
            
s.clear()

print(f"set: {s}")""",
                },
                {
                    "title": "Check Membership",
                    "py_can_run": True,
                    "code": """s = {1, 2, 3}
                
print(f"2 in s: {2 in s}")
print(f"5 in s: {5 in s}")
print(f"2 not in s: {2 not in s}")""",
                },
                {
                    "title": "Iterate Over Set",
                    "py_can_run": True,
                    "code": """s = {'a', 'b', 'c'}
for item in s:
    print(f"item: {item}")""",
                },
                {
                    "title": "Union",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3}
b = {3, 4, 5}

# c = a ∪ b
c = a.union(b)

print(f"union: {c}")""",
                },
                {
                    "title": "Intersection",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3}
b = {2, 3, 4}

# c = a ∩ b
c = a.intersection(b)

print(f"intersection: {c}")""",
                },
                {
                    "title": "Difference",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3, 4}
b = {3, 4, 5}

# c = a - b
# items in a that are no in b
c = a.difference(b)

print(f"difference: {c}")""",
                },
                {
                    "title": "Symmetric Difference",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3}
b = {2, 3, 4}

# c = a ⊖ b 
# items in a or b but NOT in both
c = a.symmetric_difference(b)

print(f"symmetric_difference: {c}")""",
                },
                {
                    "title": "Subset",
                    "py_can_run": True,
                    "code": """a = {1, 2}
b = {1, 2, 3, 4}

# c = a ⊂ b
c = a.issubset(b)

print(f"issubset: {c}")""",
                },
                {
                    "title": "Superset",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3, 4}
b = {1, 2}

# c = a ⊃ b
c = a.issuperset(b)

print(f"issuperset: {c}")""",
                },
                {
                    "title": "Disjoint",
                    "py_can_run": True,
                    "code": """a = {1, 2}
b = {3, 4}

# check if no common elements
c = a.isdisjoint(b)

print(f"isdisjoint: {c}")""",
                },
                {
                    "title": "Copy",
                    "py_can_run": True,
                    "code": """a = {1, 2, 3}
b = a.copy()

print(f"a: {a}")
print(f"b: {b}")
print(f"a is b: {a is b}")""",
                },
                {
                    "title": "Frozenset",
                    "py_can_run": True,
                    "code": """fs = frozenset([1, 2, 3])
print(f"fs: {fs}")

# AttributeError
fs.add(4)""",
                },
            ],
        },
        # Classes
        {
            "key": "classes",
            "py_code_config": [
                {
                    "title": "Class Declaration",
                    "py_can_run": False,
                    "code": """class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age""",
                },
                {
                    "title": "Create Object",
                    "py_can_run": False,
                    "code": """class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)""",
                },
                {
                    "title": "Access Attribute",
                    "py_can_run": True,
                    "code": """class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
p1_name = p1.name
p1_age = p1.age

print(f"p1_name: {p1_name}")
print(f"p1_age: {p1_age}")""",
                },
                {
                    "title": "Define Method",
                    "py_can_run": True,
                    "code": """class Person:
    def __init__(self, name: str):
        self.name = name
        
    def introduce(self):
        return f"Hi, I am {self.name}"\\""",
                },
                {
                    "title": "Call Method",
                    "py_can_run": True,
                    "code": """class Person:
    def __init__(self, name: str):
        self.name = name
        
    def introduce(self):
        return f"Hi, I am {self.name}"
        
p1 = Person("Bob")
p1_intro = p1.introduce()

print(f"p1_intro: {p1_intro}")""",
                },
                {
                    "title": "Default Values",
                    "py_can_run": True,
                    "code": """class Person:
    def __init__(self, name: str = "Guest"):
        self.name = name
        
p1 = Person()
p1_name = p1.name

print(f"p1_name: {p1_name}")""",
                },
                {
                    "title": "Add Method Outside Class",
                    "py_can_run": True,
                    "code": """class Person:
    def __init__(self, name: str = "Guest"):
        self.name = name

def say_hello(self):
    return f"Hello, I am {self.name}"
    
Person.say_hello = say_hello

p1 = Person("Alice")
p1_say_hello = p1.say_hello()

print(f"p1_say_hello: {p1_say_hello}")""",
                },
                {
                    "title": "Class Inheritance",
                    "py_can_run": True,
                    "code": """class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} makes a sound."
        
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."
    
d = Dog("Tom")
d_speak = d.speak()

print(f"d_speak: {d_speak}")""",
                },
                {
                    "title": "Multiple Inheritance",
                    "py_can_run": True,
                    "code": """class Flyable:
    def fly(self):
        return "Flying"
        
class Swimmable:
    def swim(self):
        return "Swimming"
        
class Duck(Flyable, Swimmable):
    pass

d = Duck()
d_fly = d.fly()
d_swim = d.swim()

print(f"d_fly: {d_fly}")
print(f"d_swim: {d_swim}")""",
                },
                {
                    "title": "Class Methods",
                    "py_can_run": True,
                    "code": """class Counter:
    count = 0
    
    @classmethod
    def get_count(cls):
        return cls.count
        
c = Counter()
Counter.count += 1
updated_count = Counter.get_count()

print(f"updated_count: {updated_count}")""",
                },
                {
                    "title": "Static Methods",
                    "py_can_run": True,
                    "code": """class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b
        
sum_ = MathUtil.add(2, 3)
print(f"sum: {sum_}")""",
                },
                {
                    "title": "Properties (Getter / Setter)",
                    "py_can_run": True,
                    "code": """class User:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value.strip()
        
p1 = User("Alice")
p1_user_name = p1.name
print(f"p1_user_name: {p1_user_name}")

p1.name = 'Bob'
p1_user_name = p1.name
print(f"p1_user_name: {p1_user_name}")""",
                },
                {
                    "title": "Dunder Methods",
                    "py_can_run": True,
                    "code": """class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(2, 3)
p_value = str(p)

print(f"p_value: {p_value}")""",
                },
                {
                    "title": "Class Variables",
                    "py_can_run": True,
                    "code": """class Product:
    category = "General"

    def __init__(self, name):
        self.name = name
    
category = Product.category
print(f"category: {category}")""",
                },
                {
                    "title": "Polymorphism",
                    "py_can_run": True,
                    "code": """class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.1416 * self.r ** 2
    
c = Circle(2)
c_area = c.area()
print(f"c_area: {c_area}")""",
                },
                {
                    "title": "Abstract Base Class",
                    "py_can_run": True,
                    "code": """from abc import ABC, abstractmethod
                
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
        
    def area(self):
        return self.w * self.h
        
rect = Rectangle(4, 5)
rect_area = rect.area()

print(f"rect_area: {rect_area}")""",
                },
                {
                    "title": "Private / Protected Members",
                    "py_can_run": True,
                    "code": """class User:
    def __init__(self, id):
        # protected (single _)
        self._id = id

        #private (name mangling)
        self.__token = 'abc'
        
    def get_id(self):
        return self._id
        
user = User(1)
user_id = user.get_id()

print(f"user_id: {user_id}")

# user.__token not accessible directly
print(f"user.__token: {user.__token}")""",
                },
                {
                    "title": "Class Methods",
                    "py_can_run": True,
                    "code": """class MathUtil:
    PI = 3.14159
    
    @classmethod
    def area(cls, r):
        return cls.PI * r ** 2
        
pi = MathUtil.PI
area = MathUtil.area(2)

print(f"pi: {pi}")
print(f"area: {area}")""",
                },
                {
                    "title": "Composition",
                    "py_can_run": True,
                    "code": """class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand):
        self.engine = Engine()
        self.brand = brand

car = Car('Toyota')
engine = car.engine.start();

print(f"engine: {engine}")""",
                },
            ],
        },
        # Typed Hints
        {
            "key": "typed_hints",
            "py_code_config": [
                {
                    "title": "Type Definition",
                    "py_can_run": False,
                    "code": """from typing import TypedDict
                
class User(TypedDict):
    id: int
    name: str
    isActive: bool
    
# Or using a class with type hints

class UserModel:
    id: int
    name: str
    isActive: bool""",
                },
                {
                    "title": "Optional Properties",
                    "py_can_run": False,
                    "code": """from typing import TypedDict, NotRequired
                
class User(TypedDict, total=False):
    id: int
    name: NotRequired[str]
    email: NotRequired[str]""",
                },
                {
                    "title": "Readonly Properties",
                    "py_can_run": False,
                    "code": """from typing_extensions import ReadOnly
                
class User(TypedDict):
    id: ReadOnly[int]
    name: ReadOnly[str]""",
                },
                {
                    "title": "Call Signature",
                    "py_can_run": False,
                    "code": """from typing import Callable
Add = Callable([int, int], int)
Greater = Callable([str], str)""",
                },
                {
                    "title": "Record Type",
                    "py_can_run": False,
                    "code": """from typing import Dict
StringMap = Dict[str, str]
RoleMap = Dict[str, int]""",
                },
                {
                    "title": "Union Types",
                    "py_can_run": False,
                    "code": """from typing import Literal
Status = Literal['success', 'error', 'loading']

class ApiResponse(TypedDict):
    status: Status
    data: object""",
                },
                {
                    "title": "Intersection Types",
                    "py_can_run": False,
                    "code": """from typing import TypedDict
class A(TypedDict):
    id: int
    
class B(TypedDict):
    name: str

class AWithB(A, B):
    pass""",
                },
                {
                    "title": "Generics",
                    "py_can_run": False,
                    "code": """from typing import TypeVar, Generic
T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        
box: Box[int] = Box(123)""",
                },
            ],
        },
        # Error Handling
        {
            "key": "error_handling",
            "py_code_config": [
                {
                    "title": "Basic Syntax",
                    "py_can_run": False,
                    "code": """try:
    # risky code
except Exception as e:
    # handle error""",
                },
                {
                    "title": "Catch Specific Errors",
                    "desc": "",
                    "py_can_run": True,
                    "code": """try:
    risky_call()
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
except Exception as e:
    print(f"Other error: {e}")""",
                },
                {
                    "title": "Finally Block",
                    "py_can_run": True,
                    "code": """try:
    risky_call()
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
except Exception as e:
    print(f"Other error: {e}")
finally:
    # always runs
    print("finally executed.")""",
                    "notes": "_finally_ runs regardness of success or failure.",
                },
                {
                    "title": "Throw / Raise Errors",
                    "py_can_run": True,
                    "code": """user = None
if not user:
    raise ValueError("User not found")
raise TypeError("Invalid type")""",
                },
                {
                    "title": "Custom Errors",
                    "py_can_run": True,
                    "code": """class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        
raise ValidationError("Invalid data")""",
                },
                {
                    "title": "Access Error Information",
                    "desc": "",
                    "py_can_run": True,
                    "code": """import traceback
import sys

try:
    # Trigger a conscious error (Division by Zero)
    result = 10 / 0
except Exception:
    print("An error occurred! Printing the stack trace:")

    # Forces traceback into stdout because web playgrounds often hide stderr
    traceback.print_exc(file=sys.stdout)

print("The program continues to run normally!")""",
                },
                {
                    "title": "Ignore Exception",
                    "py_can_run": True,
                    "code": """try:
    risky_call()
except Exception as e:
    # Not recommended generally
    pass

print("The program continues to run normally!")""",
                },
                {
                    "title": "Rethrow Exception",
                    "py_can_run": True,
                    "code": """try:
    risky_call()
except Exception as e:
    print("Something failed")
    raise ValueError("risky_call not found")""",
                },
            ],
        },
        # JSON
        {
            "key": "json",
            "py_code_config": [
                {
                    "title": "Parse JSON",
                    "py_can_run": True,
                    "code": """import json

json_string: str = '{"name": "Alice", "age": 25}'
obj: dict[str, str | int] = json.loads(json_string)

# 'Alice'
print(f"obj['name']: {obj['name']}")

# 25
print(f"obj['age']: {obj['age']}")""",
                },
                {
                    "title": "Stringify JSON",
                    "py_can_run": True,
                    "code": """import json

obj: dict[str, str | int] = {"name": "Alice", "age": 25}
json_string: str = json.dumps(obj)

# '{"name": "Alice", "age": 25}'
print(f"json_string: {json_string}")""",
                },
                {
                    "title": "Pretty Print",
                    "py_can_run": True,
                    "code": """import json

obj: dict[str, str | int | list[str]] = {"name": "Alice", "age": 25, "skills": ['JS', 'TS']}

pretty_str: str = json.dumps(obj, indent=2)

\"""
{
"name": "Alice",
"age": 25,
"skills": [
    "JS",
    "TS"
]
}
\""" 
print(f"pretty_str: {pretty_str}")""",
                },
                {
                    "title": "Handle Errors",
                    "py_can_run": True,
                    "code": """import json

json_string_invalid: str = '{"name": "Alice", age": 25}'

try:
    obj = json.loads(json_string_invalid)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")""",
                },
                {
                    "title": "Check if String is Valid JSON",
                    "py_can_run": True,
                    "code": """import json

def is_valid_json(s: str):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False
        
json_string_valid: str = '{"name": "Alice", "age": 25}'

# True
print(f"json_string_valid: {is_valid_json(json_string_valid)}")

json_string_invalid: str = '{"name: "Alice", age": 25}'

# False
print(f"json_string_invalid: {is_valid_json(json_string_invalid)}")""",
                },
                {
                    "title": "Custom Replacer",
                    "desc": "Filter / Transform while Stringify",
                    "py_can_run": True,
                    "code": """import json

def replacer(obj):
    return {k: v for k, v in obj.items() if k != 'password'}

obj: dict[str, str | int] = {"name": "Alice", "age": 25, "password": "123456"}

safe_obj = replacer(obj)
safe_str = json.dumps(safe_obj, default=replacer)

# '{"name": "Alice", "age": 25}'
print(f"safe_str: {safe_str}")""",
                },
                {
                    "title": "Write JSON to File",
                    "py_can_run": False,
                    "code": """import json

obj: dict[str, str | int] = {"name": "Alice", "age": 25}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f, indent=2)

# File: data.json""",
                },
                {
                    "title": "Read JSON from File",
                    "py_can_run": False,
                    "code": """import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"data: {data}")""",
                },
            ],
        },
        # HTTP Requests
        {
            "key": "http_requests",
            "py_code_config": [
                {
                    "title": "Get Request",
                    "py_can_run": True,
                    "code": """import requests

print("Fetching data...\\n")

url: str = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json()

print(f"data: {data}")""",
                },
                {
                    "title": "Post Request",
                    "py_can_run": True,
                    "code": """import requests

print("Fetching data...\\n")

url: str = "https://jsonplaceholder.typicode.com/posts"
payload: dict[str, str | int] = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(url, json=payload)

data = response.json()
print(f"data: {data}")""",
                },
                {
                    "title": "Headers & Query Params",
                    "py_can_run": True,
                    "code": """import requests

print("Fetching data...\\n")

url: str = "https://jsonplaceholder.typicode.com/posts/1"
params: dict[str, str] = {"search": "python"}
headers: dict[str, str] = {"Authorization": "Bearer TOKEN", "Accept": "application/json"}

response = requests.get(url, params=params, headers=headers)

data = response.json()
print(f"data: {data}")""",
                },
                {
                    "title": "Response Handling",
                    "py_can_run": True,
                    "code": """import requests

print("Fetching data...")

url: str = "https://jsonplaceholder.typicode.com/pt/1"
response = requests.get(url)

status_code = response.status_code

if status_code != 200:
    raise Exception(f"HTTP {status_code}")

data = response.json()
print(f"data: {data}")""",
                },
                {
                    "title": "Timeout & Error Handling",
                    "py_can_run": True,
                    "code": """import requests
print("Fetching data...")

try:
    url: str = "https://jsonplaceholder.typicode.com/psts/4"
    response = requests.get(url, timeout=4)
    response.raise_for_status()
except requests.Timeout:
    print("Request time out")
except requests.RequestException as e:
    print(f"Request failed: {e}")""",
                },
                {
                    "title": "Async / Await (Non-blocking)",
                    "desc": "",
                    "py_can_run": True,
                    "code": """import httpx
import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        url: str = "https://jsonplaceholder.typicode.com/posts/1"
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"data: {data}")

print("Fetching data...\\n")
asyncio.run(get_data())""",
                },
            ],
            "py_notes": """**Common Status Codes:**
| Status Code | Status Name | Description |
| :--- | :--- | :--- |
| **200 OK** | Success | Request completed successfully |
| **201 Created** | Resource created | New resource successfully built |
| **400 Bad Request** | Invalid request | Server cannot process bad syntax |
| **401 Unauthorized** | Auth required | Valid authentication credentials missing |
| **403 Forbidden** | Access denied | Server understands but refuses action |
| **404 Not Found** | Resource not found | Target resource does not exist |
| **500 Internal Server Error** | Server issue | Server encountered an unexpected error |
| **502 Bad Gateway** | Gateway error | Invalid response from upstream server |
""",
        },
        # Async Operations
        {
            "key": "async_operations",
            "py_code_config": [
                {
                    "title": "Define Async Function",
                    "py_can_run": False,
                    "code": """import asyncio

async def simulate_fetch_data():
    print("Start fetching...")

    # Simulate waiting 2 seconds for a server response without blocking
    await asyncio.sleep(2) 

    print("Data fetched!")
    return {"data": "success"}""",
                },
                {
                    "title": "Await Function",
                    "py_can_run": False,
                    "code": """data = await simulate_fetch_data()""",
                },
                {
                    "title": "Run Async Code",
                    "py_can_run": True,
                    "code": """import asyncio

async def simulate_fetch_data():
    print("Start fetching...")

    await asyncio.sleep(2) 

    print("Data fetched!")
    return {"data": "success"}

async def call_fetch_data():
    data = await simulate_fetch_data()
    print(f"data: {data}")

asyncio.run(call_fetch_data())""",
                },
                {
                    "title": "Handle Errors",
                    "py_can_run": True,
                    "code": """import asyncio

async def simulate_fetch_data():
    print("Start fetching...")

    await asyncio.sleep(2) 
    raise ConnectionError("Failed to connect to server.")

    print("Data fetched!")
    return {"data": "success"}

async def call_fetch_data():
    try:
        data = await simulate_fetch_data()
        print(f"data: {data}")
    except ConnectionError as e:
        print(f"Caught error: {e}")

asyncio.run(call_fetch_data())""",
                },
                {
                    "title": "Run Tasks Concurrently",
                    "py_can_run": True,
                    "code": """import asyncio

async def simulate_fetch_data(id_: int, sleep_time: int):
    print(f"id-{id_}: Start fetching...")
    await asyncio.sleep(sleep_time) 
    print(f"id-{id_}: Data fetched!")
    return {"id": id_, "data": "success"}

async def call_concurrent_fetch_data():
    results = await asyncio.gather(simulate_fetch_data(2, 2), simulate_fetch_data(1, 1))
    print(f"results: {results}")

asyncio.run(call_concurrent_fetch_data())""",
                },
                {
                    "title": "Cancel Task",
                    "py_can_run": True,
                    "code": """import asyncio

async def simulate_fetch_data():
    print("Start fetching...")
    await asyncio.sleep(1)
    print("Data fetched!")
    return {"data": "success"}

async def call_fetch_data():
    task = asyncio.create_task(simulate_fetch_data())
    await asyncio.sleep(0.1)

    task.cancel()
    
    try:
        data = await task
        print(f"data: {data}")
    except asyncio.CancelledError:
        print("Cancelled! (Safely handled)")

asyncio.run(call_fetch_data())
""",
                },
            ],
        },
        # Date & Time
        {
            "key": "date_time",
            "py_code_config": [
                {
                    "title": "Get Current Date & Time & Timestamp",
                    "py_can_run": True,
                    "code": """# Current date & time (local)
from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()
print(f"now: {now}")
print(f"timestamp: {timestamp}")

# Timestamp (seconds sinch epoch)
import time
ts = time.time()
print(f"ts: {ts}")""",
                },
                {
                    "title": "Create Specific Date & Time",
                    "py_can_run": True,
                    "code": """from datetime import datetime
d1 = datetime(2024, 5, 24)
d2 = datetime(2024, 5, 24, 10, 30, 0)
d3 = datetime.fromisoformat("2024-05-24T10:30:30")

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}")""",
                },
                {
                    "title": "Format Date Only",
                    "py_can_run": True,
                    "code": """from datetime import date
d = date(2024, 5, 24)
formatted_date_only = d.strftime("%a %b %d %Y")

print(f"d: {d}")
print(f"formatted_date_only: {formatted_date_only}")""",
                },
                {
                    "title": "Format Time Only",
                    "py_can_run": True,
                    "code": """from datetime import time
t = time(14, 30, 0)
formatted_time_only = t.strftime("%H:%M:%S")

print(f"t: {t}")
print(f"formatted_time_only: {formatted_time_only}")""",
                },
                {
                    "title": "Format Date & Time",
                    "py_can_run": True,
                    "code": """from datetime import datetime
d = datetime(2024, 5, 24, 10, 30, 0)

iso_formatted_datetime = d.isoformat()
formatted_date_only = d.strftime("%d %b %Y")
formatted_datetime = d.strftime("%Y-%m-%d %H:%M:%S")


print(f"iso_formatted_datetime: {iso_formatted_datetime}")
print(f"formatted_date_only: {formatted_date_only}")
print(f"formatted_datetime: {formatted_datetime}")""",
                },
                {
                    "title": "Parse String to Date",
                    "py_can_run": True,
                    "code": """from datetime import datetime
d1 = datetime.fromisoformat('2024-05-24T10:30:00')
d2 = datetime.strptime('Jun 24, 2024 10:30:00', '%b %d, %Y %H:%M:%S')
d3 = datetime.fromtimestamp(1716528123.456789)

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}")""",
                },
                {
                    "title": "Work with Timezones",
                    "py_can_run": True,
                    "code": """from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime.now(timezone.utc)
utc_now_isoformat = utc_now.isoformat()
print(f"utc_now: {utc_now}")
print(f"utc_now_isoformat: {utc_now_isoformat}")

ist = datetime.now(ZoneInfo('Asia/Kolkata'))
print(f"ist: {ist}")""",
                },
                {
                    "title": "Date  Arithmetic",
                    "py_can_run": True,
                    "code": """from datetime import datetime, timedelta

d = datetime(2024, 5, 24, 10, 30, 0)
next_day = d + timedelta(days=1)

print(f"d: {d}")
print(f"next_day: {next_day}")

diff = next_day - d
diff_seconds = diff.total_seconds()

print(f"diff: {diff}")
print(f"diff_seconds: {diff_seconds}")""",
                },
                {
                    "title": "Compare Dates",
                    "py_can_run": True,
                    "code": """from datetime import datetime
                
a = datetime(2024, 5, 24)
b = datetime(2024, 5, 25)
c = datetime(2024, 5, 26)
d = datetime(2024, 5, 26)

print(f"a < b: {a < b}")
print(f"a == b: {a == b}")
print(f"c > a: {c > a}")
print(f"c == d: {c == d}")""",
                },
                {
                    "title": "Extract Date Components",
                    "py_can_run": True,
                    "code": """from datetime import datetime
    
d = datetime(2024, 5, 24, 10, 30, 0)

print(f"year: {d.year}")
print(f"month: {d.month}")
print(f"day: {d.day}")
print(f"hour: {d.hour}")
print(f"minute: {d.minute}")
print(f"d.second: {d.second}")""",
                },
                {
                    "title": "Start & End of Day",
                    "py_can_run": True,
                    "code": """from datetime import datetime, time
                
d = datetime.now()
start_day = datetime.combine(d.date(), time.min)
end_day = datetime.combine(d.date(), time.max)

print(f"d: {d}")
print(f"start_day: {start_day}")
print(f"end_day: {end_day}")""",
                },
                {
                    "title": "Weekday",
                    "py_can_run": True,
                    "code": """from datetime import date
            
d = date(2024, 5, 24)

# 4 (Mon-0 ... Sun-6)
weekday = d.weekday()

# 5 (Mon-1 ... Sun-7)
iso_weekday = d.isoweekday()

print(f"weekday: {weekday}")
print(f"iso_weekday: {iso_weekday}")""",
                },
                {
                    "title": "Leap Year Check",
                    "py_can_run": True,
                    "code": """from calendar import isleap
                
is_leap_year = isleap(2024)
print(f"is_leap_year: {is_leap_year}")""",
                },
            ],
            "py_notes": """**strftime** / **strptime** Format Codes
| Code | Meaning |
| -------- | ------- |
| %Y | 4-digit year (e.g. 2024) |
| %m | Month as zero-padded number (01-12) |
| %b | Abbreviated month name (Jan-Dec) |
| %B | Full month name (January-December) |
| %d | Day of month (01-31) |
| %H | Hour (24-hour clock) (00-23) |
| %l | Hour (12-hour clock) (01-12) |
| %M | Minute (00-59) |
| %S | Second (00-59) |
| %f | Microsecond (000000-999999) |
| %p | AM or PM |
| %z | UTC offset like +05:30 |
| %Z | Timezone name |
""",
        },
    ]


@st.cache_data
def get_sidebar_options():
    return [
        "Variables",
        "Data Types",
        "Output & Comments",
        "Operators",
        "Control Flow",
        "Import Modules",
        "String",
        "Functions",
        "List (Array)",
        "Dictionary (Object)",
        "Set",
        "Classes",
        "Typed Hints",
        "Error Handling",
        "JSON",
        "HTTP Requests",
        "Async Operations",
        "Date & Time",
    ]


py_cheatsheet_config: list[dict[str | str]] = get_py_code_config()
sidebar_options = get_sidebar_options()


class StreamlitCallbackWriter:
    def __init__(self, buffer, output_label, placeholder):
        self.buffer = buffer
        self.output_label = output_label
        self.placeholder = placeholder

    def write(self, data):
        if not self.buffer:
            self.output_label.success("Output")
        self.buffer.append(data)
        self.placeholder.code(
            "".join(self.buffer.copy()), wrap_lines=True, language="text"
        )

    def flush(self):
        pass


class PySubChapter:
    def __init__(self, key: str, index: int, py_config_value: dict):
        self.key = key
        self.index = index
        self.py_code = st.session_state
        self.py_code_key = f"py_code_{self.key}_{self.index}"
        self.py_config_value = py_config_value

        self.editor_key = f"code_editor_{self.key}-{self.index}"
        self.namespace = {"__builtins__": __import__("builtins")}

    @st.fragment
    def render(self):
        if "title" in self.py_config_value:
            if self.index not in [0, 1]:
                st.divider()
            st.markdown(f"##### {self.py_config_value["title"]}")
        if "desc" in self.py_config_value:
            st.text(self.py_config_value["desc"])
        if "code" in self.py_config_value:
            with st.expander(
                "Playground", expanded=True, key=f"playground_{self.key}-{self.index}"
            ):
                self.py_code[self.py_code_key] = code_editor(
                    self.py_config_value.get("code", ""),
                    lang="python",
                    response_mode="default",
                    allow_reset=True,
                    options={
                        "showLineNumbers": True,
                        "showGutter": True,
                        "fixedWidthGutter": True,
                        "wrap": True,
                    },
                    buttons=(
                        [
                            {
                                "name": "Copy",
                                "feather": "Copy",
                                "alwaysOn": False,
                                "class": "copy-btn",
                                "style": {
                                    "top": "0.44rem",
                                    "right": "0.4rem",
                                },
                                "commands": [
                                    "copyAll",
                                ],
                            },
                            *(
                                [
                                    {
                                        "name": "Run",
                                        "feather": "Play",
                                        "primary": False,
                                        "hasText": True,
                                        "hasSecondary": True,
                                        "showWithIcon": True,
                                        "alwaysOn": False,
                                        "style": {
                                            "font-size": "0.9rem",
                                            "top": "0.44rem",
                                            "right": "2.7rem",
                                            "background-color": "#ff4500d0",
                                            "padding": "0px !important",
                                            "margin": "0px",
                                            "border-radius": "10px",
                                        },
                                        "commands": ["submit"],
                                    }
                                ]
                                if self.py_config_value.get("py_can_run", False)
                                else []
                            ),
                        ]
                    ),
                    key=f"code_editor_{self.key}-{self.index}",
                )

                if (
                    self.py_code_key in self.py_code
                    and self.py_code[self.py_code_key]
                    and "text" in self.py_code[self.py_code_key]
                    and self.py_code[self.py_code_key].get("type") == "submit"
                ):

                    self.py_code_output_key = f"py_code_output-{self.key}_{self.index}"
                    self.py_code_output_label_key = (
                        f"output_label-{self.key}_{self.index}"
                    )
                    self.py_code_output_placeholder_key = (
                        f"output_placeholder-{self.key}_{self.index}"
                    )

                    if self.py_code_output_label_key not in self.py_code:
                        self.py_code[self.py_code_output_label_key] = st.empty()

                    if self.py_code_output_placeholder_key not in self.py_code:
                        self.py_code[self.py_code_output_placeholder_key] = st.empty()

                    self.py_code[self.py_code_output_key] = {}

                    self.py_code[self.py_code_output_key] = self.run_py_code(
                        self.py_code[self.py_code_key]["text"],
                        self.py_code[self.py_code_output_label_key],
                        self.py_code[self.py_code_output_placeholder_key],
                    )

                    if "output" in self.py_code[self.py_code_output_key]:
                        self.py_code[self.py_code_output_placeholder_key].empty()
                        st.success("Output")
                        st.code(
                            self.py_code[self.py_code_output_key]["output"],
                            wrap_lines=True,
                            language="text",
                        )

                    if "error" in self.py_code[self.py_code_output_key]:
                        st.error(
                            f"**Error**: {self.py_code[self.py_code_output_key]["error"]}"
                        )

        if "notes" in self.py_config_value:
            st.markdown(self.py_config_value["notes"])

    def run_py_code(self, code: str, output_label, output_placeholder):

        self.output_list = []
        self.writer = StreamlitCallbackWriter(
            self.output_list, output_label, output_placeholder
        )
        try:
            with contextlib.redirect_stdout(self.writer):
                exec(code, self.namespace, self.namespace)
                return {}
        except Exception as e:
            return {
                **({"output": "".join(self.output_list)} if self.output_list else {}),
                "error": str(e),
            }


@st.fragment
def py_chapter_tab(
    py_code_config,
    py_notes=None,
    key="default",
):
    left_child = None
    right_child = None
    for index, config_value in enumerate((py_code_config)):
        if index % 2 == 0:
            left_child, right_child = st.columns(2)
        with left_child:
            if index % 2 == 0:
                PySubChapter(key, index, config_value).render()
        with right_child:
            if index % 2 == 1:
                PySubChapter(key, index, config_value).render()
            if py_notes and index == (len(py_code_config) - 1) and index % 2 == 0:
                st.divider()
                st.write("##### General Notes:")
                with st.container(border=True):
                    st.markdown(py_notes)

    if py_notes and (len(py_code_config) - 1) % 2 == 1:
        left_notes, _ = st.columns(2)
        with left_notes:
            st.divider()
            st.write("##### General Notes:")
            with st.container(border=True):
                st.markdown(py_notes)


@st.fragment
def render_chapter(selected_section_: str):
    if selected_section_ in sidebar_options:
        option_index = sidebar_options.index(selected_section_)
        st.subheader(
            f"Python Quick Ref : {selected_section_}",
            width="content",
            text_alignment="center",
            divider=True,
            anchor=False,
        )

        with st.container(
            border=False, horizontal=True, vertical_alignment="center", width="content"
        ):
            st.markdown(
                "Developed by: **Samir Solanki** | [Linkedin](https://linkedin.com/in/samir38) | [Portfolio](https://noto.li/fxHVPg)"
            )

        py_cs_config = py_cheatsheet_config[option_index]
        if py_cs_config:
            py_chapter_tab(
                key=py_cs_config["key"],
                py_code_config=py_cs_config["py_code_config"],
                py_notes=py_cs_config.get("py_notes", None),
            )


preselected_chapter = "Variables"


def render_sidebar_sections():
    st.header("Quick Ref Menu", width="content", divider=True, anchor=False)
    st.session_state["selected_section"] = option_menu(
        menu_title=None,
        options=sidebar_options,
        icons=[None for n in sidebar_options],
        menu_icon="list",
        default_index=sidebar_options.index(preselected_chapter),
        orientation="vertical",
        styles={
            "icon": {"visibility": "hidden"},
            "container": {"padding": "10px!important"},
            "nav-link": {
                "margin": "0px",
            },
            "nav-link-selected": {"margin": "0px"},
        },
    )


st.set_page_config(layout="wide")
with st.sidebar:
    render_sidebar_sections()

render_chapter(st.session_state["selected_section"])
