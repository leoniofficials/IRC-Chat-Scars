"""
Bitch-X Chat Configuration
Central configuration file for server and client settings
"""
SERVER_CONFIG = {
    'host': '0.0.0.0',  
    'port': 7762,
    'max_clients': 50,
    'buffer_size': 4096,
    'encoding': 'utf-8'
}

# Client Configuration
CLIENT_CONFIG = {
    'default_host': '127.0.0.1',
    'default_port': 7762,
    'buffer_size': 4096,
    'encoding': 'utf-8',
    'max_username_length': 20,
    'max_message_length': 500
}

# UI Configuration
UI_CONFIG = {
    'banner_style': 'standard',
    'show_timestamps': True,
    'timestamp_format': '%H:%M:%S',
    'message_prefix': '>>>',
    'system_prefix': '***'
}

# Color Theme Configuration
THEME_CONFIG = {
    'primary': '\033[95m',      
    'secondary': '\033[97m',   
    'accent': '\033[96m',      
    'success': '\033[92m',      
    'warning': '\033[93m',      
    'error': '\033[91m',        
    'reset': '\033[0m'
}

# Feature Flags
FEATURES = {
    'private_messages': True,
    'file_transfer': False,
    'encryption': False,
    'user_list': True,
    'typing_indicator': False
}