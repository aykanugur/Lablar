def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except Exception:
        return "Error"
def power(x, y):
    return x ** y
def mod(x, y):
    try:
        return x % y
    except Exception:
        return "Error"

if __name__ == "__main__":
    print('work in main')