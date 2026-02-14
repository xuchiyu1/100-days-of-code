import random

# Hangman 图形
stages = [
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
display = ["_"] * word_length

lives = 6
end_of_game = False

print("Welcome to Hangman!")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # 已猜过提示
    if guess in display:
        print(f"You already guessed {guess}")

    # 检查字母
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    # 错误扣命
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    print(" ".join(display))
    print(stages[lives])

    # 胜利判断
    if "_" not in display:
        end_of_game = True
        print("You win!")
