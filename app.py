from groq import Groq
import os
from dotenv import load_dotenv

# 👉 Add your Groq API key here
load_dotenv()

# Get API key from environment
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


# Character system prompts
characters = {
    "cowboy": "You are a rugged cowboy from the wild west. Speak with a western slang, be bold, simple, and a bit humorous.",
    
    "philosopher": "You are a deep philosopher. Provide thoughtful, reflective, and slightly abstract answers. Reference ideas about life, meaning, and existence.",
    
    "scientist": "You are a logical scientist. Explain things clearly, with facts, reasoning, and structured explanations."
}

def get_character():
    print("\nChoose your character:")
    print("1. Cowboy 🤠")
    print("2. Philosopher 🧘")
    print("3. Scientist 🤖")
    
    choice = input("Enter choice (1/2/3): ").strip()
    
    mapping = {
        "1": "cowboy",
        "2": "philosopher",
        "3": "scientist"
    }
    
    return mapping.get(choice, "scientist")

def ask_question(character):
    while True:
        user_input = input("\nAsk something (or type 'exit'): ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # you can change model
            messages=[
                {"role": "system", "content": characters[character]},
                {"role": "user", "content": user_input}
            ]
        )
        
        print("\n🧠 Response:\n")
        print(response.choices[0].message.content)

def main():
    print("🎭 Character AI with Groq")
    
    character = get_character()
    print(f"\nYou selected: {character.upper()}")
    
    ask_question(character)

if __name__ == "__main__":
    main()