# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [4,2,3,4]
# 输出: 4 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  
# 
#  Related Topics 贪心 数组 双指针 二分查找 排序 👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        n = len(nums)

        for i in range(0 , n , 1):

            left = i+1
            right = n-1
            while left<right:
                s = nums[left] + nums[right]
                if s > nums[i]:
                    res = res + right - left
                    left += 1
                else :
                    right -= 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
