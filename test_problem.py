import pytest
from all_solutions import Solution

@pytest.fixture
def solution():
    return Solution()

class TestMergeStringsAlternately:
    def test_example_1(self, solution: Solution):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        output = solution.mergeAlternately(word1, word2)
        assert expected == output
    
    def test_example_2(self, solution: Solution):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        output = solution.mergeAlternately(word1, word2)
        assert expected == output

    def test_example_3(self, solution: Solution):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        output = solution.mergeAlternately(word1, word2)
        assert expected == output

class TestGCDOfStrings():
    def test_example_1(self, solution: Solution):
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_example_2(self, solution: Solution):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_example_3(self, solution: Solution):
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_example_4(self, solution: Solution):
        str1 = "ABCDEF"
        str2 = "ABC"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_example_5(self, solution: Solution):
        str1 = "AA"
        str2 = "A"
        expected = "A"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output
    
    def test_51(self, solution: Solution):
        str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
        str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
        expected = "NLZGM"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_56(self, solution: Solution):
        str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        expected = "TAUXX"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_75(self, solution: Solution):
        str1 = "ABABABAB"
        str2 = "ABAB"
        expected = "ABAB"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_79(self, solution: Solution):
        str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        expected = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_94(self, solution: Solution):
        str1 = "AAAAAAAAA"
        str2 = "AAACCC"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output

    def test_94_ALT(self, solution: Solution):
        str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        expected = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        output = solution.gcdOfStrings(str1, str2)
        assert expected == output


class TestKidsWithCandies():
    def test_example_1(self, solution: Solution):
        candies = [2,3,5,1,3]
        extraCandies = 3
        expected = [True, True, True, False, True] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert expected == output

    def test_example_2(self, solution: Solution):
        candies = [4,2,1,1,2]
        extraCandies = 1
        expected = [True, False, False, False, False] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert expected == output

    def test_example_3(self, solution: Solution):
        candies = [12,1,12]
        extraCandies = 10
        expected = [True, False, True] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert expected == output
                

class TestCanPlaceFlowers():
    def test_example_1(self, solution: Solution):
        flowerbed = [1,0,0,0,1]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_example_2(self, solution: Solution):
        flowerbed = [1,0,0,0,1]
        n = 2
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example(self, solution: Solution):
        flowerbed = [0,0,0]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example_2(self, solution: Solution):
        flowerbed = [0,0,0]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example_3(self, solution: Solution):
        flowerbed = [1,0,0,0,0,1]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example_4(self, solution: Solution):
        flowerbed = [1,0,0,0,0,1]
        n = 2
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example_5(self, solution: Solution):
        flowerbed = [1,0,0,0,0,0,1]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_self_example_6(self, solution: Solution):
        flowerbed = [1,0,0,0,0,0,1]
        n = 3
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output

    def test_118(self, solution: Solution):
        flowerbed = [1,0,0,0,1,0,0]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert expected == output
    
class TestReverseVowels():
    def test_example_1(self, solution: Solution):
        s = "hello"
        expected = "holle"
        output = solution.reverseVowels(s)
        assert expected == output

    def test_example_2(self, solution: Solution):
        s = "leetcode"
        expected = "leotcede"
        output = solution.reverseVowels(s)
        assert expected == output

    def test_290(self, solution: Solution):
        s = "aA"
        expected = "Aa"
        output = solution.reverseVowels(s)
        assert expected == output

class TestReverseWords():
    def test_example_1(self, solution: Solution):
        s = "the sky is blue"
        expected = "blue is sky the"
        output = solution.reverseWords(s)
        assert expected == output

    def test_example_2(self, solution: Solution):
        s = "  hello world  "
        expected = "world hello"
        output = solution.reverseWords(s)
        assert expected == output

    def test_example_3(self, solution: Solution):
        s = "a good   example"
        expected = "example good a"
        output = solution.reverseWords(s)
        assert expected == output


class TestProductExceptSelf():
    def test_example_1(self, solution: Solution):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        output = solution.productExceptSelf(nums)
        assert expected == output

    def test_example_2(self, solution: Solution):
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        output = solution.productExceptSelf(nums)
        assert expected == output

    def test_18(self, solution: Solution):
        nums = [0,0]
        expected = [0,0]
        output = solution.productExceptSelf(nums)
        assert expected == output

    def test_17(self, solution: Solution):
        nums = [1,0]
        expected = [0,1]
        output = solution.productExceptSelf(nums)
        assert expected == output

    def test_13(self, solution: Solution):
        nums = [2,3,5,0]
        expected = [0,0,0,30]
        output = solution.productExceptSelf(nums)
        assert expected == output


class TestIncreasingTriplet():
    def test_example_1(self, solution: Solution):
        nums = [1,2,3,4,5]
        expected = True
        output = solution.increasingTriplet(nums)
        assert expected == output

    def test_example_2(self, solution: Solution):
        nums = [5,4,3,2,1]
        expected = False
        output = solution.increasingTriplet(nums)
        assert expected == output

    def test_example_3(self, solution: Solution):
        nums = [2,1,5,0,4,6]
        expected = True
        output = solution.increasingTriplet(nums)
        assert expected == output

    def test_67(self, solution: Solution):
        nums = [20,100,10,12,5,13]
        expected = True
        output = solution.increasingTriplet(nums)
        assert expected == output

    def test_75(self, solution: Solution):
        nums = [4,5,2147483647,1,2]
        expected = True
        output = solution.increasingTriplet(nums)
        assert expected == output


class TestStringCompression():
    def test_example_1(self, solution: Solution):
        chars = ["a","a","b","b","c","c","c"]
        expected = 6
        expected_chars = ["a","2","b","2","c","3"]
        output = solution.compress(chars)
        assert expected == output
        assert expected_chars == chars[:expected]

    def test_example_2(self, solution: Solution):
        chars = ["a"]
        expected = 1
        expected_chars = ["a"]
        output = solution.compress(chars)
        assert expected == output
        assert expected_chars == chars[:expected]

    def test_example_3(self, solution: Solution):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected = 4
        expected_chars = ["a","b","1","2"]
        output = solution.compress(chars)
        assert expected == output
        assert expected_chars == chars[:expected]

    def test_example_3(self, solution: Solution):
        chars = ["a","a","a","b","b","a","a"]
        expected = 6
        expected_chars = ["a","3","b","2","a","2"]
        output = solution.compress(chars)
        assert expected == output
        assert expected_chars == chars[:expected]


class TestMoveZeroes():
    def test_example_1(self, solution: Solution):
        nums = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        solution.moveZeroes(nums)
        assert expected == nums

    def test_example_2(self, solution: Solution):
        nums = [0]
        expected = [0]
        solution.moveZeroes(nums)
        assert expected == nums

    def test_28(self, solution: Solution):
        nums = [0, 0, 1]
        expected = [1, 0, 0]
        solution.moveZeroes(nums)
        assert expected == nums    

    
class TestIsSubsequence():
    def test_example_1(self, solution: Solution):
        s = "abc"
        t = "ahbgdc"
        expected = True
        output = solution.isSubsequence(s, t)
        assert expected == output

    def test_example_2(self, solution: Solution):
        s = "axc"
        t = "ahbgdc"
        expected = False
        output = solution.isSubsequence(s, t)
        assert expected == output

    def test_self_example_1(self, solution: Solution):
        s = "ahbgdc"
        t = "axc"
        expected = False
        output = solution.isSubsequence(s, t)
        assert expected == output

    def test_1(self, solution: Solution):
        s = ""
        t = "ahbgdc"
        expected = True
        output = solution.isSubsequence(s, t)
        assert expected == output