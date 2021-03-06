"""
https://leetcode-cn.com/problems/3sum/submissions/
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


注意时间复杂度！！！

"""
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums = sorted(nums)

        result = []
        computed_set = set()
        for j, n in enumerate(nums):
            # 防止重复计算,同时防止重复出现
            if n in computed_set:
                continue
            result_2 = self.twoSum(nums[j + 1:], -n)
            if len(result_2) > 0:
                for r_2 in result_2:
                    result.append((n,) + r_2)
            computed_set.add(n)
        return list(set(result))

    def twoSum(self, nums, n):
        i, j = 0, len(nums) - 1

        result = []

        while i < j:
            if nums[i] + nums[j] == n:
                result.append((nums[i], nums[j]))

                if nums[i] == nums[i + 1]:
                    i += 1
                elif nums[j] == nums[j - 1]:
                    j -= 1
                else:
                    i += 1
                    j -= 1
            elif nums[i] + nums[j] < n:
                i += 1
            else:
                j -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum(
        [-1, 0, 1, 2, -1, -4]))
