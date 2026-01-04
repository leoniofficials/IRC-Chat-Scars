from utils.colors import Colors
import platform
import sys
import random

def show_banner():
   
    
    banner = f"""
{Colors.HOT_PINK}        
         -*++---=:    =-=---=*        
       -*+*+--**+*+=-+=-=- ==+%*      
      *+-+- --+=+-+++=+#*#== ---*+    
      #+:*-*-#%%#--*-*++#% *+.=.=*    
      %*-=.-++   :+=--     =+*-+*     
      #%++===:+= %       +=*+***+     
         +:-*=*+#%+   **--*+***       
          +*--*-=#*==== .=-***        
           * **=**  =.=*:-*.#         
              *#-====*=*.             
                +--:****              
                * -  * #              
                   .##                
                    %
{Colors.RESET}
{Colors.LIGHT_PINK}    ╔═══════════════════════════════════════════════════╗
{Colors.WHITE}    ║ {Colors.HOT_PINK}[{Colors.WHITE}0x{random.randint(100, 999):03X}{Colors.HOT_PINK}]{Colors.PINK} irc client{Colors.WHITE}                                ║
{Colors.WHITE}    ║ {Colors.HOT_PINK}[{Colors.WHITE}0x{random.randint(100, 999):03X}{Colors.HOT_PINK}]{Colors.LIGHT_PINK} xwb, sususoftware.xyz{Colors.WHITE}                     ║
{Colors.WHITE}    ║ {Colors.HOT_PINK}[{Colors.WHITE}0x{random.randint(100, 999):03X}{Colors.HOT_PINK}]{Colors.GRAY} no log, just chatting{Colors.WHITE}                      ║
{Colors.LIGHT_PINK}    ╚═══════════════════════════════════════════════════╝{Colors.RESET}
"""
    
    print(banner)
    

    sys_info = f"{Colors.GRAY}    [{Colors.PINK}>{Colors.GRAY}] SYS: {Colors.WHITE}{platform.system()}{Colors.GRAY} | Python: {Colors.WHITE}{sys.version.split()[0]}{Colors.GRAY} | NET: {Colors.PINK}TCP/IP{Colors.GRAY} | ID: {Colors.HOT_PINK}0x{random.randint(1000, 9999):04X}{Colors.RESET}"
    print(sys_info)
    

    hex_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
    print(f"{Colors.GRAY}    [SESSION:{Colors.PINK}{hex_code}{Colors.GRAY}]{'═' * 35}{Colors.RESET}\n")

def show_connection_banner():

    banner = f"""
{Colors.GREEN}    ╔═══════════════════════════════════════════════════╗
{Colors.WHITE}    ║ {Colors.GREEN}[✓]{Colors.WHITE} TUNNEL ESTABLISHED • ENCRYPTION ACTIVE         ║
{Colors.GREEN}    ╚═══════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def show_disconnect_banner():
 
    banner = f"""
{Colors.RED}    ╔═══════════════════════════════════════════════════╗
{Colors.WHITE}    ║ {Colors.RED}[✖]{Colors.WHITE} SESSION TERMINATED • TRACES CLEARED            ║
{Colors.RED}    ╚═══════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def show_welcome_message(username):

    user_id = f"BX-{random.randint(10000, 99999)}"
    ghost_code = ''.join(random.choice('!@#$%^&*') for _ in range(4))
    message = f"""
{Colors.LIGHT_PINK}    ┌───────────────────────────────────────────────────┐
{Colors.WHITE}    │ {Colors.PINK}>>>{Colors.WHITE} ACCESS GRANTED {Colors.HOT_PINK}{ghost_code}{Colors.WHITE} WELCOME {Colors.HOT_PINK}{username.upper()}{Colors.WHITE} {Colors.PINK}<
{Colors.LIGHT_PINK}    │ {Colors.GRAY}└─[{Colors.HOT_PINK}USER_ID{Colors.GRAY}:{Colors.WHITE}{user_id}{Colors.GRAY}]─[{Colors.HOT_PINK}STATUS{Colors.GRAY}:{Colors.GREEN}ONLINE{Colors.GRAY}]
{Colors.LIGHT_PINK}    │ {Colors.CYAN}└─[{Colors.WHITE}Type {Colors.PINK}/help{Colors.WHITE} for chaos commands{Colors.CYAN}]
{Colors.LIGHT_PINK}    └───────────────────────────────────────────────────┘{Colors.RESET}
"""
    print(message)

def show_server_info(host, port, clients):

    ghost = ''.join(random.choice('█▓▒░') for _ in range(6))
    info = f"""
{Colors.PINK}    ╔═══════════════════════════════════════════════════╗
{Colors.WHITE}    ║ {Colors.HOT_PINK}>>> {Colors.WHITE}BITCH-X SERVER STATUS {Colors.HOT_PINK}{ghost}{Colors.WHITE}                ║
{Colors.PINK}    ╠═══════════════════════════════════════════════════╣
{Colors.WHITE}    ║ {Colors.GRAY}[{Colors.PINK}HOST{Colors.GRAY}]{Colors.WHITE} {host:<40} ║
{Colors.WHITE}    ║ {Colors.GRAY}[{Colors.PINK}PORT{Colors.GRAY}]{Colors.WHITE} {port:<40} ║
{Colors.WHITE}    ║ {Colors.GRAY}[{Colors.PINK}LIVE{Colors.GRAY}]{Colors.WHITE} {clients} Ghost(s) Connected{' ' * 24}║
{Colors.PINK}    ╚═══════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(info)

def show_hacker_prompt():

    hex1 = f"0x{random.randint(1000, 9999):04X}"
    hex2 = f"0x{random.randint(1000, 9999):04X}"
    hex3 = f"0x{random.randint(1000, 9999):04X}"
    
    prompts = [
        f"{Colors.HOT_PINK}[{Colors.WHITE}{hex1}{Colors.HOT_PINK}]{Colors.LIGHT_PINK} Bypassing firewalls...{Colors.RESET}",
        f"{Colors.CYAN}[{Colors.WHITE}{hex2}{Colors.CYAN}]{Colors.WHITE} Establishing dark tunnel...{Colors.RESET}",
        f"{Colors.GREEN}[{Colors.WHITE}{hex3}{Colors.GREEN}]{Colors.WHITE} You're in the shadows now{Colors.RESET}"
    ]
    
    for prompt in prompts:
        print(f"    {prompt}")