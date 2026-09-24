import random


WORDS = [
	"python",
	"computer",
	"keyboard",
	"programming",
	"developer",
	"function",
	"internet",
]

HANGMAN = [
	"""
	 +---+
		 |
		 |
		 |
		===
	""",
	"""
	 +---+
	 O   |
		 |
		 |
		===
	""",
	"""
	 +---+
	 O   |
	 |   |
		 |
		===
	""",
	"""
	 +---+
	 O   |
	/|   |
		 |
		===
	""",
	"""
	 +---+
	 O   |
	/|\\  |
		 |
		===
	""",
	"""
	 +---+
	 O   |
	/|\\  |
	/    |
		===
	""",
	"""
	 +---+
	 O   |
	/|\\  |
	/ \\  |
		===
	""",
]


def play_hangman():
	word = random.choice(WORDS)
	correct_letters = set()
	wrong_letters = set()
	max_wrong_guesses = len(HANGMAN) - 1

	print("Welcome to Hangman!")
	print(f"You have {max_wrong_guesses} wrong guesses available.")

	while len(wrong_letters) < max_wrong_guesses:
		print(HANGMAN[len(wrong_letters)])
		display = " ".join(
			letter if letter in correct_letters else "_"
			for letter in word
		)
		print(f"Word: {display}")
		print("Wrong letters:", " ".join(sorted(wrong_letters)) or "None")

		if all(letter in correct_letters for letter in word):
			print(f"You won! The word was '{word}'.")
			return

		guess = input("Guess one letter: ").strip().lower()

		if len(guess) != 1 or not guess.isalpha():
			print("Please enter exactly one letter.")
			continue

		if guess in correct_letters or guess in wrong_letters:
			print("You already guessed that letter.")
			continue

		if guess in word:
			correct_letters.add(guess)
			print("Correct!")
		else:
			wrong_letters.add(guess)
			print("Wrong guess!")

	print(HANGMAN[-1])
	print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
	play_hangman()
