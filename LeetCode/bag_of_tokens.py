from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:

        # score >= 1 이다 -> 가장 큰 token을 찾아서 face down
        # score = 0 인데 currentPower가 tokens[i] 보다 크다면 face up해서 score을 얻는다.

        # Making list as an ascending order list
        tokens.sort()

        currentPower = P
        score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if currentPower >= tokens[left]:
                # Face Up
                # used[tokens[left]] = True
                score += 1
                currentPower -= tokens[left]
                left += 1
                continue
            elif currentPower < tokens[left]:
                # Face Down
                # used[tokens[right]] = True
                if left == right:
                    # 현재 score를 face down 하며은 더 작은 score을 얻는다.
                    return score

                if score >= 1:
                    score -= 1
                    currentPower += tokens[right]
                    right -= 1
                    continue
                else:
                    return score
        return score


if __name__ == "__main__":
    tokens = [100, 200, 300, 400]
    # tokens = [100, 200]
    P = 150
    print(Solution().bagOfTokensScore(tokens, P))