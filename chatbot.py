import tkinter as tk
from datetime import datetime, date

def chatbot_response(user_input):
    user_input = user_input.strip().lower()
    
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    elif user_input in ["how are you?", "how are you doing?"]:
        return "I'm just a program, but I'm here to help you!"
    elif user_input in ["what's your name?", "who are you?"]:
        return "I'm a simple chatbot created to respond to your queries."
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I'm not able to check the weather right now, but you can use a weather app or website for that."
    elif "time" in user_input:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in user_input:
        today = date.today()
        return f"Today's date is {today}."
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "advice" in user_input:
        return "Always believe in yourself and never give up!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def send_message(event=None):
    user_input = user_entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_log.insert(tk.END, f"Chatbot: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    user_entry.delete(0, tk.END)
    if response == "Goodbye! Have a great day!":
        root.quit()

# Set up the GUI
root = tk.Tk()
root.title("Chatbot")

chat_log = tk.Text(root, bd=1, bg="white", font=("Arial", 12), state=tk.DISABLED)
chat_log.grid(row=0, column=0, columnspan=2)

scrollbar = tk.Scrollbar(root, command=chat_log.yview)
chat_log['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=0, column=2, sticky='ns')

user_entry = tk.Entry(root, bd=1, bg="white", font=("Arial", 12))
user_entry.grid(row=1, column=0)
user_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message, bd=1, bg="lightblue", font=("Arial", 12))
send_button.grid(row=1, column=1)

root.mainloop()
