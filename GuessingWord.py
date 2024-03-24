import random

words = ["cake", "mango", "pancake", "fruit", "banana"]
random_word = random.choice(words)
word_length = len(random_word)
print("_ \t" * word_length)

chance = 3
while (chance != 0) and (word_length != 0):
    guess_letter = input("Enter your letter: ").lower()
    found = False
    for letter in random_word:
        if letter == guess_letter:
            print(f"You guessed correctly! The letter is {letter}")
            word_length -= 1
            found = True
    if not found:
        chance -= 1
        print(f"Sorry, '{guess_letter}' is not in the word. You have {chance} chances left.")

if word_length == 0:
    print(f"Congratulations! You've guessed the word correctly.The word is {random_word}")
else:
    print(f"Sorry, you've run out of chances. The word was '{random_word}'.")
