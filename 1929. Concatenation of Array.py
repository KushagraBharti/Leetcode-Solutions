class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        for x in range(0, n):
            nums.append(nums[x])
            #print(nums)
        
        return nums