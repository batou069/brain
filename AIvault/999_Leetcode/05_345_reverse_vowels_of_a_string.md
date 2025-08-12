# Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

> **Input:** s = "IceCreAm"
> **Output:** "AceCreIm"
> **Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

> **Input:** s = "leetcode"
> **Output:** "leotcede"

**Constraints:**

- `1 <= s.length <= 3 * 105`
- `s` consist of **printable ASCII** characters.

# My Solution

## Pseodo Code

1. create an array with the vowels
2. create an two empty lists, one for indices, one for vowels
3. iterate over the whole string
4. for every character that is a vowel append it its index to the `indices_list` and the vowel to the `vowel_list`
5. flip the vowel_list list by slicing it `[ : : -1 ]`
6. iterate over `string` again and replace where `i == indices_list` and replace `string[i]` with `vowel_list[i]`

## My Solution

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        indices_list = []
        vowels_list = []
        vowels = ["a", "e", "i", "o", "u"]

        for i in range(len(s)):
            if s[i].lower() in vowels:
                indices_list.append(i)
                vowels_list.append(s[i])
            else:
                continue

        vowels_list = vowels_list[::-1]

        s = list(s)

        for i in range(len(vowels_list)):
            index_to_replace = indices_list[i]
            s[index_to_replace] = vowels_list[i]
        
        return "".join(s)
```


## Better Solution


```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels=set("AEIOUaeiou")
        i,j=0,len(s)-1
        while(i<j):
            if (s[i] in vowels) and (s[j] in vowels):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in vowels:j-=1
            elif s[j] in vowels:i+=1
            else:
                i+=1
                j-=1
        return "".join(s)    
```
