import pytest
from all_solutions import Solution

@pytest.fixture
def solution():
    return Solution()

class TestMergeStringsAlternately:
    def test_example_1(self, solution):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        output = solution.mergeAlternately(word1, word2)
        assert output == expected
    
    def test_example_2(self, solution):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        output = solution.mergeAlternately(word1, word2)
        assert output == expected

    def test_example_3(self, solution):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        output = solution.mergeAlternately(word1, word2)
        assert output == expected

class TestGCDOfStrings():
    def test_example_1(self, solution):
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_example_2(self, solution):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_example_3(self, solution):
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_example_4(self, solution):
        str1 = "ABCDEF"
        str2 = "ABC"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_example_5(self, solution):
        str1 = "AA"
        str2 = "A"
        expected = "A"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected
    
    def test_51(self, solution):
        str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
        str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
        expected = "NLZGM"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_56(self, solution):
        str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        expected = "TAUXX"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_75(self, solution):
        str1 = "ABABABAB"
        str2 = "ABAB"
        expected = "ABAB"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_79(self, solution):
        str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        expected = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_94(self, solution):
        str1 = "AAAAAAAAA"
        str2 = "AAACCC"
        expected = ""
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected

    def test_94_ALT(self, solution):
        str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        expected = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        output = solution.gcdOfStrings(str1, str2)
        assert output == expected


class TestKidsWithCandies():
    def test_example_1(self, solution):
        candies = [2,3,5,1,3]
        extraCandies = 3
        expected = [True, True, True, False, True] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert output == expected

    def test_example_2(self, solution):
        candies = [4,2,1,1,2]
        extraCandies = 1
        expected = [True, False, False, False, False] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert output == expected

    def test_example_3(self, solution):
        candies = [12,1,12]
        extraCandies = 10
        expected = [True, False, True] 
        output = solution.kidsWithCandies(candies, extraCandies)
        assert output == expected
                

class TestCanPlaceFlowers():
    def test_example_1(self, solution):
        flowerbed = [1,0,0,0,1]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_example_2(self, solution):
        flowerbed = [1,0,0,0,1]
        n = 2
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example(self, solution):
        flowerbed = [0,0,0]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example_2(self, solution):
        flowerbed = [0,0,0]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example_3(self, solution):
        flowerbed = [1,0,0,0,0,1]
        n = 1
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example_4(self, solution):
        flowerbed = [1,0,0,0,0,1]
        n = 2
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example_5(self, solution):
        flowerbed = [1,0,0,0,0,0,1]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_self_example_6(self, solution):
        flowerbed = [1,0,0,0,0,0,1]
        n = 3
        expected = False
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected

    def test_118(self, solution):
        flowerbed = [1,0,0,0,1,0,0]
        n = 2
        expected = True
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected
    
class TestReverseVowels():
    def test_example_1(self, solution):
        s = "hello"
        expected = "holle"
        output = solution.reverseVowels(s)
        assert output == expected

    def test_example_2(self, solution):
        s = "leetcode"
        expected = "leotcede"
        output = solution.reverseVowels(s)
        assert output == expected

    def test_290(self, solution):
        s = "aA"
        expected = "Aa"
        output = solution.reverseVowels(s)
        assert output == expected