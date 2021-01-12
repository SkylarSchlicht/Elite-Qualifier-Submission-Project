import random

def generate_response(user_input):
  responses = [
    "How interesting!",
    "Really?!",
    "That's awesome!",
    "Wow!",
    "Great!",
    "Good!",
    "Glad to hear!",
    "Thanks for sharing",
    "Awesome!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'X'

  user_input = input("Hey, how are you doing?\n")

  while user_input != quit_character:
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()