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