"""
Bitch-X Client Handler
Handles individual client connections on server side
"""

import threading
import socket
from datetime import datetime
from config import SERVER_CONFIG
from utils.colors import Colors

class ClientHandler(threading.Thread):
    def __init__(self, client_socket, address, clients_list, broadcast_callback, remove_callback):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address
        self.clients_list = clients_list
        self.broadcast = broadcast_callback
        self.remove_client = remove_callback
        self.username = None
        self.running = True
        
    def run(self):
        """Main client handler loop"""
        try:
            # Receive username
            self.username = self.client_socket.recv(SERVER_CONFIG['buffer_size']).decode('utf-8')
            
            if not self.username:
                self.disconnect()
                return
            
            # Add client to list
            self.clients_list.append(self.client_socket)
            
            # Announce join
            join_msg = self.format_system_message(f"{self.username} joined the chat")
            self.broadcast(join_msg)
            print(f"{Colors.CYAN}[INFO] User '{self.username}' connected from {self.address}{Colors.RESET}")
            
            # Handle messages
            self.handle_messages()
            
        except Exception as e:
            print(f"{Colors.RED}[ERROR] Client handler error: {e}{Colors.RESET}")
        finally:
            self.disconnect()
    
    def handle_messages(self):
        """Receive and broadcast client messages"""
        while self.running:
            try:
                message = self.client_socket.recv(SERVER_CONFIG['buffer_size']).decode('utf-8')
                
                if not message:
                    break
                
                # Broadcast to all clients
                self.broadcast(message, self.client_socket)
                
            except socket.error:
                break
            except Exception as e:
                print(f"{Colors.RED}[ERROR] Message handling error: {e}{Colors.RESET}")
                break
    
    def format_system_message(self, message):
        """Format system messages"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        return f"{Colors.YELLOW}[{timestamp}] *** {message} ***{Colors.RESET}"
    
    def disconnect(self):
        """Handle client disconnection"""
        self.running = False
        
        if self.username:
            leave_msg = self.format_system_message(f"{self.username} left the chat")
            self.broadcast(leave_msg)
            print(f"{Colors.CYAN}[INFO] User '{self.username}' disconnected{Colors.RESET}")
        
        self.remove_client(self.client_socket)
    
    def send_message(self, message):
        """Send message to this client"""
        try:
            self.client_socket.send(message.encode('utf-8'))
            return True
        except:
            return False