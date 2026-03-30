import random
import re
import datetime

class SimpleAIChatbot:
    def __init__(self):
        self.name = "Alex"
        self.responses = {
            # Greetings
            r'hello|hi|hey|good morning|good evening': [
                "Hello! 👋 How can I help you today?",
                "Hi there! 😊 What's up?",
                "Hey! Great to see you! How are you?",
                "Hello! Ready to chat? 🚀"
            ],
            
            # How are you
            r'how are you|how\'s it going': [
                "I'm doing great, thanks for asking! 😄 How about you?",
                "Fantastic! Just chilling in the digital world 💻 How are you?",
                "All good here! How's your day going? 🌟"
            ],
            
            # Name questions
            r'what\'s your name|who are you|your name': [
                f"I'm {self.name}! Your friendly AI assistant 🤖",
                f"Call me {self.name}! Nice to meet you! 😊",
                f"I'm {self.name}, here to help you! 🚀"
            ],
            
            # Age questions
            r'how old|your age': [
                "I'm timeless! Just born yesterday in AI years 😄",
                "Age is just a number. I'm eternally young! 💫",
                "I don't age like humans. I'm always learning! 📚"
            ],
            
            # Time/Date
            r'time|date|day': [
                f"Right now it's {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                f"Current time: {datetime.datetime.now().strftime('%H:%M')}",
                f"Today's date: {datetime.datetime.now().strftime('%B %d, %Y')}"
            ],
            
            # Help
            r'help|what can you do': [
                "I can chat about anything! Ask me:\n• How I'm doing\n• The time/date\n• Jokes\n• Weather (fake 😄)\n• Math problems\n• Or just say hi! 😊",
                "I'm great at:\n✅ Casual conversation\n✅ Telling jokes\n✅ Time/Date info\n✅ Simple math\n• Try asking me something fun!"
            ],
            
            # Jokes
            r'joke|funny|tell me a joke': [
                "Why don't scientists trust atoms? Because they make up everything! 😄",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾😂",
                "Why don't eggs tell jokes? They'd crack each other up! 🥚😆",
                "What do you call fake spaghetti? An impasta! 🍝🤣"
            ],
            
            # Weather (fake responses)
            r'weather': [
                "☀️ It's sunny and 75°F here in AI-land!",
                "🌤️ Perfect weather today - 72°F and clear skies!",
                "🌈 Looks like a beautiful day outside! 😊"
            ],
            
            # Math (simple calculator)
            r'calculate|math|(\d+\s*[\+\-\*\/]\s*\d+)': [
                self.calculate_match
            ],
            
            # Goodbye
            r'bye|goodbye|see you|exit|quit': [
                "Goodbye! Have a great day! 👋✨",
                "See you later! Take care! 😊🙋",
                "Bye bye! Come chat again soon! 🚀"
            ],
            
            # Default responses
            r'.*': [
                "That's interesting! Tell me more 😊",
                "Cool! What else? 🤔",
                "I see! Anything else on your mind? 💭",
                "Nice! Keep talking! 😄",
                "Hmm, interesting point! What next? 🚀"
            ]
        }
    
    def calculate_match(self, message):
        """Simple calculator for math expressions"""
        try:
            # Extract numbers and operator
            math_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', message)
            if math_match:
                num1 = int(math_match.group(1))
                op = math_match.group(2)
                num2 = int(math_match.group(3))
                
                if op == '+': return f"{num1} + {num2} = {num1 + num2}"
                elif op == '-': return f"{num1} - {num2} = {num1 - num2}"
                elif op == '*': return f"{num1} × {num2} = {num1 * num2}"
                elif op == '/':
                    if num2 != 0:
                        return f"{num1} ÷ {num2} = {num1 / num2:.2f}"
                    else:
                        return "Can't divide by zero! 😅"
        except:
            pass
        return "Try something like: calculate 5 + 3"
    
    def get_response(self, user_input):
        """Find best response for user input"""
        user_input = user_input.lower()
        
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                if callable(responses[0]):
                    return responses[0](user_input)
                else:
                    return random.choice(responses)
        
        return "Hmm, not sure about that one! Try asking about jokes, time, or math 😊"

def main():
    bot = SimpleAIChatbot()
    
    print("🤖" + "="*50)
    print("     Welcome to Simple AI Chatbot!")
    print("     Type 'quit' or 'bye' to exit")
    print("="*50 + "🤖")
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print(f"\n🤖 {bot.name}: Goodbye! Have a wonderful day! 👋✨")
            break
        
        if user_input:
            response = bot.get_response(user_input)
            print(f"🤖 {bot.name}: {response}\n")

if __name__ == "__main__":
    main()