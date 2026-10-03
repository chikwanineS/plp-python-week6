````markdown
# PLP Python Week 6 Assignment

## Assignment Title

Week 6 Assignment - Safe Functions and Error Handling

## Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.
- `unbreakable.py` - Demonstrates how try/except can prevent a program from crashing when errors occur.
- `README.md` - Contains information about the assignment and explains how error handling works.

## Why can the if check not catch "abc" on its own?

An `if` check can test a condition, but it cannot catch the `ValueError` that occurs when Python tries to convert `"abc"` into an integer using `int()`. The `try/except` block is needed to catch the error and allow the program to continue running.

## Expected Output

```text
5.0
Cannot divide by zero
42
Not a number
82
Field not found
````

## Concepts Practiced

* try/except
* ZeroDivisionError
* ValueError
* KeyError
* Functions
* Return values
* Error handling

```
```
