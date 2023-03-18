import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrian


Question_bank = []
for question in question_data:
    text = question['question']
    answer = question['answer']
    new_q = Question(text, answer)
    Question_bank.append(new_q)

quiz= QuizBrian(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you've completed the Quiz , congrats")
print(f"your final score was : {quiz.score}/{quiz.question_number}")