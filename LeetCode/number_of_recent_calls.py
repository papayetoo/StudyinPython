class RecentCounter:

    def __init__(self):
        self.request = []
        self.count = 0
        self.index = 0

    def ping(self, t: int) -> int:
        self.request.append(t)
        i = self.index
        self.count += 1
        while self.request[i] < self.request[-1] - 3000 and i < len(self.request):
            self.count -= 1
            i += 1
        self.index = i
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)