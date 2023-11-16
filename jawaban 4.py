def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: division by zero"

result = divide(10, 2)
print(result)

result = divide(10, 0)
print(result)
