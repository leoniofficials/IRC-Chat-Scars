import socket
import threading
import sys
from datetime import datetime
from config import SERVER_CONFIG
from utils.colors import Colors
from handlers.client_handler import ClientHandler
from handlers.message_handler import MessageHandler

class BitchXServer:
    def __init__(self):
        self.host = SERVER_CONFIG['host']
        self.port = SERVER_CONFIG['port']
        self.server_socket = None
        self.clients = []
        self.client_handlers = {}
        self.message_handler = MessageHandler()
        self.running = False
        
    def start(self):
    
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(SERVER_CONFIG['max_clients'])
            self.running = True
            
            print(f"{Colors.PINK}╔══════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.WHITE}║     Bitch-X Chat Server Active      ║{Colors.RESET}")
            print(f"{Colors.PINK}╚══════════════════════════════════════╝{Colors.RESET}")
            print(f"{Colors.LIGHT_PINK}[*] Listening on {self.host}:{self.port}{Colors.RESET}\n")
            
            self.accept_connections()
            
        except Exception as e:
            print(f"{Colors.RED}[ERROR] Server start failed: {e}{Colors.RESET}")
            sys.exit(1)
    
    def accept_connections(self):
        
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                
                handler = ClientHandler(
                    client_socket, 
                    address, 
                    self.clients,
                    self.broadcast_message,
                    self.remove_client
                )
                
                self.client_handlers[address] = handler
                handler.start()
                
                print(f"{Colors.CYAN}[INFO] New connection from {address}{Colors.RESET}")
                
            except Exception as e:
                if self.running:
                    print(f"{Colors.RED}[ERROR] Accept connection error: {e}{Colors.RESET}")
    
    def broadcast_message(self, message, sender_socket=None):
   
        for client in self.clients[:]:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    self.remove_client(client)
    
    def remove_client(self, client_socket):
        
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            try:
                client_socket.close()
            except:
                pass
    
    def shutdown(self):
     
        self.running = False
        print(f"{Colors.CYAN}[INFO] Shutting down server...{Colors.RESET}")
        
        for client in self.clients[:]:
            try:
                client.close()
            except:
                pass
        
        if self.server_socket:
            self.server_socket.close()
        
        print(f"\n{Colors.PINK}[*] Server shutdown complete{Colors.RESET}")

if __name__ == "__main__":
    server = BitchXServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print(f"\n{Colors.PINK}[!] Server interrupted{Colors.RESET}")
        server.shutdown()
        sys.exit(0)