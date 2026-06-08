from ast import List
#Q: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    # One pass Birectional two pointer : O(N)/O(1)
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_left_height = -1
        max_right_height = -1
        total_water = 0
        while i < j:
            if (height[i] < height[j]):
                max_left_height = max(max_left_height, height[i])
                total_water = total_water + (max_left_height - height[i])
                i += 1
            else:
                max_right_height = max(max_right_height, height[j])
                total_water = total_water + (max_right_height - height[j])
                j -= 1

        return total_water


def trap(self, height: List[int]) -> int:
    left_elevation_map = []
    right_elevation_map = []

    # 3 Pass by building each left/right elevation separately.
    # i = 0
    # max_left_height = -1
    # while i<len(height):
    #     max_left_height = max(max_left_height,height[i])
    #     left_elevation_map.append(max_left_height)
    #     i+=1

    # i = 0
    # max_right_height = -1
    # reversed_height = height[::-1] #O(N)
    # while i<len(reversed_height):
    #     max_right_height = max(max_right_height,reversed_height[i])
    #     right_elevation_map.append(max_right_height)
    #     i+=1

    # 2 pass by building elevation map in one go.
    i = 0
    max_left_height = -1
    max_right_height = -1
    while i < len(height):
        max_left_height = max(max_left_height, height[i])
        left_elevation_map.append(max_left_height)

        max_right_height = max(max_right_height, height[len(height) - 1 - i])
        right_elevation_map.append(max_right_height)
        i += 1

    # print(f"Left: {left_elevation_map}")
    # print(f"Right: {right_elevation_map}")

    i = 0
    total_water = 0
    while i < len(height):
        min_of_both_sides = min(left_elevation_map[i], right_elevation_map[len(height) - i - 1])
        total_water = total_water + (min_of_both_sides - height[i])
        i += 1
    return total_water
