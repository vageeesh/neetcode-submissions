class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # my idea
        # keep a stack, check if the top element is less than current one, if yes, keep on removing untill you find highest than this or empty
        # after you slide, you also have to remove the left most element you slided
        # since i will be remvoing element from front and back then dequeue O(1) is the right DS
        from collections import deque
        dq = deque([])

        r = 0
        l = 0
        res = []
        while r < k:
            while dq and dq[-1] < nums[r]:
                dq.pop()
            dq.append(nums[r])
            r += 1

        # first element will be the highest, so keep
        res.append(dq[0])

        while r < len(nums):
            # since moving left, if first element is the one which is in left most,
            # then remove it from queue and then move left
            if nums[l] == dq[0]:
                dq.popleft()
            l += 1

            while dq and dq[-1] < nums[r]:
                dq.pop()

            # append right
            dq.append(nums[r])
            # move right
            r += 1

            res.append(dq[0])

        return res
            



        
        