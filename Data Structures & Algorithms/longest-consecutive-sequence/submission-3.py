class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        longest=0

        # convert list to set because "in" operation on list will take O(n) time and since i have to do this operation in a loop it will become O(n)**2, so convert to set and do the operation
        new_set = set()
        for each in nums:
            new_set.add(each)

        for each in new_set:
            c_each = each
            c_longest = 1
            
            if each in visited:
                # already counted, no need to count again
                continue
            else:
               visited.add(each)

            # check if next numbers are present
            while c_each + 1 in new_set:
                c_longest += 1
                visited.add(c_each + 1)
                c_each += 1
            longest = c_longest if c_longest > longest else longest

        return longest

        