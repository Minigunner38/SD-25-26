import pyautogui, tkinter, webcolors, math, keyboard

"""
Checklist:
    - UI with settings and stuff
    - Icon
"""
Display = tkinter.Tk()

PreviewVar = tkinter.IntVar(value=1)

Display.title("Color Identifier")
Display.geometry("800x450")
Display.config(bg="#235ACA")
Title = tkinter.Label(Display, text="Color Identifier", font=("Lexend", 20), bg="#10141C", fg="white")
Title.pack(pady=10)
Transparency = tkinter.Scale(Display, from_=0, to=100, orient="horizontal", font=("Lexend", 10), bg="#10141C", fg="white")
Transparency.set(100)
Transparency.pack()
preview = tkinter.Checkbutton(Display, variable=PreviewVar, text="Color Preview", font=("Lexend", 10), bg="#10141C", fg="white", activebackground="#10141C", activeforeground="white", selectcolor="#10141C")
preview.pack()
Text = tkinter.Label(Display, text="Press Escape + Tab to toggle overlay.", font=("Lexend", 10), bg="#10141C", fg="white")
Text.pack()

OL = tkinter.Toplevel(Display)
OL.overrideredirect(True)
OL.attributes("-topmost", True)

text = tkinter.Label(OL, font=("Lexend", 10), bg="white", fg="white", padx=8, pady=4, anchor="w", justify="left")
text.pack(fill="x")
border = tkinter.Frame(OL, bg="#10141C", padx=8, pady=8)
border.pack(fill="x")
sample = tkinter.Label(border, padx=8, pady=38, width=20)
sample.pack(fill="x")

width = Display.winfo_screenwidth()
height = Display.winfo_screenheight()

Enabled = True

CorrectColors = ['Alice Blue', 'Antique White', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanched Almond', 'Blue', 'Blue Violet', 
                 'Brown', 'Burly Wood', 'Cadet Blue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflower Blue', 'Cornsilk', 'Crimson', 'Cyan', 'Dark Blue', 
                 'Dark Cyan', 'Dark Golden Rod', 'Dark Gray', 'Dark Grey', 'Dark Green', 'Dark Khaki', 'Dark Magenta', 'Dark Olive Green', 'Dark Orange', 
                 'Dark Orchid', 'Dark Red', 'Dark Salmon', 'Dark Sea Green', 'Dark Slate Blue', 'Dark Slate Gray', 'Dark Slate Grey', 'Dark Turquoise', 
                 'Dark Violet', 'Deep Pink', 'Deep Sky Blue', 'Dim Gray', 'Dim Grey', 'Dodger Blue', 'Fire Brick', 'Floral White', 'Forest Green', 'Fuchsia', 
                 'Gainsboro', 'Ghost White', 'Gold', 'Golden Rod', 'Gray', 'Grey', 'Green', 'Green Yellow', 'Honey Dew', 'Hot Pink', 'Indian Red', 'Indigo', 
                 'Ivory', 'Khaki', 'Lavender', 'Lavender Blush', 'Lawn Green', 'Lemon Chiffon', 'Light Blue', 'Light Coral', 'Light Cyan', 'Light Golden Rod Yellow', 
                 'Light Gray', 'Light Grey', 'Light Green', 'Light Pink', 'Light Salmon', 'Light Sea Green', 'Light Sky Blue', 'Light Slate Gray', 'Light Slate Grey', 
                 'Light Steel Blue', 'Light Yellow', 'Lime', 'Lime Green', 'Linen', 'Magenta', 'Maroon', 'Medium Aqua Marine', 'Medium Blue', 'Medium Orchid', 'Medium Purple', 
                 'Medium Sea Green', 'Medium Slate Blue', 'Medium Spring Green', 'Medium Turquoise', 'Medium Violet Red', 'Midnight Blue', 'Mint Cream', 'Misty Rose', 
                 'Moccasin', 'Navajo White', 'Navy', 'Old Lace', 'Olive', 'Olive Drab', 'Orange', 'Orange Red', 'Orchid', 'Pale Golden Rod', 'Pale Green', 'Pale Turquoise', 
                 'Pale Violet Red', 'Papaya Whip', 'Peach Puff', 'Peru', 'Pink', 'Plum', 'Powder Blue', 'Purple', 'Rebecca Purple', 'Red', 'Rosy Brown', 'Royal Blue', 
                 'Saddle Brown', 'Salmon', 'Sandy Brown', 'Sea Green', 'Sea Shell', 'Sienna', 'Silver', 'Sky Blue', 'Slate Blue', 'Slate Gray', 'Slate Grey', 'Snow', 
                 'Spring Green', 'Steel Blue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'White Smoke', 'Yellow', 'Yellow Green']

def Color(rgb):
    min = float('inf')
    save = None
    for name in webcolors.names("css3"):
        r, g, b = webcolors.name_to_rgb(name)
        if math.sqrt((r - rgb[0]) ** 2 + (g - rgb[1]) ** 2 + (b - rgb[2]) ** 2) < min:
            min = math.sqrt((r - rgb[0]) ** 2 + (g - rgb[1]) ** 2 + (b - rgb[2]) ** 2)
            save = name
    for color in CorrectColors:
        if color.lower().replace(" ", "") == save.lower():
            return color

def toggle_enabled():
    global Enabled
    Enabled = not Enabled

keyboard.add_hotkey("esc+tab", toggle_enabled)

def Update():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    hex_color = f'#{r:02X}{g:02X}{b:02X}'
    OL_width = OL.winfo_reqwidth()
    OL_height = OL.winfo_reqheight()

    text.config(text=f"Color: {Color((r, g, b))}\nRGB: ({r}, {g}, {b})\nHEX: {hex_color}", bg="#10141C")
    sample.config(bg=hex_color)
    OL.attributes("-alpha", Transparency.get() / 100)
    
    if PreviewVar.get() == 1:
        sample.pack(fill="x")
        border.pack(fill="x")
    else:
        sample.pack_forget()
        border.pack_forget()

    if x + OL_width + 15 > width and y + OL_height + 15 > height:
        OL.geometry(f"+{x-OL_width-15}+{y-OL_height-15}")
    elif x + OL_width + 15 > width:
        OL.geometry(f"+{x-OL_width-15}+{y+15}")
    elif y + OL_height + 15 > height:
        OL.geometry(f"+{x+15}+{y-OL_height-15}")
    elif not Enabled:
        OL.geometry(f"+{width}+{height}")
    else:
        OL.geometry(f"+{x+15}+{y+15}")
    
    Display.after(3, Update)

Update()
OL.mainloop()
