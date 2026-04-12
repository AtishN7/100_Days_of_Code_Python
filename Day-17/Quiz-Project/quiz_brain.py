class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question .text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)


    def check_answer(self, user_ans, correct_ans):
        if user_ans.upper() == correct_ans.upper():
            print("Correct answer!!")
            self.score += 1
        else:
            print("Wrong answer!!")
        print(f"The answer to question last asked is {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



