from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union-Find 알고리즘 사용
        parents = {}
        for index, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                parents[email] = email

        def find(email: str):
            if email == parents[email]:
                return email
            root = find(parents[email])
            parents[email] = root
            return root

        for index, account in enumerate(accounts):
            emails = account[1:]
            n = len(emails)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    u = find(emails[i])
                    v = find(emails[j])
                    if u != v:
                        parents[v] = u

        answer = defaultdict(list)
        for account in accounts:
            name = account[0]
            rootEmail = find(account[1])
            emails = account[1:]
            if name not in answer[(name, rootEmail)]:
                answer[(name, rootEmail)].append(name)
            for email in emails:
                if email not in answer[(name, rootEmail)]:
                    answer[(name, rootEmail)].append(email)
            answer[(name, rootEmail)].sort()
        answer = [x for x in answer.values()]
        return answer