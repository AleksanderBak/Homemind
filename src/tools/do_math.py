def do_math(a: int, op: str, b: int) -> str:
    """
    Do basic math operations
    a: The first operand
    op: The operation to perform (one of '+', '-', '*', '/')
    b: The second operand
    """
    res = "Nan"
    if op == "+":
        res = str(int(a) + int(b))
    elif op == "-":
        res = str(int(a) - int(b))
    elif op == "*":
        res = str(int(a) * int(b))
    elif op == "/":
        if int(b) != 0:
            res = str(int(a) / int(b))
    return res
