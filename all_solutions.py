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