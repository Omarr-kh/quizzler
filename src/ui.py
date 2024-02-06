import tkinter as tk

THEME_COLOR = "#375362"


class QuizUI():

    def __init__(self):
        # window settings
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = tk.Label(text="Score: 0",
                                    bg=THEME_COLOR, fg="white", font=(
                                        "Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white",
                                highlightbackground="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text", font=(
            "Arial", 25, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = tk.PhotoImage(file="../images/true.png")
        self.true_button = tk.Button(
            image=true_image, highlightthickness=2, highlightbackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="../images/false.png")
        self.false_button = tk.Button(
            image=false_image, highlightthickness=2, highlightbackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
