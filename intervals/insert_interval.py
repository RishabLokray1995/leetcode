#Q: https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        len_intervals = len(intervals)

        if (len_intervals == 0 and len(newInterval) != 0):
            return [newInterval]

        # find position newInterval fits
        should_merge = True
        i = 0
        while i < len_intervals:
            if newInterval[0] <= intervals[i][1]:
                if (newInterval[1] < intervals[i][0]):
                    should_merge = False
                break
            i += 1

        pos = i
        if (pos >= len_intervals):
            intervals.append(newInterval)
            return intervals

        res = list()
        for j in range(len_intervals):
            if (j == pos):
                if should_merge == True:
                    start = min(newInterval[0], intervals[j][0])
                    end = max(newInterval[1], intervals[j][1])
                    res.append([start, end])
                else:
                    res.append(newInterval)

            # take last one from res and merge interval{j} with it.
            if (len(res) >= 1 and intervals[j][0] <= res[-1][1]):
                last_res = res[-1]
                start = last_res[0]
                end = max(last_res[1], intervals[j][1])
                res.pop()
                res.append([start, end])
            else:
                res.append(intervals[j])
        return res











