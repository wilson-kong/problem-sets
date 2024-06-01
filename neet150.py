# https://neetcode.io/roadmap

from typing import List
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        
        return len(counter) != len(nums)
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = list(s)
        for char in t:
            if char in s_letters:
                s_letters.remove(char)

        return len(s_letters) == 0


def main():
    solution = Solution()
    # nums = [1, 2, 3, 3]
    # print(solution.hasDuplicate(nums))
    # nums = [1, 2, 3, 4]
    # print(solution.hasDuplicate(nums))
    s = "racecar"
    t = "carrace"
    print(solution.isAnagram(s, t))
    s = "jar"
    t = "jam"
    print(solution.isAnagram(s, t))
    s = "a"
    t = "ab"
    print(solution.isAnagram(s, t))

main()