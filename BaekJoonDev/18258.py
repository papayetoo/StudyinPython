import sys
class Queue:
    def __init__(self):
        self.q = []
        self.f = -1
        self.b = -1

    def push(self, n: int):
        self.q.append(n)
        self.i = 1
        self.f += self.i

    def pop(self):
        ret = self.q[self.b]
        self.b -= 1
        return ret

    def front(self):
        return self.q[self.f]

    def back(self):
        return self.q[-1]

    def size(self):
        return len(self.q) - self.f - 1

    def empty(self):
        return 0 if self.size() else 1


if __name__ == '__main__':
    n = int(input())
    q = Queue()
    for _ in range(n):
        ops = sys.stdin.readline().split()
        if len(ops) == 1:
            order = ops[0]
            if order == 'front':
                print(q.front())
            elif order == 'back':
                print(q.back())
            elif order == 'empty':
                print(q.empty())
            elif order == 'pop':
                print(q.pop())
            elif order == 'size':
                print(q.size())
        else:
            q.push(int(ops[1]))
            print(ops[1])