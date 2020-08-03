# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
a, b, c = user_input.split()
a = int(a)
b = int(b)
c = int(c)

count = 1
for n in range(a, b + 1):
    tmp_count = 1
    if n == 1:
        continue
    else:
        while n != 1:
            tmp_count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
                if b / 3 < n and c > 0:
                    n = n + 10
                    c = c - 1
    count = max(count, tmp_count)
print(count)

