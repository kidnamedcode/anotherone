import tkinter as tk

questions = [
    ["1. What is the country with the capital city Brussels?", "belgium"],
    ["2. What is the capital of Bulgaria?", "sofia"],
    ["3. What is the capital of the U.S. state of New Mexico?", "santa fe"]
]

current_question = 0
score = 0

window = tk.Tk()
window.title("Untitled random question game")
window.geometry("600x300")

def submit_answer():
    global current_question, score

    answer = answer_entry.get().strip().lower()
    correct_answer = questions[current_question][1]

    if answer == correct_answer:
        score += 1
        result_label.config(text="Correct!")
    else:
        score -= 1
        result_label.config(text=f"Incorrect, correct answer is: {correct_answer}")

    score_label.config(text=f"Score: {score}")
    answer_entry.delete(0, tk.END)

    current_question += 1

    if current_question < len(questions):
        question_label.config(text=questions[current_question][0])
    else:
        question_label.config(text=f"Game over... Final score: {score}")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")

question_label = tk.Label(window, text=questions[0][0], font=("Comfortaa", 14))
question_label.pack(pady=20)

answer_entry = tk.Entry(window, width=30)
answer_entry.pack()

submit_button = tk.Button(window, text="Submit", command=submit_answer)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

score_label = tk.Label(window, text="Score: 0")
score_label.pack()

window.mainloop()
