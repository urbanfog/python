from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()
print("The quiz is complete.")
print(f"Your score was: {brain.player_score}/{len(brain.question_list)}")
