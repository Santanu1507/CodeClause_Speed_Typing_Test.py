import time

def typing_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text as fast as you can.\n")
    print(prompt_text)
    input("Press Enter when you are ready to start...")

    start_time = time.time()

    user_input = input("\nStart typing: ")

    end_time = time.time()

    # Calculate the time taken in seconds
    elapsed_time = end_time - start_time

    # Calculate the number of characters typed by the user
    num_characters_typed = len(user_input)

    # Calculate words per minute (WPM) and accuracy
    words_per_minute = (num_characters_typed / 5) / (elapsed_time / 60)
    accuracy = calculate_accuracy(prompt_text, user_input)

    print("\nTime taken: {:.2f} seconds".format(elapsed_time))
    print("Characters typed: {}".format(num_characters_typed))
    print("Words per minute (WPM): {:.2f}".format(words_per_minute))
    print("Accuracy: {:.2f}%".format(accuracy))

def calculate_accuracy(prompt_text, user_input):
    prompt_words = prompt_text.split()
    user_words = user_input.split()

    correct_words = 0
    for i in range(min(len(prompt_words), len(user_words))):
        if prompt_words[i] == user_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(prompt_words)) * 100
    return accuracy

if __name__ == "__main__":
    typing_test()