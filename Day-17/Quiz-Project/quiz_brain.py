class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        ans = input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False)?: ")
        print(ans)




