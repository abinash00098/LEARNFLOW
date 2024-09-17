import tkinter as tk
from tkinter import messagebox
import random
from Questions import questions

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizMaster")
        self.score = 0
        self.num_questions = 3
        self.current_question = None
        
        self.difficulty = tk.StringVar()
        
        self.setup_start_screen()
    
    def setup_start_screen(self):
        tk.Label(self.root, text="Welcome to QuizMaster!").pack()
        
        tk.Label(self.root, text="Choose difficulty:").pack()
        tk.Radiobutton(self.root, text="Easy", variable=self.difficulty, value="easy").pack()
        tk.Radiobutton(self.root, text="Medium", variable=self.difficulty, value="medium").pack()
        tk.Radiobutton(self.root, text="Hard", variable=self.difficulty, value="hard").pack()
        
        tk.Button(self.root, text="Start", command=self.start_quiz).pack()
    
    def start_quiz(self):
        self.difficulty_level = self.difficulty.get()
        if self.difficulty_level not in questions:
            messagebox.showerror("Error", "Invalid difficulty")
            return
        
        self.question_count = 0
        self.ask_question()
    
    def ask_question(self):
        if self.question_count >= self.num_questions:
            self.show_score()
            return
        
        question = self.get_question(self.difficulty_level)
        self.current_question = question
        
        self.clear_frame()
        
        tk.Label(self.root, text=question["question"]).pack()
        self.options = tk.StringVar()
        for option in question["options"]:
            tk.Radiobutton(self.root, text=option, variable=self.options, value=option).pack()
        
        tk.Button(self.root, text="Submit", command=self.check_answer).pack()
    
    def get_question(self, difficulty):
        question_set = questions[difficulty]
        return random.choice(question_set)
    
    def check_answer(self):
        answer = self.options.get()
        if answer == self.current_question["answer"]:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer was: {self.current_question['answer']}")
        
        self.question_count += 1
        self.ask_question()
    
    def show_score(self):
        self.clear_frame()
        tk.Label(self.root, text=f"Game over! Your score: {self.score}/{self.num_questions}").pack()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()