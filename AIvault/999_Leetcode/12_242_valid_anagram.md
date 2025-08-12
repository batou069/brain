# Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Example 1:**

> **Input:** s = "anagram", t = "nagaram"
> **Output:** true

**Example 2:**

> **Input:** s = "rat", t = "car"
> **Output:** false

**Constraints:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# Solution

## Pseudocode

for both string, go character by character, and fill a dictionary 
first try to get the character from dict
if there is no, update it with {char: 1}
else get the value from the dict and update it to +1
dpo so with both strings, then compare the dicts
## My Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = {}
        t_string = {}
        for i in s:
            o = s_string.get(i)
            if o is None:
                s_string.update({i: 1})
            else:
                s_string.update({i: o+1})
        for i in t:
            o = t_string.get(i)
            if o is None:
                t_string.update({i: 1})
            else:
                t_string.update({i: o+1})
        return t_string == s_string
```
## Better Solution
```python
from collections import Counter

return Counter(s) == Counter(t)
```
