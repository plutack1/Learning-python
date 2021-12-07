class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q{self.question_number}: {question.text} ("f""
                               f"true or false)")
        self.check_answer(current_answer, question.answer)

    def check_answer(self, current_answer, correct_answer):
        if current_answer.lower() == correct_answer.lower():
            print(f"You got it right")
            self.score += 1
        else:
            print(f"you got it wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"yor current score is {self.score}/{self.question_number}")
