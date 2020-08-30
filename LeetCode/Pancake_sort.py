from typing import List
class Solution:
    def pancakeSort(self, arr: List[int])->List[int]:
        length = len(arr)
        i = length - 1
        answer = []
        while length >= 1:
            max_val = length
            max_index = arr.index(length)
            if max_val != max_index + 1:
                arr = arr[:max_index+1][::-1] + arr[max_index+1:]
                answer.append(max_index+1)
                arr = arr[:length][::-1] + arr[length:]
                answer.append(length)
            length -= 1
        return answer


if  __name__ == '__main__':
    arr = [3,2,4,1]
    s = Solution()
    answer = s.pancakeSort(arr)
    print(answer)