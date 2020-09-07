from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        dic = {}
        for tr in transactions:
            name, time, amount, city = tr.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                invalid.append(tr)

            if name not in dic:
                dic[name] = (time, amount, city)
            else:
                print(name, dic[name])
                prevTime, prevAmount, prevCity = dic[name]
                if prevCity != city:
                    if abs(time - prevTime) <= 60:
                        inputs = f'{name},{prevTime},{prevAmount},{prevCity}'
                        if inputs not in invalid:
                            invalid.append(inputs)
                        if tr not in invalid:
                            invalid.append(tr)
                    else:
                        dic[name] = (time, amount, city)
                else:
                    dic[name] = (time, amount, city)
        return invalid


if __name__ == '__main__':
    s = Solution()
    result = s.invalidTransactions(["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona",
                                    "alex,587,402,bangkok", "chalicefy,973,830,barcelona", "alex,932,86,bangkok",
                                    "bob,188,989,amsterdam"])
    print(result)