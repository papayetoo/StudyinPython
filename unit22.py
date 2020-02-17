a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel','india']
b = [i for i in a if len(i) == 5]
print(b)

n, m = map(int, input().split()) # 1 10
answer = [ pow(2,i) for i in range(n, m + 1)]
print(answer)