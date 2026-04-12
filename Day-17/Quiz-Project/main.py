from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(a_text=q['question'], a_answer=q['correct_answer']))

quiz = QuizBrain(question_bank)

# print(len(question_bank))

while quiz.still_has_questions():
    quiz.next_question()


print(f"Congrats!! You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")