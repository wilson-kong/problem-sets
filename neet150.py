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
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        count = 0
        for i in range(nums_len - 1, 0, -1):
            for j in range(i):
                if nums[nums_len - i - 1] + nums[j + 1 + count] == target:
                    return[nums_len - i - 1, j + 1 + count]
            count += 1


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