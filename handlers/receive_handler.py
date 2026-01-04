"""
Bitch-X Receive Handler
Handles incoming messages on client side
"""

import threading
import socket
from config import CLIENT_CONFIG
from utils.colors import Colors

class ReceiveHandler(threading.Thread):
    def __init__(self, client_socket, disconnect_callback):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.disconnect_callback = disconnect_callback
        self.running = True
        self.daemon = True
    
    def run(self):
        """Main receive loop"""
        while self.running:
            try:
                message = self.client_socket.recv(CLIENT_CONFIG['buffer_size']).decode('utf-8')
                
                if not message:
                    print(f"{Colors.YELLOW}[WARNING] Connection lost{Colors.RESET}")
                    self.disconnect_callback()
                    break
                
                # Display received message
                self.display_message(message)
                
            except socket.error as e:
                print(f"{Colors.RED}[ERROR] Socket error: {e}{Colors.RESET}")
                self.disconnect_callback()
                break
            except Exception as e:
                print(f"{Colors.RED}[ERROR] Receive error: {e}{Colors.RESET}")
                break
    
    def display_message(self, message):
        """Display received message"""
        # Clear current line and print message
        print(f"\r{message}")
        # Redisplay input prompt
        print(f"{Colors.PINK}>>> {Colors.RESET}", end='', flush=True)
    
    def stop(self):
        """Stop the receive handler"""
        self.running = False