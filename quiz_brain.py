
class QuizBrian:

    def __init__(self, Question_bank):

        self.question_list = Question_bank
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_q.text} (True/false) :")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_ans, current_ans):
        if user_ans.lower() == current_ans.lower():
            print("You got it right ")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {current_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")

