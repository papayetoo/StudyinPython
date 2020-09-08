from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for i, t1 in enumerate(transactions):
            name1, time1, amount1, city1 = t1.split(',')
            if int(amount1) > 1000:
                invalid.append(t1)
                continue
            for j, t2 in enumerate(transactions):
                if i != j:
                    name2, time2, amount2, city2 = t2.split(',')
                    if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                        invalid.append(t1)
                        break

        return invalid



if __name__ == '__main__':
    s = Solution()
    transactions = ["xnova,261,1949,chicago","bob,206,1284,chicago","xnova,420,996,bangkok","chalicefy,704,1269,chicago","iris,124,329,bangkok","xnova,791,700,amsterdam","chalicefy,572,697,budapest","chalicefy,231,310,chicago","chalicefy,763,857,chicago","maybe,837,198,amsterdam","lee,99,940,bangkok","bob,132,1219,barcelona","lee,69,857,barcelona","lee,607,275,budapest","chalicefy,709,1171,amsterdam"]
    result = s.invalidTransactions(transactions)

    print(result)
