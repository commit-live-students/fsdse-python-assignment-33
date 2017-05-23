from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        result = solution(['abc', 'xyz', 'aba', '1221'])
        self.assertEqual(result, 2)