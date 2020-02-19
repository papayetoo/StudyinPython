s = input()
def myAtoi(s:str):
    MINUS_SIGN = '-'
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2,31)
    arr = list(s.strip().split())
    first = arr[0]
    def is_digit(str):
        try:
            tmp = float(str)
            return True
        except ValueError:
            return False

    if is_digit(first) is True:
        if float(first) > INT_MAX:
            return INT_MAX
        elif float(first) < INT_MIN:
            return INT_MIN
        return int(float(first))
    else:
        return 0
print(myAtoi(s))