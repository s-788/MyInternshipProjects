import random

def ask_question(question, options, correct_answer):
    
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Your answer (enter the corresponding number): ")

    # Validate user input
    try:
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(options):
            user_answer_index = user_answer - 1
            if options[user_answer_index] == correct_answer:
                print("Correct!\n")
                return 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}\n")
                return 0
        else:
            print("Invalid input. Please enter a valid number.\n")
            return 0
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return 0

def quiz():
    
    print("Welcome to the Python Quiz!\n")

    
    questions = [
        "What is the capital of France?",
        "Which programming language is known for its readability and simplicity?",
        "What is the largest planet in our solar system?",
        "Which of the following are called 'Key Industrial animals'?",
        "Which of the following Himalayan regions is called Shivalik's?",
        
    ]
    options = [
        ["Paris", "Berlin", "London", "Rome"],
        ["Java", "Python", "C++", "JavaScript"],
        ["Earth", "Jupiter", "Mars", "Venus"],
        ["Producers", "Tertiary consumers", "Primary consumers", "None of these"],
        ["Upper Himalayas", "Lower Himalayas", "Outer Himalayas", "Inner Himalayas"],

    ]
    correct_answers = ["Paris", "Python", "Jupiter", "Primary consumers", "Outer Himalayas"]

    
    question_order = list(range(len(questions)))
    random.shuffle(question_order)

    
    score = 0

    
    for i in question_order:
        score += ask_question(questions[i], options[i], correct_answers[i])

    
    print(f"Your final score is: {score}/{len(questions)}")


quiz()
