from typing import List
from random import randint


# 실패한 문제...
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        mp = {0: 0}
        prefix = 0
        # mp[지금까지의 합] = 위치
        for i, num in enumerate(nums, 1):
            prefix += num
            mp[prefix] = i

        ans = mp.get(x, float('inf'))
        # mp에 합 x가 존재하면 해당 위치 아니면 'inf'
        for i, num in enumerate(reversed(nums), 1):
            # 뒤부터 진행
            x -= num
            # mp에 합이 x인 위치를 기억하고 있으면 앞에서의 위치 + 뒤에서의 위치 <= 배열의 길이
            if x in mp and mp[x] + i <= len(nums):
                ans = min(ans, i + mp[x])
        return ans if ans < float('inf') else -1


if __name__ == "__main__":
    # nums = [randint(1, 10) for _ in range(10)]
    # x = randint(10, 100)
    nums = [5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996,
            8902, 228, 4461, 90, 7321, 7893, 4879, 9987, 1146, 8177, 1073, 7254, 5088, 402, 4266, 6443, 3084, 1403,
            5357, 2565, 3470, 3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530, 9630, 1521,
            2174, 5027, 4833, 3483, 445, 8300, 3194, 8784, 279, 3097, 1491, 9864, 4992, 6164, 2043, 5364, 9192, 9649,
            9944, 7230, 7224, 585, 3722, 5628, 4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968,
            9983, 3540, 9224, 6216, 9665, 8070, 31, 3555, 4198, 2626, 9553, 9724, 4503, 1951, 9980, 3975, 6025, 8928,
            2952, 911, 3674, 6620, 3745, 6548, 4985, 5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639]
    x = 565610
    print(nums)
    print(x)
    print(Solution().minOperations(nums, x))
