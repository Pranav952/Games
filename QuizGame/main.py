from question_model import Question
from QuizGame.data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
q1 = QuizBrain(question_bank)
q1.next_question()
