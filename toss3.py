# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
user_input = input()
paren_lst = [x for x in user_input]
paren_lst.index
result_q = deque()
for paren in paren_lst:
    if paren == '(' or paren == '{':
        result_q.append(paren)
    elif (paren == ')' or paren == '}') and len(result_q) == 0:
        result_q.append(paren)
    elif paren == ')' and len(result_q) > 0 and result_q[-1] == '(':
        result_q.pop()
    elif paren == '}' and len(result_q) > 0 and result_q[-1] == '{':
        result_q.pop()

if len(result_q) == 0:
    print('True')
else:
    print('False')