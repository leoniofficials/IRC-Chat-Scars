"""
Bitch-X Message Handler
Processes and formats chat messages
"""

from datetime import datetime
from config import UI_CONFIG, CLIENT_CONFIG
from utils.colors import Colors

class MessageHandler:
    def __init__(self):
        self.message_history = []
        self.max_history = 1000
    
    def format_chat_message(self, username, message):
        """Format a chat message with timestamp and styling"""
        timestamp = self.get_timestamp()
        
        formatted = (
            f"{Colors.GRAY}[{timestamp}] "
            f"{Colors.PINK}{username}{Colors.WHITE}: "
            f"{Colors.LIGHT_GRAY}{message}{Colors.RESET}"
        )
        
        return formatted
    
    def format_system_message(self, message):
        """Format a system message"""
        timestamp = self.get_timestamp()
        
        formatted = (
            f"{Colors.GRAY}[{timestamp}] "
            f"{Colors.YELLOW}*** {message} ***{Colors.RESET}"
        )
        
        return formatted
    
    def format_private_message(self, from_user, to_user, message):
        """Format a private message"""
        timestamp = self.get_timestamp()
        
        formatted = (
            f"{Colors.GRAY}[{timestamp}] "
            f"{Colors.HOT_PINK}[PM] {from_user} → {to_user}{Colors.WHITE}: "
            f"{Colors.LIGHT_GRAY}{message}{Colors.RESET}"
        )
        
        return formatted
    
    def format_error_message(self, message):
        """Format an error message"""
        return f"{Colors.RED}[ERROR] {message}{Colors.RESET}"
    
    def format_success_message(self, message):
        """Format a success message"""
        return f"{Colors.GREEN}[SUCCESS] {message}{Colors.RESET}"
    
    def validate_message(self, message):
        """Validate message content"""
        if not message or not message.strip():
            return False, "Message cannot be empty"
        
        if len(message) > CLIENT_CONFIG['max_message_length']:
            return False, f"Message too long (max {CLIENT_CONFIG['max_message_length']} chars)"
        
        return True, "Valid"
    
    def sanitize_message(self, message):
        """Sanitize message content"""
        # Remove control characters
        sanitized = ''.join(char for char in message if ord(char) >= 32 or char == '\n')
        
        # Trim whitespace
        sanitized = sanitized.strip()
        
        return sanitized
    
    def parse_command(self, message):
        """Parse command from message"""
        if not message.startswith('/'):
            return None, None
        
        parts = message.split(' ', 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        return command, args
    
    def add_to_history(self, message):
        """Add message to history"""
        self.message_history.append({
            'timestamp': datetime.now(),
            'content': message
        })
        
        # Maintain max history size
        if len(self.message_history) > self.max_history:
            self.message_history.pop(0)
    
    def get_timestamp(self):
        """Get formatted timestamp"""
        if UI_CONFIG['show_timestamps']:
            return datetime.now().strftime(UI_CONFIG['timestamp_format'])
        return ""
    
    def create_notification(self, notification_type, message):
        """Create a notification message"""
        icons = {
            'info': 'ℹ',
            'warning': '⚠',
            'error': '✖',
            'success': '✓',
            'user': '👤'
        }
        
        icon = icons.get(notification_type, '•')
        colors = {
            'info': Colors.CYAN,
            'warning': Colors.YELLOW,
            'error': Colors.RED,
            'success': Colors.GREEN,
            'user': Colors.PINK
        }
        
        color = colors.get(notification_type, Colors.WHITE)
        
        return f"{color}{icon} {message}{Colors.RESET}"