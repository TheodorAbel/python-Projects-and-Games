import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextBrowser, QPushButton, QMessageBox
from auth import register_user, login_user
from chatbot import get_ai_response, save_chat
from config import DATABASE_NAME

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.user_id = None  # Store logged-in user ID
        self.init_ui()

    def init_ui(self):
        """Initialize the GUI layout"""
        self.setWindowTitle("AI Chatbot")
        self.setGeometry(200, 200, 500, 600)

        layout = QVBoxLayout()

        # Welcome Message
        self.label = QLabel("Welcome to AI Chatbot! Please log in or register.")
        layout.addWidget(self.label)

        # Username Input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        # Register Button
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.handle_register)
        layout.addWidget(self.register_button)

        # Chat History Display
        self.chat_display = QTextBrowser()
        self.chat_display.setVisible(False)  # Hide until user logs in
        layout.addWidget(self.chat_display)

        # Message Input
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type a message...")
        self.message_input.setVisible(False)
        layout.addWidget(self.message_input)

        # Send Button
        self.send_button = QPushButton("Send")
        self.send_button.setVisible(False)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def handle_login(self):
        """Handle user login"""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        user_id = login_user(username, password)
        if user_id:
            self.user_id = user_id
            self.label.setText(f"Welcome, {username}! Start chatting below.")
            self.show_chat_interface()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def handle_register(self):
        """Handle new user registration"""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        message = register_user(username, password)
        QMessageBox.information(self, "Registration", message)

    def show_chat_interface(self):
        """Show the chat input and history after login"""
        self.chat_display.setVisible(True)
        self.message_input.setVisible(True)
        self.send_button.setVisible(True)
        self.username_input.setVisible(False)
        self.password_input.setVisible(False)
        self.login_button.setVisible(False)
        self.register_button.setVisible(False)
        self.load_chat_history()

    def load_chat_history(self):
        """Load previous chat history for the logged-in user"""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT message, response FROM chat_history WHERE user_id = ?", (self.user_id,))
        chats = cursor.fetchall()
        conn.close()

        self.chat_display.clear()
        for user_msg, bot_reply in chats:
            self.chat_display.append(f"🧑 You: {user_msg}")
            self.chat_display.append(f"🤖 Bot: {bot_reply}\n")

    def send_message(self):
        """Send user message and get AI response"""
        user_input = self.message_input.text().strip()
        if not user_input:
            return

        bot_response = get_ai_response(user_input)
        self.chat_display.append(f"🧑 You: {user_input}")
        self.chat_display.append(f"🤖 Bot: {bot_response}\n")

        save_chat(self.user_id, user_input, bot_response)
        self.message_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_gui = ChatbotGUI()
    chatbot_gui.show()
    sys.exit(app.exec_())
