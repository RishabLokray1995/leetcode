#Q: https://leetcode.com/problems/meeting-rooms/
#O(N) O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        for i, val in enumerate(sorted_intervals):
            if (i == len(sorted_intervals) - 1): break

            if sorted_intervals[i + 1][0] < sorted_intervals[i][1]:
                return False

        return True


