from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RED = "#e7305b"
GREEN = "#9bdeac"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightthickness=0)
        check = PhotoImage(file="images/true.gif")
        cross = PhotoImage(file="images/false.gif")
        self.score_label = Label(
            text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.true_button = Button(text="Start",
                                  highlightthickness=0, image=check, command=self.check_if_true)
        self.false_button = Button(text="Reset",
                                   highlightthickness=0, image=cross, command=self.check_if_false)
        self.quiz_text = self.canvas.create_text(150, 125, width=200, text="Test", fill=THEME_COLOR,
                                                 font=("arial", 20, "italic"))

        # Layout
        self.score_label.grid(row=0, column=1)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question)
        else:
            self.canvas.itemconfig(
                self.quiz_text, text=f"You've reached the end of the quiz. {self.quiz.score} / {self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_true(self):
        is_correct = self.quiz.check_answer(True)
        self.update_canvas(is_correct)

    def check_if_false(self):
        is_correct = self.quiz.check_answer(False)
        self.update_canvas(is_correct)

    def update_canvas(self, answer: bool):
        if answer:
            self.canvas.config(bg=GREEN)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.next_question)
