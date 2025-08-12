# Problem
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

 

Example 1:

> Input: nums = [1,2,3,4,5]
> Output: true
> Explanation: Any triplet where i < j < k is valid.

Example 2:

> Input: nums = [5,4,3,2,1]
> Output: false
> Explanation: No triplet exists.

Example 3:

> Input: nums = [2,1,5,0,4,6]
> Output: true
> Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

**Constraints:**
- `1 <= nums.length <= 5 * 105`
- `-231 <= nums[i] <= 231 - 1`


**Follow up:** Could you implement a solution that runs in `O(n)` time complexity and `O(1)` space complexity?
# Solution



## Pseudocode
- check for length of nums:
    - if its smaller than 3 return false
    - if length is 3, check if conditions are met, else false
    - for length over 3 we start moving our sliding window
    - pointer 3 moves by one, check if pointer3 > pointer 2 > pointer 1
    - if not move pointer 2, but if pointer2>pointer1 but pointer3 not, we try to move pointer3 instead
- 
- Have one pointer at nums[0] and another at nums[-1]
- Additionaly have one pointer at nums[-2]
- Move the first pointer
## My Solution
```python
<NONE>
```
## Better Solution
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True  # n > second > first → found triplet
        
        return False
```