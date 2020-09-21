from operator import itemgetter
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sortedTrip = sorted(trips, key=itemgetter(1, 2))
        endTime = max(sortedTrip, key=itemgetter(2))[2]
        passengers = [0] * (endTime + 1)

        for curPassenger, start, end in sortedTrip:
            for i in range(start, end):
                passengers[i] += curPassenger
        answer = [x for x in passengers if x > capacity]
        return True if len(answer) == 0 else False

