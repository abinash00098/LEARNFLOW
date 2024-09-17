import random
from Questions import questions

def get_question(difficulty):
    question_set = questions[difficulty]
    return random.choice(question_set)

def ask_question(question):
    print(question["question"])
    for idx, option in enumerate(question["options"], 1):
        print(f"{idx}. {option}")
    user_answer = input("Your answer (number): ")
    return question["options"][int(user_answer) - 1] == question["answer"]

def quiz_game():
    print("Welcome to QuizMaster!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    if difficulty not in questions:
        print("Invalid difficulty. Exiting game.")
        return
    
    score = 0
    num_questions = 3  # Number of questions to ask
    for _ in range(num_questions):
        question = get_question(difficulty)
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {question['answer']}\n")
    
    print(f"Game over! Your score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz_game()