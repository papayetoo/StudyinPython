from functools import reduce
# 람다 표현식 사용하기
# 일반 함
def plus_ten(x):
    return x + 10
print(plus_ten(1))

# plus_ten의 람다 표현식 사용하기
lambdas_way = lambda x: x + 10
print(lambdas_way(1))
# 람다 표현식 안에서는 변수를 만들지 못함
# lamda x : y = 10; x + y 이런 식이면 오류 발생

# 람다 표현식을 인수로 사용하기
lst = [i for i in range(1, 9)]
mullst = list(map(lambda x : x * 2 , lst))
# print(mullst)

# map 에 객체를 여러 개 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
c = list(map(lambda x, y: x * y, a, b))

# filter 사용하기
def f(x:int):
    return x > 5 and x < 10
# 함수를 사용하는 방법
# print(list(filter(f, b)))
# 람다 표현식을 사용하는 방법
print(list(filter(lambda x: x > 5 and x < 10, b)))

# reduce 사용하기
def f(x, y):
    return x + y

a = [1,2,3,4,5]
#함수 사용 버젼
sumA = reduce(f, a)
print(sumA)

# practice 1
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
newlst = list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files))
# print(newlst)

# pratice2
files2 = ['1.jpg', '10.png', '11.png', '2.jpg', '3.png']
newlst2 = list(map(lambda x: x.split('.')[0].zfill(3) +'.' + x.split('.')[1], files2))
print(newlst2)