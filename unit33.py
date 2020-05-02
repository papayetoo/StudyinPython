def calc():
    a = 3
    b = 5
    # def mul_add(x):
    #     return a * x + a
    # return mul_add
    return lambda x : a * x + b

c = calc()
print(c(1), c(2), c(3), c(4), c(5))