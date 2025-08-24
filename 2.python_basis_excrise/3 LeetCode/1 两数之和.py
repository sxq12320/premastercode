import numpy as np
from typing import List

class Solution:
    #暴力枚举
    def twosum_violence(self, nums: List[int], target: int) -> List[int]:
        for i in range(0 , len(nums)):
            for j in range(i+1 , len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i , j]
        return[]

    def twosum_hashtab(self, nums: List[int], target: int) -> List[int]:
        #哈希表
        map = {}
        for index , value in enumerate(nums):
            map[value] = index
        for j in range(0 , len(nums) , 1):
            if ((target - nums[j]) in map) and (map[target-nums[j]] != j) :
                return [j , map[target-nums[j]]]

nums = [2,7,11,15]
target = 9

a = Solution.twosum_violence(Solution , nums , target)
b = Solution.twosum_hashtab(Solution , nums , target)

print(a)
print(b)


    

    
