class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # idea: find the mid element and contribution from both array
        # take min array so we can easily findout its contribution and then take rest from another array
        # once you know the contribution from this, check if partition is correct
        # how to check
        # left part should be less than right part thats it

        total_len = len(nums1) + len(nums2)
        mid_e = (total_len + 1) // 2

        # check which array is small so that we can start to find partition using it
        # why: because at max i have to consider whole array + rest from another
            # also no edge cases like index out of range
        
        # i have to swap and keep minimum array as num1 so in downstream all access
        # and mid operations happen on min array, only reference is not enough
        if len(nums2) < len(nums1):
            # swap so nums1 will be min
            nums1, nums2 = nums2, nums1

        i = 0
        j = len(nums1)

        while True:
            m1 = (i + j) // 2
            # since i found mid element (this is the contibution from small array)
            # and rest of the elements will be the contribution from other array
            m2 = mid_e - m1

            l1 = nums1[m1-1] if m1 > 0 else float("-inf")
            r1 = nums1[m1] if (m1) < len(nums1) else float("inf")

            l2 = nums2[m2-1] if m2 >0 else float("-inf")
            r2 = nums2[m2] if (m2) < len(nums2) else float("inf")

            if (l1 <= r2) and (l2 <= r1):
                # partition is correct and left part is less than right
                
                # check odd or even
                if total_len % 2 == 0:
                    # last element from 1st partition and 
                    # first eleemtn from second partition and return mean
                    t1 = max(l1, l2)
                    t2 = min(r1, r2)
                    return (t1 + t2) / 2
                else:
                    # odd, so only 1 mid element
                    # return the last max element
                    return max(l1, l2)

            elif (l1 > r2):
                # meaning i have more elements from 1st list, reduce
                j = m1 - 1
            else:
                # meaning l2 have more elements so i have to increase l1 elements
                i = m1 + 1
