class Colors:
    
    PINK = '\033[95m'
    LIGHT_PINK = '\033[38;5;218m'
    HOT_PINK = '\033[38;5;198m'
    DEEP_PINK = '\033[38;5;197m'
    
   
    WHITE = '\033[97m'
    LIGHT_GRAY = '\033[37m'
    GRAY = '\033[90m'
    

    CYAN = '\033[96m'
    LIGHT_CYAN = '\033[38;5;159m'
    
   
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    
 
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def rgb(r, g, b):

        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg_rgb(r, g, b):
        
        return f'\033[48;2;{r};{g};{b}m'
    
    @staticmethod
    def gradient_text(text, start_color, end_color):
        
        result = ""
        length = len(text)
        for i, char in enumerate(text):
            if i % 2 == 0:
                result += start_color + char
            else:
                result += end_color + char
        return result + Colors.RESET
    
    @staticmethod
    def pink_gradient(text):
     
        return Colors.gradient_text(text, Colors.HOT_PINK, Colors.LIGHT_PINK)
    
    @staticmethod
    def colorize(text, color):
      
        return f"{color}{text}{Colors.RESET}"