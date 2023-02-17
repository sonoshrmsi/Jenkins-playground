def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divde(a,b):
    if a/b:
        return a/b
    else:
        raise {"message": "Division by zero is not possible"}