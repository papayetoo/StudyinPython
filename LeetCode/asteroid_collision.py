from typing import List
# 스택 문제

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            currentAsteroid = asteroids[i]
            if not q:
                q.append(currentAsteroid)
                continue
            if q[-1] * currentAsteroid > 0:
                q.append(currentAsteroid)
                continue
            elif q[-1] < 0 and currentAsteroid > 0:
                q.append(currentAsteroid)
                continue
            elif q[-1] > 0 and currentAsteroid < 0:
                # 큰 절대값 전까지 모두 pop
                while q and currentAsteroid * q[-1] < 0 and abs(currentAsteroid) > q[-1]:
                    q.pop()
                # 큐가 존재한다면 append
                if q:
                    if q[-1] * currentAsteroid > 0:
                        q.append(currentAsteroid)
                        continue
                    if abs(q[-1]) < abs(currentAsteroid):
                        q.pop()
                        q.append(currentAsteroid)
                        continue
                    if abs(q[-1]) == abs(currentAsteroid):
                        q.pop()
                        continue
                else:
                    q.append(currentAsteroid)
                    continue

        return q



