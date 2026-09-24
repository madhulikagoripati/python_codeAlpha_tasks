from datetime import datetime


def get_response(message, user_name):
	message = message.lower().strip()

	if message in {"bye", "exit", "quit"}:
		return "Goodbye! Have a great day.", True, user_name

	if message in {"hi", "hello", "hey"}:
		name = f", {user_name}" if user_name else ""
		return f"Hello{name}! How can I help you?", False, user_name

	if message in {"help", "what can you do"}:
		return (
			"You can greet me, tell me your name, ask for the time or date, "
			"or type 'bye' to exit."
		), False, user_name

	if message.startswith("my name is "):
		new_name = message.removeprefix("my name is ").strip().title()
		if new_name:
			return f"Nice to meet you, {new_name}!", False, new_name

	if "what is my name" in message or "do you know my name" in message:
		if user_name:
			return f"Your name is {user_name}.", False, user_name
		return "I do not know your name yet. Tell me by saying 'my name is ...'.", False, user_name

	if "time" in message:
		current_time = datetime.now().strftime("%I:%M %p")
		return f"The current time is {current_time}.", False, user_name

	if "date" in message or "today" in message:
		current_date = datetime.now().strftime("%A, %B %d, %Y")
		return f"Today is {current_date}.", False, user_name

	if "how are you" in message:
		return "I am doing well. Thanks for asking!", False, user_name

	return "I am not sure how to answer that. Type 'help' to see what I can do.", False, user_name


def run_chatbot():
	print("ChatBot: Hello! Type 'help' for options or 'bye' to exit.")
	user_name = ""

	while True:
		message = input("You: ").strip()

		if not message:
			print("ChatBot: Please type a message.")
			continue

		response, should_exit, user_name = get_response(message, user_name)
		print(f"ChatBot: {response}")

		if should_exit:
			break


if __name__ == "__main__":
	run_chatbot()
