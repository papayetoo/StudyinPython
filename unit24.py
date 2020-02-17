# 문자열 바꾸기
print('Hello world'.replace('world', 'python'))
# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
# 구분자 문자열과 문자열 리스트 연결하기
s ='-'.join(['apple', 'pear', 'grape', 'pineapple', 'oragne'])
# 공백 삭제하기
testStr = '      python .,'
print(testStr)
print(testStr.lstrip())
print(testStr.rstrip('.,') + 'world')

# 문자열 개수 세기
p1count = 'apple pineapple'.count('pl')
print(p1count)

# 서식 지정자 사용하기
formatstr = 'I am %s'
print(formatstr % 'maria')

# format 메서드 사용하기
formatstr = 'Hello, {0}'.format('world!')
print(formatstr)
# format - 1
formatstr = 'Hello, {language} {version}'.format(language='Python', version=3.6)
print(formatstr)

# format method
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

# practice 1
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
lastIndex = path.rindex('\\')
filename = path[lastIndex + 1:]
print(filename)

# practice 3 높은 가격순으로 출력하기
stdin = '51900;83000;15800;367500;250000;59200;128500;1304000'
answer = list(map(int, stdin.split(';')))
answer.sort(reverse=True)
for ans in answer:
    print('{0:>9,}'.format(ans))