class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        size=len(nums)
        while i<size and size>0:
            if nums[i-1]==nums[i]:
                nums.remove(nums[i-1])
                i-=1
                size-=1
            i+=1
        print(nums)