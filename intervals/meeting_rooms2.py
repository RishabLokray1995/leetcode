#Q: https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = list()

        sorted_starts = sorted([i[0] for i in intervals])
        sorted_ends = sorted([i[1] for i in intervals])
        count = 0
        i = 0
        j = 0
        while i < len(sorted_starts):
            if (sorted_starts[i] >= sorted_ends[j]):
                count -= 1
                j += 1
            else:
                i += 1
                count += 1

        return count



