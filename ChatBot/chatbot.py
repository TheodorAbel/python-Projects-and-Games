import openai
import sqlite3
from config import OPENAI_API_KEY, DATABASE_NAME
from auth import register_user, login_user

# Print OpenAI version
print("OpenAI Version:", openai.__version__)

# Set OpenAI API key (use the correct method of accessing the key from your config)
openai.api_key = OPENAI_API_KEY

def get_ai_response(user_input):
    try:
        # Use the correct method for chat-based models
        response = openai.Completion.create(  # Correct method
            model="gpt-3.5-turbo",  # Or "gpt-4", depending on which model you want
            prompt=user_input,
            max_tokens=150
        )

        # Extract the response from the API
        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"Error: {str(e)}"

def save_chat(user_id, user_message, bot_response):
    """Save chat messages in the database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO chat_history (user_id, message, response) VALUES (?, ?, ?)", 
                   (user_id, user_message, bot_response))
    
    conn.commit()
    conn.close()

def main():
    """Main chatbot function with authentication"""
    print("Welcome to the AI Chatbot!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            print(register_user(username, password))
        
        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            user_id = login_user(username, password)

            if user_id:
                print(f"✅ Login successful! Welcome, {username}.\n")
                
                # Start chatbot session
                while True:
                    user_input = input("You: ")
                    if user_input.lower() in ["exit", "quit"]:
                        print("Goodbye!")
                        break
                    
                    bot_response = get_ai_response(user_input)
                    print(f"Bot: {bot_response}")

                    # Save chat history
                    save_chat(user_id, user_input, bot_response)
            else:
                print("❌ Invalid username or password. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
