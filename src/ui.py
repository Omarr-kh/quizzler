import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#4d4d00"


class QuizUI():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        # window settings
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        # Score label
        self.score_label = tk.Label(text="Score: 0",
                                    bg=THEME_COLOR, fg="white", font=(
                                        "Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tk.Canvas(width=400, height=250, bg="white",
                                highlightbackground="white")
        self.question_text = self.canvas.create_text(200, 125, width=340, font=(
            "Arial", 18, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = tk.PhotoImage(file="../images/true.png")
        self.true_button = tk.Button(
            image=true_image, highlightthickness=2, highlightbackground=THEME_COLOR, command=lambda: self.check_answer("true"))
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="../images/false.png")
        self.false_button = tk.Button(
            image=false_image, highlightthickness=2, highlightbackground=THEME_COLOR, command=lambda: self.check_answer("false"))
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer):
        self.switch(self.quiz_brain.check_answer(answer))

    def switch(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_question)
