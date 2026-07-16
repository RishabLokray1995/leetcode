#Q: https://leetcode.com/problems/employee-free-time/
# Can be done using min heap in NlogK 

# # Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        combined_schedule = list()
        for emp in schedule:
            combined_schedule = combined_schedule + emp

        # merge intervals of busy times, after sorting by start times
        combined_schedule = sorted(combined_schedule, key=lambda x: x.start)

        print(f"combined_schedule:{[(x.start, x.end) for x in combined_schedule]}")

        merged_intervals = list()
        i = 0
        while (i < len(combined_schedule)):
            if (len(merged_intervals) == 0 or merged_intervals[-1].end < combined_schedule[i].start):
                merged_intervals.append(combined_schedule[i])
            else:
                end = max(merged_intervals[-1].end, combined_schedule[i].end)
                merged_intervals[-1].end = end
            i += 1

        print(f"merged_schedule:{[(x.start, x.end) for x in merged_intervals]}")

        # find spaces between the busy intervals -> free intervals of all employees

        free_intervals = list()
        if (len(merged_intervals) == 1): return []
        for i in range(1, len(merged_intervals)):
            free_interval = Interval(merged_intervals[i - 1].end, merged_intervals[i].start)
            free_intervals.append(free_interval)
        print(f"free_intervals:{[(x.start, x.end) for x in free_intervals]}")

        return free_intervals













