# unit25 dictionary 응용하기
x = {'a' : 10, 'b': 20, 'c': 30, 'd': 40}
# 키 - 값 쌍 추가하기
x.setdefault('e') # 키 - 값 추가 1 키만 추가
x.setdefault('f', 100) # 키 - 값 추가 2 키 값 추가

# 키 값 수정하기
x.update(a=90)
x.update(e=50) # 키 값이 있으면 수정, 없으면 'e':50 추가
x.update(a=900, f=60) # 키-값 쌍 여러 개를 한꺼번에 수정.

# 키-값 쌍 삭제하기
x.pop('a') # 키-값 쌍 삭제하기 1
del x['b'] # 키-값 쌍 삭제하기 2

# 임의의 키-값 쌍 삭제하기
print(x)
x.popitem() # 파이썬 3.6 기준 마지막 키-값 쌍을 삭제.
print(x)

# 모든 키-값 쌍 삭제하기
# x.clear()

# 키-값 상을 모두 가져오기
print(x.items()) #  키 - 값 쌍을 모두 가져옴.
print(x.keys()) # 키만 가져옴.
print(x.values()) # 값만 가져옴.

# 리스트와 튜플로 딕셔너리 만들기
keys =['a','b','c','d']
# x = dict.fromkeys(keys) 리스트 또는 튜플로 딕셔너리 만들기1
x = dict.fromkeys(keys) # 리스트 또는 튜플로 딕셔너리 만들기2 모든 값을 100으로 초기화.

# 딕셔너리의 키-값 쌍을 모두 출력하기
for key,value in x.items():
    print(key, value, sep=' ', end= '\n')

# 딕셔너리 표현식 사용하기
x = {keys[i]: i + 1 for i in range(len(keys))}

# 딕셔너리의 할당과 복사
# y = x # x 와 y는 같은 딕셔너리
y = x.copy() # x 와 y는 다른 딕셔너리.
y['a'] = 99 # x에 아무런 영향이 없음.
if x is y:
    print('같은 딕셔너리입니다.')
else:
    print('다른 딕셔너리 입니다.')
print('x는 ',end=' ')
print(x)
print('y는 ',end=' ')
print(y)

# practice 1 평균 점수 구하기
maria = {'korean' : 94, 'english': 91, 'mathmatics':89, 'science': 83}
average = sum(maria.values())/len(maria)
print(average)

# practice 2 딕셔너리에서 특정 값 삭제하기
names = list(input().split())
numKeys = list(map(int, input().split()))
prac2Dic = dict(zip(names, numKeys))
copyDic = prac2Dic.copy()
for key,value in copyDic.items():
    if key == 'delta':
        del prac2Dic[key]
    if value == 30:
        del prac2Dic[key]
print(prac2Dic)