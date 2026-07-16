# Q: https://leetcode.com/problems/interval-list-intersections/

# O(N+M)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if (len(firstList) == 0 or len(secondList) == 0): return []
        first = 0
        second = 0
        intersection = list()
        heap = [(firstList[0], 1), (secondList[0], 2)]
        heapify(heap)

        while (first < len(firstList) and second < len(secondList)):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])

            if start <= end:
                intersection.append([start, end])

            if (firstList[first][1] < secondList[second][1]):
                first += 1
            else:
                second += 1
        return intersection