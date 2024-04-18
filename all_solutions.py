from collections import Counter
import math
from typing import List

class Solution:
    ##### Array / String #####
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
        """ 1431. Kids With the Greatest Number of Candies """
        greatest = max(candies)
        output = []
        for kid in candies:
            if kid + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)
        return output
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """ 605. Can Place Flowers """
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
    
    def reverseVowels(self, s: str) -> str:
        """ 345. Reverse Vowels of a String 
            time complexity can be improved 
        """
        storing = []
        storing_index = {}
        alpha = 'aeiouAEIOU'

        for index, char in enumerate(s):
            if char in alpha:
                storing.append(index)
                storing_index[index] = char

        number_of_vowels = len(storing)
        s = list(s)
        for _ in range(number_of_vowels//2):
            first = storing.pop(0)
            last = storing.pop(-1)
            s[first], s[last] = s[last], s[first]
        
        return "".join(s)

    def reverseWords(self, s: str) -> str:
        """ 151. Reverse Words in a String 
            Solutiuon uses a linked list, just to see if I can.
            The solution that uses a regular list is commented out.
        """
        output = []
        output = LinkedList()
        start_index = None
        s = ' ' + s + ' '
        for index, char in enumerate(s):
            if char != ' ':
                if start_index is None:
                    start_index = index
                    print("start_index", start_index)
            else:
                if start_index is not None:
                    # output.insert(0, s[start_index:index])
                    output.insert_at_start(s[start_index:index])
                    start_index = None

        return output.all_data()
        # return " ".join(output)
        # Alt solution 
        # return ' '.join(reversed(s.split()))


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 238. Product of Array Except Self  """
        output = []
        pre = 1
        for i in range(len(nums) - 1):
            num = nums[i]
            output.append(pre * num)
            pre *= num
        output.append(1)
        
        post = 1
        
        for i in range(len(nums) - 1, 0, -1):
            output[i] = output[i - 1] * post
            post = post * nums[i] 
        
        output[0] = 1 * post
        
        return output

        # total = 1
        # zero = False
        # all_zeros = None
        # for num in nums:
        #     if num != 0:
        #         total = total * num
        #         all_zeros = False
        #     else:
        #         zero = True
        #         if all_zeros is None or all_zeros == True:
        #             all_zeros = True
        # if all_zeros:
        #     return nums
        
        # output = []
        # if not zero:
        #     for num in nums:
        #         output.append(total//num)
        #     return output 
        
        # total = 1
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         total = math.prod(nums[:index]) * math.prod(nums[index + 1:])
        #         output.append(total)
        #         total = 1
        #     else:
        #         output.append(0)
        # return output

    def increasingTriplet(self, nums: List[int]) -> bool:
        """ 334. Increasing Triplet Subsequence """
        first = max(nums)
        second = first
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
    
        return False
    
    def compress(self, chars: List[str]) -> int:
        """ 443. String Compression443. String Compression """
        collected = Counter(chars)
        index = 0
        for key in collected:
            if collected[key] == 1:
                chars[index] = key
                index += 1
            else:
                chars[index] = key
                index += 1
                for char in str(collected[key]):
                    chars[index] = char
                    index += 1
        return index

    ##### Two Pointers #####
    def moveZeroes(self, nums: List[int]) -> None:
        """ 283. Move Zeroes """
        index = 0
        nums_length = len(nums)
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < nums_length:
            nums[index] = 0
            index += 1

        # Alt solution
        # for index in range(len(nums) - 1, -1, -1):
        #     print(nums)
        #     print(index)
        #     if nums[index] == 0:
        #         nums.pop(index)
        #         nums.append(0)

    def isSubsequence(self, s: str, t: str) -> bool:
        """ 392. Is Subsequence """
        if s == "":
            return True
        if len(s) > len(t):
            return False
        
        index = 0
        for char in t:
            if char == s[index]:
                if index == len(s) - 1:
                    return True
                index += 1
        return False
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """ 643. Maximum Average Subarray I
            Felt like a two pointers question. 
        """
        if len(nums) == k:
            return sum(nums)/k
        
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum
        left = 0
        right = k
        while right < len(nums):
            current_sum -= nums[left]
            current_sum += nums[right]
            left += 1
            right += 1
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum/k



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


class LinkedListNode:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data: str):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def all_data(self):
        current_node = self.head
        output = ""
        while current_node:
            output += current_node.data + " "
            current_node = current_node.next
        
        return output[:-1]