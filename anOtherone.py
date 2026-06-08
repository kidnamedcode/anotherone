import tkinter as tk
window = tk.Tk()

window.title("We the best")
window.geometry("800x800")

## Where the function goes:
## 'def submit_answer'


question_label = tk.Label(
    window,
    text = "Hackclub please approve my stuff im new to this"
)
question_label.pack()
question_label.pack(pady=100)

answer_entry = tk.Entry(window)
answer = answer_entry.get()

command = submit_answer

submit_button = tk.Button(
    window, 
    text="Submit",
    command= submit_answer
)

window.mainloop()       