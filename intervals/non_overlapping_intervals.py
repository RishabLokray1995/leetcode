# Pattern: sort by end time intervals. O(NlogN) / Greedy
#Q: https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        res = list()

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        j = 0
        while j < len(sorted_intervals):
            if (len(res) == 0):
                res.append(sorted_intervals[j])
            else:
                if (sorted_intervals[j][0] < res[-1][1]):
                    count += 1
                else:
                    res.append(sorted_intervals[j])
            j += 1
        return count








