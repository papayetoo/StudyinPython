class Solution:
    def distributeCandies(self, candies: int, num_people:int):
        answer = [0] * num_people
        candy = 1
        cur = 0
        while candies > 0:
            answer[cur % num_people] += candy if candies > candy else candies
            cur += 1
            candies -= 1
            candy += 1
        return answer
