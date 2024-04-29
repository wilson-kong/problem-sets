from collections import Counter
import math
from typing import List, Optional
GUESS = 2

class ListNode:
    """ for 206. Reverse Linked List """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    """ for 104. Maximum Depth of Binary Tree """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        """ 443. String Compression """
        output = []
        current_char = chars[0]
        count = 1

        for index in range(1, len(chars)):
            char = chars[index]
            if char != current_char:
                output.append((current_char,str(count)))
                current_char = char
                count = 1
            else:
                count += 1
        output.append((current_char,str(count)))
        
        index = 0
        for char, count in output:
            if count == "1":
                chars[index] = char
                index += 1
            else:
                chars[index] = char
                index += 1
                for number in count:
                    chars[index] = number
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
    
    def largestAltitude(self, gain: List[int]) -> int:
        """ 1732. Find the Highest Altitude """
        altitude = 0
        highest = altitude
        for step in gain:
            altitude += step
            if altitude > highest:
                highest = altitude

        return highest

    def pivotIndex(self, nums: List[int]) -> int:
        """ 724. Find Pivot Index """
        right_total = sum(nums)
        left_total = 0
        for index, num in enumerate(nums):
            right_total -= num
            if right_total == left_total:
                return index
            left_total +=  num
        return -1
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """ 2215. Find the Difference of Two Arrays """
        answer = [[],[]]
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num not in nums2:
                answer[0].append(num)

        for num in nums2:
            if num not in nums1:
                answer[1].append(num)
        
        return answer
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """ 1207. Unique Number of Occurrences """
        # arr = Counter(arr)
        # all_occurences = Counter(arr.values())
        # for occurence in all_occurences.values():
        #     if occurence != 1:
        #         return False
        
        # return True

        # Faster by using variables
        count_arr = Counter(arr).values()
        return len(set(count_arr)) == len(count_arr)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 206. Reverse Linked List """
        reverse_node = None
        node = head

        while node is not None:
            next_node = node.next

            node.next = reverse_node.val
            reverse_node = node
            node = next_node

        return reverse_node.head
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ 104. Maximum Depth of Binary Tree """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """ 872. Leaf-Similar Trees """
        return dfs_leaves(root1) == dfs_leaves(root2)
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ 700. Search in a Binary Search Tree """
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
            
        return self.searchBST(root.right, val)  
    
    def guessNumber(self, n: int) -> int:
        """ 374. Guess Number Higher or Lower """
        if n == 1:
            return 1

        start = 1
        end = n
        
        while start <= end:
            guessing = (end + start) // 2    
            output = guess(guessing)
            if output == 0:
                return guessing
            elif output == -1:
                end = guessing - 1
            else:
                start = guessing + 1
        
        return guessing
    
    def tribonacci(self, n: int) -> int:
        """ 1137. N-th Tribonacci Number """
        if n < 2:
            return n
        
        current = [0, 1, 1]
        
        for _ in range(3, n + 1):
            new = sum(current)
            current[0] = current[1]
            current[1] = current[2]
            current[2] = new

        return current[2]

        # recursive
        # if n == 0:
        #     return 0
        
        # if n == 1 or n == 2:
        #     return 1
        
        # return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """ 746. Min Cost Climbing Stairs """
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return cost[-1]

def guess(num: int):
    if num > GUESS:
        return -1
    elif num < GUESS:
        return 1
    else:
        return 0

class RecentCounter:
    def __init__(self):
        self._queue = []
        self._front = 0
        self._rear = 0

    def ping(self, t: int) -> int:
        self._queue.append(t)
        # count = 0
        self._rear += 1
        start_time = t - 3000
        while self._queue[self._front] < start_time:
            self._front += 1
        
        return self._rear - self._front 
    
        # Brute force
        for i in range(len(self._queue) - 1, -1, -1):
            print(i)
            print(self._queue[i])
            print(t)

            if self._queue[i] >= start_time:
                count += 1

        return count


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
    

def dfs_leaves(root):
    """ for 872. Leaf-Similar Trees """
    if root is None:
        return []
    leaves = dfs_leaves(root.left) + dfs_leaves(root.right)
    return leaves or [root.val]

def main():
    s = Solution()
    s.compress(["a","a","b","b","c","c","c"])
    s.compress(["a"])
    s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

main()