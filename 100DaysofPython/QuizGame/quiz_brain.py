class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.player_score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {q.text} (True / False)")
        self.check_answer(user_answer, q.answer)

    def still_has_questions(self):
        """Returns a boolean"""
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.player_score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(
            f"Your current score is: {self.player_score}/{self.question_number}")
        print("\n")
