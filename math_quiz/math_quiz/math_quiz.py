import random

# Generate a random integer between min_val and max_val.

def generate_random_number(min_val, max_val):
    """
    Random integer.
    """
    return random.randint(min_val, max_val)

# Returns a random mathematical operator: +, -, or *.

def generate_random_operator():
    return random.choice(['+', '-', '*'])


def create_problem_answer(num1, num2, operator):
    problem = f"{num1} {operator} {num2}"

    # Correcting the operation logic
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

# Starts the math quiz game, presenting the user with math problems and calculate the score.
def math_quiz():
    score = 0
    total_questions = 4 # adjusted to an integer value instead of a float

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

# Loop through the total number of questions
    for i in range(total_questions):
        num1 = generate_random_number(min_val= 1, max_val= 10) 
        num2 = generate_random_number(min_val= 1, max_val= 5) 
        operator = generate_random_operator()

        # Gernerate the problem and compute the correct answer
        problem, correct_answer = create_problem_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get user input and check if it is correct
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1 # increment the score for each correct answer
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print(f"\nGame over! Your score is: {score}/{total_questions}")

# Run the math quiz game.
if __name__ == "__main__":
    math_quiz()