class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if val not in nums:
            return len(nums)

        while (val in nums) == True:
            nums.remove(val)