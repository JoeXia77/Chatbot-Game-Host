import os
import json
import openai
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext



# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = ""

class Chatbot:
    def __init__(self):
        self.history = []
        self.model = "gpt-3.5-turbo"
        self.default_conversation_length = 5

    def generate_message(self, user_input, conversation_length):
        message = {"role": "user", "content": user_input}
        self.history.append(message)
        messages = self.history[-conversation_length:]
        return messages

    def get_response(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=0,
        )
        return response['choices'][0]['message']['content']

    def run(self):
        while True:
            user_input = input("You: ")
            if user_input == "quit":
                break
            messages = self.generate_message(user_input, self.default_conversation_length)
            response = self.get_response(messages)
            self.history.append({"role": "system", "content": response})
            print("system: " + response)


class PuzzleHolder(Chatbot):
    def __init__(self):
        super().__init__()
        self.hint_chance = 0.3

        self.story_file_name = 'story-1.json'
        dir_path = os.path.dirname(os.path.abspath(__file__))
        stories_path = os.path.join(dir_path, "stories")
        story_path = os.path.join(stories_path, self.story_file_name)
        with open(story_path, "r") as f:
            story = json.load(f)
        self.story = story

    def announce_game_start(self):
        print('Here is the story:')
        print(self.story['appearance'])
        print("\nQuestion: " + self.story['question'])
        print("\nType below to ask anything which could help you reach the truth")

    def prefix_game_rule(self, messages):
        rule = f"I want you to hold an Lateral-Thinking Puzzles game. You know the truth of the story, if user ask you any question about this story, if you are not very sure about the answer, please answer 'I don't know', if you could use yes or no to answer the question, do that. if you cannot reply only with yes or no, don't tell anything about the truth but tell the user I can not answer that. The truth of story is as follows: {self.story['truth']}, now the game starts."
        prefix = {"role": "user", "content": rule}
        messages.insert(0, prefix)
        return messages

    def run(self):
        self.announce_game_start()
        while True:
            user_input = input("You: ")
            if user_input == "quit":
                break
            messages = self.generate_message(user_input, self.default_conversation_length)
            messages = self.prefix_game_rule(messages)
            response = self.get_response(messages)
            self.history.append({"role": "system", "content": response})
            print("system: " + response)


class LateralThinkingPuzzlesUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.master.title("Lateral-Thinking Puzzles")
        self.master.geometry("800x600")

        # Create a ttk style object
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))

        self.story_frame = ttk.Frame(self.master)
        self.story_frame.pack(pady=20)

        self.story_label = ttk.Label(self.story_frame, text="Story:", font=("Helvetica", 12))
        self.story_label.pack(side=tk.LEFT, padx=5)

        self.story_text = tk.Text(self.story_frame, wrap=tk.WORD, height=8, width=60, font=("Helvetica", 12))
        self.story_text.pack(side=tk.LEFT, padx=5)
        self.story_text.insert(tk.END, self.game.story['appearance'])

        self.question_label = ttk.Label(self.master, text="Seeking Truth: " + self.game.story['question'], wraplength=500)
        self.question_label.pack(pady=20, anchor=tk.CENTER, expand=True)
        
        
        self.input_frame = ttk.Frame(self.master)
        self.input_frame.pack(pady=20)

        self.input_label = ttk.Label(self.input_frame, text="Any questions? Type it below and send it to me.", font=("Helvetica", 12))
        self.input_label.pack(side=tk.TOP, anchor=tk.W)

        self.input_entry = ttk.Entry(self.input_frame, width=60)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)
        

        self.chat_frame = ttk.Frame(self.master)
        self.chat_frame.pack(pady=10)

        self.chat_label = ttk.Label(self.chat_frame, text="Chat History:", font=("Helvetica", 12))
        self.chat_label.pack(pady=10, anchor=tk.CENTER, expand=True)

        self.chat_text = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, height=15, width=80, font=("Helvetica", 12))
        self.chat_text.pack(padx=10)
        self.chat_text.config(state=tk.DISABLED)



    def send_message(self):
        user_input = self.input_entry.get()
        if user_input == "quit":
            self.master.destroy()
            return

        self.append_chat("You: " + user_input)
        messages = self.game.generate_message(user_input, self.game.default_conversation_length)
        messages = self.game.prefix_game_rule(messages)
        response = self.game.get_response(messages)
        self.game.history.append({"role": "system", "content": response})
        self.append_chat("System: " + response)
        self.input_entry.delete(0, tk.END)

    def append_chat(self, message):
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, message + "\n")
        self.chat_text.config(state=tk.DISABLED)
        self.chat_text.yview(tk.END)




def main():
    root = tk.Tk()
    game = PuzzleHolder()
    LateralThinkingPuzzlesUI(root, game)
    root.mainloop()

main()


