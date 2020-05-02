import itertools

arr = [5,5,5,5]
perms = list(itertools.permutations(arr, 4))
result = {}
for p in perms:
    hour = p[0] * 10 + p[1]
    min = p[2] * 10 + p[3]

    if hour >= 24 or min >= 60:
        continue

    if hour not in result.keys():
        result[hour] = min
    else:
        if result[hour] < min :
            result[hour] = min

if len(result) == 0:
    print('')
else:
    sortedResult = sorted(result.items(), key=lambda items: items[0], reverse=True)
    answer = '{}:{}'.format(sortedResult[0][0], sortedResult[0][1])
    print(answer)
