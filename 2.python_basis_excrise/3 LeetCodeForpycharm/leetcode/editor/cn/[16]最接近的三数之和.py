# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。 
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1751 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        result = 0

        #range前闭后开 len(nums) - 2 在循环里面到达len(nums)-这个位置
        for i in range(0 , len(nums)-2 , 1):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left<right:
                s =  nums[i] + nums[left] + nums[right]
                if s == target:
                    result = s
                    return result

                if s > target :
                    if diff > s - target:
                        result = s
                        diff = s - target
                    right -= 1

                if s<target :
                    if diff > target - s:
                        result = s
                        diff = target - s
                    left += 1
        return result










        
# leetcode submit region end(Prohibit modification and deletion)
