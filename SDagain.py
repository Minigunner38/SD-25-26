import pyautogui, tkinter, webcolors, math

"""
Checklist:
    - Toggle on and off
    - UI with settings and stuff
    - move slowly at edges of screen instead of snapping
    - transpancy slider
    - fix color names
"""

Display = tkinter.Tk()


OL = tkinter.Toplevel(Display)
OL.overrideredirect(True)
OL.attributes("-topmost", True)
OL.attributes("-alpha", 1)

text = tkinter.Label(OL, font=("Lexend", 10), bg="white", fg="white", padx=8, pady=4, anchor="w", justify="left")
text.pack(fill="x")
border = tkinter.Frame(OL, bg="#10141C", padx=8, pady=8)
border.pack(fill="x")
sample = tkinter.Label(border, padx=8, pady=38, width=20)
sample.pack(fill="x")

width = Display.winfo_screenwidth()
height = Display.winfo_screenheight()


Enabled = True

def Color(rgb):
    min = float('inf')
    save = None
    for name in webcolors.names("css3"):
        r, g, b = webcolors.name_to_rgb(name)
        if math.sqrt((r - rgb[0]) ** 2 + (g - rgb[1]) ** 2 + (b - rgb[2]) ** 2) < min:
            min = math.sqrt((r - rgb[0]) ** 2 + (g - rgb[1]) ** 2 + (b - rgb[2]) ** 2)
            save = name
    return save

def Update():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    hex_color = f'#{r:02X}{g:02X}{b:02X}'
    OL_width = OL.winfo_reqwidth()
    OL_height = OL.winfo_reqheight()

    text.config(text=f"Color: {Color((r, g, b)).title()}\nRGB: ({r}, {g}, {b})\nHEX: {hex_color}", bg="#10141C")
    sample.config(bg=hex_color)

    
    if x + OL_width + 15 > width and y + OL_height + 15 > height:
        OL.geometry(f"+{x-OL_width-15}+{y-OL_height-15}")
    elif x + OL_width + 15 > width:
        OL.geometry(f"+{x-OL_width-15}+{y+15}")
    elif y + OL_height + 15 > height:
        OL.geometry(f"+{x+15}+{y-OL_height-15}")
    else:
        OL.geometry(f"+{x+15}+{y+15}")
    print(x, y)
    Display.after(3, Update)

Update()
OL.mainloop()
