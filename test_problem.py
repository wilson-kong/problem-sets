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