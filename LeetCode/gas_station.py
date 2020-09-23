class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            n = len(gas)

            for i in range(n):
                curGas = gas[i]
                mov = 0
                pos = i
                while mov < n and curGas >= 0:
                    curGas -= cost[pos % n]
                    if curGas < 0:
                        break
                    pos = (pos + 1) % n
                    curGas += gas[pos % n]
                    mov += 1

                if pos == i and mov == n:
                    return i
            return -1