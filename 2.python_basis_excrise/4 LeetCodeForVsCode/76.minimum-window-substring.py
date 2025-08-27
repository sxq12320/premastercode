#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 
        ansleft = -1
        ansright = len(s)

        cont_s = Counter()
        cont_t = Counter(t)

        for right,val in enumerate(s):
            cont_s[val] += 1
            while cont_s>= cont_t:
                if right - left < ansright - ansleft:
                    ansleft , ansright = left , right
                    cont_s[s[left]] -= 1
                    left +=1
            return "" if ansleft<0 else s[ansleft,ansright+1]
        
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

