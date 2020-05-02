# 초콜릿과 건포도

f = open('sample_input.txt','r')

testcase = int(f.readline())

for _ in range(testcase):
    n, m = map(int, f.readline().split())
    curchocolate = [list(map(int, f.readline().split())) for _ in range(n)]

    sumarr = []
