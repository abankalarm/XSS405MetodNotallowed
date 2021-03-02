class Base:
    # Foreground:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
    # End colored text
    END = '\033[0m'
    NC ='\x1b[0m' # No Color

class ANSI_Compatible:
    END = '\x1b[0m'
    # If Foreground is False that means color effect on Background
    def Color(ColorNo, Foreground=True): # 0 - 255
        FB_G = 38 # Effect on foreground
        if Foreground != True:
            FB_G = 48 # Effect on background
        return '\x1b[' + str(FB_G) + ';5;' + str(ColorNo) + 'm'

class Formatting:
    Bold = "\x1b[1m"
    Dim = "\x1b[2m"
    Italic = "\x1b[3m"
    Underlined = "\x1b[4m"
    Blink = "\x1b[5m"
    Reverse = "\x1b[7m"
    Hidden = "\x1b[8m"
    # Reset part
    Reset = "\x1b[0m"
    Reset_Bold = "\x1b[21m"
    Reset_Dim = "\x1b[22m"
    Reset_Italic = "\x1b[23m"
    Reset_Underlined = "\x1b[24"
    Reset_Blink = "\x1b[25m"
    Reset_Reverse = "\x1b[27m"
    Reset_Hidden = "\x1b[28m"

class GColor: # Gnome supported
    END = "\x1b[0m"
    # If Foreground is False that means color effect on Background
    def RGB(R, G, B, Foreground=True): # R: 0-255  ,  G: 0-255  ,  B: 0-255
        FB_G = 38 # Effect on foreground
        if Foreground != True:
            FB_G = 48 # Effect on background
        return "\x1b[" + str(FB_G) + ";2;" + str(R) + ";" + str(G) + ";" + str(B) + "m"
