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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        output_dict = {}

        for current in strs:
            length = len(current)
            if length in output_dict:
                all_words = output_dict[length]
                # output_dict[length][0].append(current)
                flag = False
                for words in all_words:
                    if sorted(current)== sorted(words[0]):
                        words.append(current)
                        flag = True
                        break
                if not flag:
                    all_words.append([current])

            else:
                output_dict[length] = [[current]]
        output = []
        for key in output_dict:
            
            for words in output_dict[key]:
                output.append(words)
        return output
        

def main():
    solution = Solution()
    # nums = [1, 2, 3, 3]
    # print(solution.hasDuplicate(nums))
    # nums = [1, 2, 3, 4]
    # print(solution.hasDuplicate(nums))
    # s = "racecar"
    # t = "carrace"
    # print(solution.isAnagram(s, t))
    # s = "jar"
    # t = "jam"
    # print(solution.isAnagram(s, t))
    # s = "a"
    # t = "ab"
    # print(solution.isAnagram(s, t))
    strs = ["act","pots","tops","cat","stop","hat"]
    print(solution.groupAnagrams(strs))
    print([["hat"],["act", "cat"],["stop", "pots", "tops"]])
    strs = ["x"]
    print(solution.groupAnagrams(strs))

main()