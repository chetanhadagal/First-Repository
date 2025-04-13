import time

# Welcome message
print("🤖 Welcome to the Interview ChatBot!")
print("Type 'exit' anytime to quit.\n")

# List of interview questions
questions = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?",
    "Where do you see yourself in 5 years?",
    "Can you work under pressure?",
    "Do you prefer to work alone or in a team?",
    "Do you have any questions for us?"
]

# Function to simulate bot typing
def bot_say(message):
    print("\nBot:", message)
    time.sleep(1)

# Start interview
bot_say("Let's start the interview!")

for question in questions:
    bot_say(question)
    answer = input("You: ")
    
    if answer.lower() == "exit":
        bot_say("Thank you for your time! Have a great day.")
        break
    
    bot_say("Got it. Let's move to the next question!")

bot_say("This concludes our interview. Good luck! 🍀")
