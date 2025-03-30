import sqlite3
import bcrypt
from config import DATABASE_NAME

def register_user(username, password):
    """Register a new user with hashed password"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return "Username already exists. Please choose another."

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    return "Registration successful! You can now log in."

def login_user(username, password):
    """Verify user login"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()

    if user:
        user_id, stored_password = user
        # Check if password matches the hashed one
        if bcrypt.checkpw(password.encode(), stored_password):
            return user_id  # Return user ID on successful login
        else:
            return None  # Wrong password
    else:
        return None  # User not found

# Test Registration & Login (Uncomment to test)
# print(register_user("testuser", "securepassword"))
# print(login_user("testuser", "securepassword"))
