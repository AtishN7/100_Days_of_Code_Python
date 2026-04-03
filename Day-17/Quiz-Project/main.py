from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(a_text=q['text'], a_answer=q['answer']))

q = QuizBrain(question_bank)
q.next_question()