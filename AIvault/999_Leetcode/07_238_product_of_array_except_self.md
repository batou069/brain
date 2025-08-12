# Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

> Input: nums = [1,2,3,4]
> Output: [24,12,8,6]

Example 2:

> Input: nums = [-1,1,0,-3,3]
> Output: [0,0,9,0,0]

Constraints:

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

**Follow up**: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# My Solution

## Pseudo Code

We need to indiced in the length of nums
For each i we need to go over all elements of nums and multiply them together
Except for when `j==i`
This is however O(n^2)

answer[0] = nums[1] * nums[2] * nums[3] * nums[4]
answer[1] = nums[0] * nums[2] * nums[3] * nums[4]
answer[2] = nums[0] * nums[1] * nums[3] * nums[4]
answer[3] = nums[0] * nums[1] * nums[2] * nums[4]
answer[4] = nums[0] * nums[1] * nums[2] * nums[3]

## My approach

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n):
            tmp = 1
            for j in range(n): 
                if i == j:
                    continue
                tmp *= nums[j]
            answer.append(tmp)
        return answer

```

## Better appoach

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result
```


