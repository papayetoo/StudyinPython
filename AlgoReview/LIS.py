from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int])->int:
        # DP 방법을 이용한 풀이방법
        # 두 가진 단점이 존재한다고 생각됨
        # 첫 번재는 사소하지만, 최장 증가 수열이 무엇인지 이 풀이만으로는 알 수가 없음.
        # 두 번째 시간복잡도가 n^2임.
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) if len(nums) > 0 else 0


    def lengthOfLIS2(self, nums: List[int])->int:
        # 두 번째 풀이방법은 이분 탐색(Binary Search)를 이용한 방법입니다.
        # 두 번째 풀이의 장점은 첫 번째 풀이의 단점 두 가지 모두를 없앨 수 있습니다.
        lis = [nums[0]]
        ans = [(0, nums[0])]
        for i in range(1, len(nums)):
            if lis[-1] < nums[i]:
                ans.append((len(lis), nums[i]))
                lis.append(nums[i])
            elif lis[-1] > nums[i]:
                # 이진탐색을 통해 nums[i]를 집어넣을 위치를 찾은 후에
                # lis[insertPos]를 nums[i]로 치환한다.
                insertPos = bisect.bisect_left(lis, nums[i])
                lis[insertPos] = nums[i]
                ans.append((insertPos, nums[i]))
        print(ans)
        print(lis)
        ans.reverse()
        t = len(lis) - 1
        s = []
        for i in range(len(ans)):
            if ans[i][0] == t:
                s.append(ans[i][1])
                t -= 1
        print(s.reverse())
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    # nums = [10,20,40,25,15,16,17,18,20]
    nums = [10,20,40,25,15,50,30,70]
    s.lengthOfLIS2(nums)