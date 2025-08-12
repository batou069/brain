# Problem

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


**Example 1**:

> Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
> Output: [3,3,5,5,6,7]
> 
> Explanation: 
> Window position                Max
> ---------------               -----
> [1  3  -1] -3  5  3  6  7       3
>  1 [3  -1  -3] 5  3  6  7       3
>  1  3 [-1  -3  5] 3  6  7       5
>  1  3  -1 [-3  5  3] 6  7       5
>  1  3  -1  -3 [5  3  6] 7       6
>  1  3  -1  -3  5 [3  6  7]      7

**Example 2**:

> Input: nums = [1], k = 1
> Output: [1]

 

Constraints:
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- 1 <= k <= nums.length


# Solution

## Pseudocode

- Check for length of nums
- Create empty array of length k
- Initialize a loop from i=0 to i=n-k
- [0,1,2,3,4,5,6,7,8,9] n=10, if k=3 we start at i=0,1,2  and end at i=7,8,9
- At every step we can copy the sliding window to the tmp array, find out the max, and add the max to an answer array


## My solution

## Better solution
