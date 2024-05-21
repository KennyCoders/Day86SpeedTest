import tkinter
from tkinter import *
from tkinter import messagebox


# Should be .txt in different file, but no time.
word_bank = [
    "the", "and", "you", "for", "but", "not", "how", "can", "use", "see", "way", "why", "own", "man", "any", "day", "too", "may", "new", "get",
    "that", "have", "with", "all", "what", "your", "who", "out", "one", "now", "more", "says", "ask", "put", "end", "far", "big", "old", "yet", "try",
    "their", "about", "would", "which", "these", "other", "there", "which", "could", "people", "where", "every", "think", "never", "after", "first", "water", "earth", "sound", "plant"
]


#Keep track of typed word
global typed_word

correct_word_count = 0
timer_running = False

def start_timer():
    global timer_running
    timer_running = True
    count_down(15)  # Start a countdown of 15 seconds
    start_button.config(state=DISABLED)
    user_entry.config(state="normal")
    user_entry.focus_set()

def count_down(seconds):
    global timer_running
    if seconds >= 0:
        timer_label.config(text="Time Left: " + str(seconds))
        window.after(1000, count_down, seconds - 1)
    else:
        timer_label.config(text="Time's Up!")
        timer_running = False
        calculate_wpm()

def clear_entry(event):
    global typed_word
    if not timer_running:
        return
    typed_word = user_entry.get().strip()
    print("Word captured:", typed_word) # For logging
    user_entry.delete(0, END)
    compare_word()
    word_bank.pop(0) #Remove word from list

def compare_word():
    global typed_word, correct_word_count
    if typed_word == word_bank[0]:
        print("yes!")
        correct_word_count += 1
        highlight_correct_word()

def highlight_correct_word():
    start_index = text_box.search(word_bank[0], "1.0", END)
    end_index = f"{start_index.split('.')[0]}.{int(start_index.split('.')[1]) + len(word_bank[0])}"
    text_box.tag_configure("green", foreground="green")
    text_box.tag_add("green", start_index, end_index)

def calculate_wpm():
    global correct_word_count
    wpm = (correct_word_count / 15) * 60  # Calculate WPM based on 15 seconds
    messagebox.showinfo("WPM", f"Words per minute: {wpm:.2f}")



# GUI Setup
window = Tk()
window.title("Speed Type Test")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=350, width=450)
canvas.grid(row=0, column=1)

# Text Entry For User
user_entry = Entry(width=40, font=("Helvetica", 14), state="disabled")
user_entry.grid(row=1, column=1)
user_entry.bind("<space>", clear_entry)

word_row = " ".join(word_bank)

# Text Box for Words
text_box = Text(width=40, height=15, font=("Helvetica", 14), wrap=WORD)
text_box.grid(row=0, column=1)
text_box.insert(END, word_row)

# Timer Label
timer_label = Label(text="Click Start to Begin")
timer_label.grid(row=1, column=2)

# Start Button (centered underneath the text box)
start_button = Button(text="Start", width=13, command=start_timer)
start_button.grid(row=2, column=1, pady=(10, 0), sticky='n')

window.mainloop()
