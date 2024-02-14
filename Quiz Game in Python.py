questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the red planet ?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest animal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]

score = 0

def display_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data['options'], start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number of your answer: ")

    if question_data["options"][int(user_answer) - 1] == question_data["correct_answer"]:
        return True
    else:
        return False
        
for question in questions:
    if display_question(question):
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['correct_answer']}\n")

print(f"Your final score is: {score}/{len(question)}")