import heapq
from collections import deque


class Kiosk:
    def __init__(self, num: int):
        self.num = num
        self.numOfDate = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.customerNumber = 0

    def work(self, customer_date: str):
        curDt, curTm, workTm = customer_date.split()
        month, date = map(int, curDt.split('/'))
        hour, minute, sec = map(int, curTm.split(':'))
        minute += int(workTm)
        # 60분 넘겼을 때 처리
        if minute >= 60:
            minute -= 60
            hour += 1
            # 하루를 넘길 때 처리
            if hour == 24:
                hour = 0
                if self.numOfDate[month] > date:
                    date += 1
                elif self.numOfDate[month] == date:
                    date = 1
                    month += 1
        self.endDt = f'{month:02d}/{date:02d}'
        self.endTm = f'{hour:02d}:{minute:02d}:{sec}'
        self.customerNumber += 1


numOfDate = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def calEndTime(arrival: str):
    curDt, curTm, workTm = arrival.split()
    month, date = map(int, curDt.split('/'))
    hour, minute, sec = map(int, curTm.split(':'))
    minute += int(workTm)
    # 60분 넘겼을 때 처리
    if minute >= 60:
        minute -= 60
        hour += 1
        # 하루를 넘길 때 처리
        if hour == 24:
            hour = 0
            if numOfDate[month] > date:
                date += 1
            elif numOfDate[month] == date:
                date = 1
                month += 1
    endDt = f'{month:02d}/{date:02d}'
    endTm = f'{hour:02d}:{minute:02d}:{sec}'
    endSec = calSec(endTm) + (month * 30 + date) * 24 * 3600
    return endSec


def calSec(tm):
    result = 0
    hour, minute, sec = map(int, tm.split(':'))
    result += sec
    result += 60 * minute
    result += hour * (60 ** 2)
    return result


def solution(n, customers):
    # 종료시각(초), 처리한 고객수, 인덱스,
    kiosk = [[-float('inf'), 0, i] for i in range(n)]
    for customer in customers:
        t = heapq.heappop(kiosk)
        t[0] = calEndTime(customer)
        t[1] += 1
        heapq.heappush(kiosk, t)
        print(t)

    print(kiosk)

if __name__ == '__main__':
    # n = 3
    # customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24",
    #              "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
    n = 2
    customers = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]
    solution(n, customers)
