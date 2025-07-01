import csv
import os

CSV_FILE_NAME = 'questions.csv'
csv_file_path = os.path.join(os.path.dirname(__file__), CSV_FILE_NAME)

def load_questions_from_csv(file_path):
    questions = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = {
                'question_text': row['Question'],
                'answers': [row['Answer 1'], row['Answer 2'], row['Answer 3'], row['Answer 4']],
                'correct_answer_index': int(row['Correct Answer']) - 1
            }
            questions.append(question)
    return questions

def ask_question(question, question_number):
    print(f"\nQuestion {question_number + 1}: {question['question_text']}")
    for i, answer in enumerate(question['answers']):
        print(f"{i + 1}. {answer}")
    
    attempts = 0
    while attempts < 3:
        user_input = input("Your answer (1-4): ").strip()
        if user_input in ['1', '2', '3', '4']:
            return int(user_input) - 1
        else:
            attempts += 1
            print(f"Invalid input. Please enter a number between 1 and 4. Attempts left: {3 - attempts}")
    
    print("Too many invalid attempts. Skipping question.")
    return None

def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        user_answer = ask_question(question, i)
        correct_answer = question['correct_answer_index']
        
        if user_answer is None:
            print(f"The correct answer was: {question['answers'][correct_answer]}")
        elif user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['answers'][correct_answer]}")
        
        print(f"Current score: {score}/{i + 1}")
    
    print("\nQuiz complete!")
    final_score = round(score / len(questions), 2)
    print(f"Final score: {score}/{len(questions)} ({final_score})")

def main():
    questions = load_questions_from_csv(csv_file_path)
    while True:
        run_quiz(questions)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
