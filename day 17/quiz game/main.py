from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question_pair in question_data:
    question = (question_pair["text"])
    answer = (question_pair["answer"])
    new_question = Question(text=question, answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"you've completed the quiz\nYour final score was: {quiz.score}/"
      f"{quiz.question_number}")

