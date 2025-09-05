class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x = len(nums) // 2

        startList = nums[:x]
        endList = nums[x:]

        #print(startList)
        #print(endList)

        nums.clear()
        n = 0

        while len(nums) != x*2:
            nums.append(startList[n])
            nums.append(endList[n])
            
            if len(nums) == x*2:
                break
                
            #print(nums)
            #print(n)
            n += 1

        #print(nums)

        return nums