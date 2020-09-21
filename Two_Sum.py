# The Task: https://leetcode.com/problems/two-sum/

# The solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         create dictionary where the key is the number and value the index in array
        num_sum = dict()
        answer = []
#     go through the list adding nums to the dict
        for i in range(0, len(nums)):
            new_target = target - nums[i]
            if new_target in num_sum:
                answer.append(num_sum[new_target])
                answer.append(i)
                return answer
            else:
                num_sum[nums[i]] = i