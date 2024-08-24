import random

# Dictionary of questions and answers
questions_and_answers = {
    "What keyword is used to define a function in Python?": "def",
    "What data type is 'True' or 'False' in Python?": "bool",
    "Which symbol is used to comment a single line in Python?": "#",
    "What keyword is used to start a loop in Python?": "for",
    "What method is used to add an element to a list in Python?": "append",
    "What keyword is used to define a conditional statement in Python?": "if",
    "What is the output of `2 + 2` in Python?": "4",
    "What keyword is used to exit a loop in Python?": "break",
    "Which function is used to display output in Python?": "print",
    "What is the file extension for a Python script?": ".py",
    # Add more questions as needed
}

def run_quiz(questions_and_answers, num_questions=5):
    # Shuffle the questions
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    score = 0

    for i in range(min(num_questions, len(questions))):
        question = questions[i]
        answer = questions_and_answers[question]
        print(f"Question {i + 1}: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was '{answer}'.\n")

    print(f"Quiz complete! Your final score is {score}/{num_questions}.")

if __name__ == "__main__":
    num_questions = int(input("How many questions would you like in your quiz? "))
    run_quiz(questions_and_answers, num_questions)
