import itertools, queue
def generateParenthesis(n: int):
    parens = '()' * n
    permlst = list(itertools.permutations(parens, n * 2))
    def valid(s:str):
        q = []
        for c in s:
            if c == '(':
                q.append(c)
            elif len(q) - 1 >= 0 and c ==')' and q[len(q) - 1] =='(':
                q.pop()
        if len(q) == 0:
            return True
        else:
            return False
    ans = []
    for s in permlst:
        joinS = ''.join(s)
        if valid(joinS) is True:
            ans.append(joinS)
    return list(set(ans))

generateParenthesis(int(input()))
