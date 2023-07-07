import tkinter as tk
import time

class TypingTest:
    def __init__(self):
        self.prompt_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0

        self.root = tk.Tk()
        self.root.title("Typing Test")
        self.root.geometry("400x200")

        self.prompt_label = tk.Label(self.root, text="Type the following text as fast as you can:")
        self.prompt_label.pack()

        self.text_label = tk.Label(self.root, text=self.prompt_text, wraplength=380)
        self.text_label.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_typing_test)
        self.start_button.pack()

        self.stats_label = tk.Label(self.root, text="")
        self.stats_label.pack()

    def start_typing_test(self):
        self.start_time = time.time()

        self.prompt_label.destroy()
        self.start_button.destroy()

        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_typing_test)
        self.submit_button.pack()

    def submit_typing_test(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

        user_input = self.user_input_entry.get()

        self.user_input_entry.destroy()
        self.submit_button.destroy()
        self.text_label.destroy()

        num_characters_typed = len(user_input)
        words_per_minute = (num_characters_typed / 5) / (self.elapsed_time / 60)
        accuracy = self.calculate_accuracy(user_input)

        stats_text = "Time taken: {:.2f} seconds\n".format(self.elapsed_time)
        stats_text += "Characters typed: {}\n".format(num_characters_typed)
        stats_text += "Words per minute (WPM): {:.2f}\n".format(words_per_minute)
        stats_text += "Accuracy: {:.2f}%".format(accuracy)

        self.stats_label.config(text=stats_text)

    def calculate_accuracy(self, user_input):
        prompt_words = self.prompt_text.split()
        user_words = user_input.split()

        correct_words = 0
        for i in range(min(len(prompt_words), len(user_words))):
            if prompt_words[i] == user_words[i]:
                correct_words += 1

        accuracy = (correct_words / len(prompt_words)) * 100
        return accuracy

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    typing_test = TypingTest()
    typing_test.run()
