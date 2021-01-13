from typing import List
from collections import deque, Counter


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        start = count = 0
        end = len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            count += 1
        return count


if __name__ == "__main__":
    # people = [5, 1, 4, 2]
    # people = [3, 5, 3, 4]
    people = [3, 2, 2, 1]
    # limit = 3
    limit = 8
    print(Solution().numRescueBoats(people, limit))
