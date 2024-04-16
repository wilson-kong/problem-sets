from collections import Counter
from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ 1768. Merge Strings Alternately """
        output = ""
        word2_len = len(word2)
        for index, char in enumerate(word1):
            output += char
            if index < word2_len:
                output += word2[index]

        index += 1
        if index <= word2_len:
                output += word2[index:]

        return output

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """ 1071. Greatest Common Divisor of Strings """
        if str1 == str2:
            return str1
        
        # After realising this, this problem was okay, 
        # but took a while to arrive at this.
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        
        return ""
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        output = []
        for kid in candies:
            if kid + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)
        return output
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        previous = 0
        total_empty = 1
        flowerbed.append(0)
        flowerbed_len = len(flowerbed)

        if 1 not in flowerbed:
            total_empty += flowerbed_len
            n = subtracting(n, total_empty)
            return n <= 0
        
        for index in range(flowerbed_len):
            previous = flowerbed[index]
            if previous:
                n = subtracting(n, total_empty)
                total_empty = 0
                continue
            total_empty += 1

        n = subtracting(n, total_empty)

        return n <= 0
    

def gcd(first: int, second: int) -> int:
    """ for gcd """
    result = min(first, second)
    while result > 0:
        if first % result == 0 and second % result == 0:
            return result
        result -= 1

def subtracting(n: int, total_empty: int) -> int:
    """ for canPlaceFlowers """
    if total_empty and total_empty % 2 == 0:
        n -= ((total_empty/2) - 1)
    elif total_empty and total_empty % 2 != 0:
        n -= ((total_empty//2))
    return n