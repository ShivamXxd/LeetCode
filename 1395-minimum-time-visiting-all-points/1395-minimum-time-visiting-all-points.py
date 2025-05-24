class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points)-1):
            diff_y = abs(points[i+1][1] - points[i][1])
            diff_x = abs(points[i+1][0] - points[i][0])
            total_time += max(diff_x, diff_y)
        return total_time