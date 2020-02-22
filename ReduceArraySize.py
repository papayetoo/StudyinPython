# Problemn description :
# Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.
from collections import Counter
def minSetSize(arr:list[str]) ->int:
    answer = 0
    removeSize = len(arr)
    for element, count in Counter(arr).most_common():
        removeSize -= count
        answer += 1
        if removeSize >= int(len(arr)/2) :
            break
    return answer
