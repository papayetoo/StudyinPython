class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [i for i in range(1, 10)]
        visited = []
        answers = []

        def combination(arr: list, target: int, index: int, depth: int):
            if index > len(arr) or target < 0:
                return

            if depth == 0 and target == 0:
                tmp = []
                for i in visited:
                    tmp.append(arr[i])
                answers.append(tmp)
                return

            visited.append(index)
            if index < len(arr):
                combination(arr, target - arr[index], index + 1, depth - 1)
            visited.pop()
            combination(arr, target, index + 1, depth)

        combination(numbers, n, 0, k)
        return answers