class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0]*len(height), [0]*len(height)

        left_max[0]=height[0]
        for i in range(1, len(height)):
            left_max[i]=(max(left_max[i-1], height[i]))
        
        right_max[len(height)-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        total_s = 0
        for i in range(1, len(height)-1):
            # skipping first as it will not store water
            min_bound = min(left_max[i], right_max[i])
            if (min_bound - height[i]) > 0:
                total_s +=  (min_bound - height[i])
        
        return total_s

        