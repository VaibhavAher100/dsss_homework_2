import unittest
from math_quiz import generate_random_number, generate_random_operator, create_problem_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if random operator generated is one of the specified operators
        for _ in range(100):
             operator = generate_random_operator()
             self.assertIn(operator, ['+', '-', '*'])

    def test_create_problem_answer(self):
            # Test if the problem and answer are correctly generated
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (4, 2, '+', '4 + 2', 6),
                (4, 2, '-', '4 - 2', 2),
                (4, 2, '*', '4 * 2', 8),
            ]

            # Loop through the test cases and check if the problem and answer are correct
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = create_problem_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem, f"Problem incorrect for input: {num1} {num2} {operator}")
                self.assertEqual(answer, expected_answer, f"Answer incorrect for input: {num1} {num2} {operator}")

if __name__ == "__main__":
    unittest.main()
