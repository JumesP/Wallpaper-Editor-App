from tkinter import *
from tkinter import ttk

class Wallpaper:
    def __init__(self, pattern, colour, length, extras, premium, lining, paste):
        self.pattern = pattern
        self.colour = colour
        self.length = length
        self.extra = extras
        self.premium = premium
        self.lining = lining
        self.paste = paste

# Initialising Window
main_window = Tk()                      # Creates main window
main_window.title("DIY Store")          # Renames the Page
main_window.geometry("775x450")         # Changes the size of the window

# Formatting Homepage Grid
main_window.columnconfigure(0, weight = 1)
main_window.columnconfigure(1, weight = 1)
main_window.rowconfigure(0, weight = 1)
main_window.rowconfigure(1, weight = 2)
main_window.rowconfigure(2, weight = 1)

def Header():
    header = Frame(main_window, height=66, width=5, bg="#484848")
    header.grid(row=0, column=0, columnspan=2, sticky="nwe")

    header.columnconfigure(0, weight = 1)
    header.columnconfigure(1, weight = 20)
    header.columnconfigure(2, weight = 1)

    menu = Button(header, text="Menu", height=2, width=5, name="menu_button")
    menu.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
    menu.bind('<Button-3>')

    title = Label(header, text="Welcome to the DIY Store!", padx=50, pady=0, name="diy_store", bg="#484848")
    title.grid(row=0, column=1, padx=100, pady=10, sticky="ew")

    checkout = Button(header, text="Checkout", height=2, width=5, name="checkout_button")
    checkout.grid(row=0, column=2, padx=20, pady=10, sticky="ne")
    checkout.bind('<Button-3>')

def CreatePattern1(pattern1):
    for x in range(0, 4):       # looping across
        x *= 50
        for y in range(0, 10):  # looping down
            y *= 20
            pattern1.create_polygon(2 + x, 24 + y, 12 + x, 4 + y, 42 + x, 4 + y, 52 + x, 24 + y, fill='#7B48DD', outline='black', width=2)


def CreatePattern2(pattern2):
    # pattern2_xLocations = [2, 14, 22, 30, 42, 34, 42, 30, 22, 14, 2, 10]
    # pattern2_yLocations = [25, 25, 0, 25, 25, 50, 75, 75, 100, 75, 75, 50]
    for x in range(0, 5):
        x *= 40
        for i in range(0, 2):
            i *= 100
            pattern2.create_polygon(2 + x, 25 + i, 14 + x, 25 + i, 22 + x, 0 + i, 30 + x, 25 + i, 42 + x, 25 + i,
                                    34 + x, 50 + i, 42 + x, 75 + i, 30 + x, 75 + i, 22 + x, 100 + i, 14 + x, 75 + i,
                                    2 + x, 75 + i, 10 + x, 50 + i, fill='#7B48DD')

def Pattern1(b):
    pattern1 = Canvas(b, name="pattern1", height=200, width=200, bg="#484848")
    pattern1.grid(row=1, column=0, pady=50, padx=50)

    CreatePattern1(pattern1)
    pattern1.bind("<Button-1>", pattern1_clicked)

def Pattern2(c):
    pattern2 = Canvas(c, name="pattern2", height=200, width=200, bg="#484848")
    pattern2.grid(row=1, column=1, pady=50, padx=50)

    CreatePattern2(pattern2)
    pattern2.bind("<Button-1>", pattern2_clicked)

def Homepage_Prices():
    pattern1_display = Label(main_window, text="Welcome to the DIY Store!", height=10, width=10, bg="white")
    pattern1_display.grid(row=2, column=0, sticky="n")

    pattern2_display = Label(main_window, text="Welcome to the DIY Store!", height=10, width=10, bg="white")
    pattern2_display.grid(row=2, column=1, sticky="n")

def pattern1_selected():
    pattern1_onclick = Tk()  # Creates main window
    pattern1_onclick.title("Pattern One")  # Renames the Page
    pattern1_onclick.geometry("600x300")  # Changes the size of the window

    pattern1 = Canvas(pattern1_onclick, name="pattern1", height=200, width=200, bg="#484848")
    pattern1.grid(row=0, column=0, pady=50, padx=50)


def pattern2_selected():
    pattern2_onclick = Tk()                 # Creates main window
    pattern2_onclick.title("Pattern Two")     # Renames the Page
    pattern2_onclick.geometry("600x300")    # Changes the size of the window

    pattern2 = Canvas(pattern2_onclick, name="pattern2", height=200, width=200, bg="#484848")
    pattern2.grid(row=0, column=0, pady=50, padx=50)

    #frame

def pattern1_clicked(event):
    print(event.widget._name + " clicked")
    pattern1_selected()



def pattern2_clicked(event):
    print(event.widget._name + " clicked")
    pattern2_selected()

def Homepage():
    Header()
    Pattern1(b=main_window)
    Pattern2(c=main_window)
    #Homepage_Prices()

Homepage()
main_window.mainloop()
