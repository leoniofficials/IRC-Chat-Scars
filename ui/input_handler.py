"""
Bitch-X Input Handler
Handles user input and formatting
"""

from datetime import datetime
from utils.colors import Colors
from handlers.message_handler import MessageHandler

class InputHandler:
    def __init__(self, username):
        self.username = username
        self.message_handler = MessageHandler()
        self.command_history = []
        self.max_history = 50
    
    def get_input(self):
        """Get input from user with styled prompt"""
        try:
            prompt = f"{Colors.PINK}>>> {Colors.RESET}"
            message = input(prompt).strip()
            
            if message:
                self.add_to_history(message)
            
            return message
        except EOFError:
            return None
        except KeyboardInterrupt:
            return '/quit'
    
    def format_message(self, message):
        """Format message before sending"""
        # Validate message
        is_valid, error = self.message_handler.validate_message(message)
        
        if not is_valid:
            print(self.message_handler.format_error_message(error))
            return None
        
        # Sanitize message
        sanitized = self.message_handler.sanitize_message(message)
        
        # Format with timestamp and username
        formatted = self.message_handler.format_chat_message(self.username, sanitized)
        
        return formatted
    
    def add_to_history(self, command):
        """Add command to history"""
        self.command_history.append(command)
        
        if len(self.command_history) > self.max_history:
            self.command_history.pop(0)
    
    def get_history(self):
        """Get command history"""
        return self.command_history
    
    def clear_history(self):
        """Clear command history"""
        self.command_history.clear()
    
    def show_typing_indicator(self):
        """Show typing indicator"""
        print(f"{Colors.GRAY}[typing...]{Colors.RESET}", end='\r', flush=True)
    
    def clear_line(self):
        """Clear current line"""
        print('\r' + ' ' * 80 + '\r', end='', flush=True)