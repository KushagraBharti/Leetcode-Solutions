class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        i = 0
        j = 1

        while j < len(nums):
            #print(f"i: {i}, j: {j}")
            #print(f"BEFORE: {nums}")
            if nums[i] == nums[j]:
                nums.pop(j)
                #print(f"AFTER: {nums} \n")
            else:
                i += 1
                j += 1
                #print("\n")

        k = len(nums)
        
        return k