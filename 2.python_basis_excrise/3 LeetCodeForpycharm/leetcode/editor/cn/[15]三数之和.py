# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != 
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 7618 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0 , len(nums)-2 , 1):
            if ((nums[i] == nums[i-1]) and (i > 0)):
                continue
            index_left = i + 1
            index_right = len(nums) - 1

            while (index_left < index_right):
                s = nums[i]+nums[index_left] +nums[index_right]
                if s>0:
                    index_right-=1
                elif s<0:
                    index_left+=1
                else:
                    res.append([nums[i], nums[index_left] , nums[index_right]])

                    index_left +=1
                    while (index_left<index_right and nums[index_left]==nums[index_left-1]):
                        index_left+=1

                    index_right -= 1
                    while (index_left<index_right and nums[index_right] == nums[index_right+1]):
                        index_right-=1
        return res



# leetcode submit region end(Prohibit modification and deletion)
