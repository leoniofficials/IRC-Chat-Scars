import socket
import threading
import sys
import os
from config import CLIENT_CONFIG
from utils.colors import Colors
from ui.banner import show_banner
from ui.input_handler import InputHandler
from handlers.receive_handler import ReceiveHandler

class BitchXClient:
    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.client_socket = None
        self.running = False
        self.receive_handler = None
        
    def connect(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        show_banner()
        
     
        print(f"{Colors.LIGHT_PINK}[*] Enter server details:{Colors.RESET}")
        self.host = input(f"{Colors.WHITE}Server IP: {Colors.RESET}").strip() or CLIENT_CONFIG['default_host']
        
        port_input = input(f"{Colors.WHITE}Server Port [{CLIENT_CONFIG['default_port']}]: {Colors.RESET}").strip()
        self.port = int(port_input) if port_input else CLIENT_CONFIG['default_port']
        
        self.username = input(f"{Colors.PINK}Username: {Colors.RESET}").strip()
        
        if not self.username:
            print(f"{Colors.RED}[!] Username required!{Colors.RESET}")
            sys.exit(1)
        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            self.running = True
            
      
            self.client_socket.send(self.username.encode('utf-8'))
            
            print(f"\n{Colors.PINK}╔══════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.WHITE}║     Connected to Bitch-X Server     ║{Colors.RESET}")
            print(f"{Colors.PINK}╚══════════════════════════════════════╝{Colors.RESET}\n")
            

            self.receive_handler = ReceiveHandler(self.client_socket, self.disconnect)
            self.receive_handler.start()
            
         
            self.handle_input()
            
        except Exception as e:
            print(f"{Colors.RED}[!] Connection failed: {e}{Colors.RESET}")
            sys.exit(1)
    
    def handle_input(self):
  
        input_handler = InputHandler(self.username)
        
        while self.running:
            try:
                message = input_handler.get_input()
                
                if not message:
                    continue
                
                if message.lower() in ['/quit', '/exit', '/q']:
                    self.disconnect()
                    break
                
                if message.lower() == '/help':
                    self.show_help()
                    continue
                
               
                formatted_msg = input_handler.format_message(message)
                if formatted_msg:
                    self.client_socket.send(formatted_msg.encode('utf-8'))
                
            except KeyboardInterrupt:
                self.disconnect()
                break
            except Exception as e:
                print(f"{Colors.RED}[ERROR] Input error: {e}{Colors.RESET}")
                break
    
    def show_help(self):
 
        print(f"\n{Colors.PINK}╔════════════ Bitch-X Commands ═══════════╗{Colors.RESET}")
        print(f"{Colors.WHITE}║ /quit, /exit, /q  - Disconnect          ║{Colors.RESET}")
        print(f"{Colors.WHITE}║ /help            - Show this help       ║{Colors.RESET}")
        print(f"{Colors.PINK}╚═════════════════════════════════════════╝{Colors.RESET}\n")
    
    def disconnect(self):
    
        self.running = False
        
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        
        print(f"\n{Colors.PINK}[*] Disconnected from server{Colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    client = BitchXClient()
    try:
        client.connect()
    except KeyboardInterrupt:
        print(f"\n{Colors.PINK}[!] Client interrupted{Colors.RESET}")
        sys.exit(0)