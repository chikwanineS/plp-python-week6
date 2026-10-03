```python
def safe_input_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_input_number("25"))
print(safe_input_number("abc"))
print(safe_division(20, 4))
print(safe_division(20, 0))
```
