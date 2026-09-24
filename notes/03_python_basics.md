# 3. Python Programming Basics

## What is Python?

Python is a high-level, general-purpose programming language known for readable syntax and a large ecosystem.

It is widely used for:
- AI and ML
- Data analysis
- Web development
- Automation
- Scripting

## 1. Printing Output

```python
print("Hello, AI!")
```

## 2. Variables

A variable stores a value.

```python
name = "Nishant"
age = 20
score = 91.5
is_student = True
```

Common built-in types:
- `str` — text
- `int` — whole number
- `float` — decimal number
- `bool` — True/False

Check a type:

```python
print(type(age))
```

## 3. Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

`input()` returns text. Convert it when a number is required:

```python
age = int(input("Enter your age: "))
```

## 4. Operators

Arithmetic:

```python
a + b
a - b
a * b
a / b
a // b
a % b
a ** b
```

Comparison:

```python
a == b
a != b
a > b
a < b
a >= b
a <= b
```

Logical:

```python
and
or
not
```

## 5. Conditions

```python
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
else:
    grade = "B"

print(grade)
```

## 6. For Loop

```python
for i in range(1, 6):
    print(i)
```

## 7. While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## 8. Lists

Lists store multiple values.

```python
skills = ["Python", "ML", "DL"]
print(skills[0])
skills.append("AI")
```

Useful methods:
- `append()`
- `remove()`
- `pop()`
- `sort()`
- `len()`

## 9. Dictionaries

Dictionaries store key-value pairs.

```python
student = {
    "name": "Nishant",
    "age": 20,
    "course": "B.Tech CSE"
}

print(student["name"])
```

## 10. Functions

Functions group reusable logic.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Nishant")
print(message)
```

## 11. Comments

```python
# This is a single-line comment
```

Comments explain code and are ignored by Python.

## 12. Basic Error Handling

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 13. Running a Python File

From a terminal:

```bash
python filename.py
```

Check Python:

```bash
python --version
```

## Recommended Beginner Practice

Write programs for:
1. Hello World
2. Add two numbers
3. Check even/odd
4. Find largest of three numbers
5. Print numbers 1–10
6. Sum numbers in a list
7. Create a calculator
8. Create a student grade calculator
