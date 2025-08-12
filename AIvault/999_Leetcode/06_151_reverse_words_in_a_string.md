# Problem

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**

> **Input:** s = "the sky is blue"
> **Output:** "blue is sky the"

**Example 2:**

> **Input:** s = "  hello world  "
> **Output:** "world hello"
> **Explanation:** Your reversed string should not contain leading or trailing spaces.

**Example 3:**

> **Input:** s = "a good   example"
> **Output:** "example good a"
> **Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.


# Solution

## Pseudo Code
1. strip string from spaces before and after text
2. split string into list
3. loop over split string list and append an element only if its lengths is > 0
4. reverse new list
5. join with space

## My Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        s_new = []
        for i in range(len(s)):
            if len(s[i]) > 0:
                s_new.append(s[i])
        s_new = s_new[::-1]
        return " ".join(s_new)
```

## Better Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l.reverse()
        return " ".join(l)
```
