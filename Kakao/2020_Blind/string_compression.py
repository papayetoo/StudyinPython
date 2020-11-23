def solution(s):
    answer = 10000
    n = len(s)
    if n == 1:
        return 1

    for i in range(1, n // 2 + 1):
        output = ''
        prev = None
        count = 1
        for j in range(0, n, i):

            if not prev:
                prev = s[j:j + i]
                continue

            if prev and s[j:j + i] == prev:
                count += 1
                if j + i >= n:
                    output += f'{count}{prev}'
                    j += i
            else:
                if count > 1:
                    output += f'{count}{prev}'
                else:
                    output += prev
                prev = s[j:j + i]
                count = 1
        if j < n:
            output += f'{count}{prev}' if count > 1 else prev
        answer = min(answer, len(output))
    return answer