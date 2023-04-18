'''
EDITOR NOTES:
    TO-DO LIST:
        - pattern 1 needs shrinking to match pattern 2
        - pattern 2 needs ironing out
        - create windows for shopping a wallpaper
        - homepage prices needs fitting on the homepage
        - homepage prices need filling in with details
        - colour selector

    i think that to add a colour selector, and add it to the checkout, i need to when opening a wallpaper editor,
    create a new class, update with features when they're clicked, then save it on the checkout page,
    that is the possible cleanest way to do it i think for now, worth giving a try tomorrow, 17/4/2023

    when pressing "add to checkout", you could add the class to a dictionary,
    bc im not to sure if you can create infinite classes, well you can, but changing the name every time.

'''
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
main_window.geometry("650x400")         # Changes the size of the window

# Formatting Homepage Grid - not needed
main_window.columnconfigure(0, weight = 1)
main_window.columnconfigure(1, weight = 1)
main_window.rowconfigure(0, weight = 1)
main_window.rowconfigure(1, weight = 3)
main_window.rowconfigure(2, weight = 0)

def Header():
    header = Frame(main_window, height=66, width=5, bg="#484848")
    header.grid(row=0, column=0, columnspan=2, sticky="nwe")

    header.columnconfigure(0, weight=1)  # also not needed
    header.columnconfigure(1, weight=20)
    header.columnconfigure(2, weight=1)

    menu_button = Button(header, text="Menu", height=2, width=5, name="menu_button")
    menu_button.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
    menu_button.bind('<Button-3>')
    menu_button.bind("<Button-1>", menu_button_clicked)

    title = Label(header, text="Welcome to the DIY Store!", padx=50, pady=0, name="diy_store", bg="#484848")
    title.grid(row=0, column=1, padx=100, pady=10, sticky="ew")

    checkout_button = Button(header, text="Checkout", height=2, width=5, name="checkout_button")
    checkout_button.grid(row=0, column=2, padx=20, pady=10, sticky="ne")
    checkout_button.bind('<Button-3>')
    checkout_button.bind("<Button-1>", checkout_button_clicked)

def CreatePattern1(pattern1):
    # pattern1_xLocations = [2, 12, 42, 52]
    # pattern1_yLocations = [24, 4, 4, 24]

    for x in range(0, 4):       # looping across
        x *= 50
        for y in range(0, 10):  # looping down
            y *= 20
            pattern1.create_polygon(2 + x, 24 + y, 12 + x, 4 + y, 42 + x, 4 + y, 52 + x, 24 + y,
                                    fill='#7B48DD', outline='black', width=2)

    # for x in range(0, 4):                               # looping across
    #     pattern1_Locations = []                         # resetting position
    #     if x > 3:                                       # loop for bottem row
    #         x = x - 5                                   # second rows x coordinates move back to the left of the screen
    #         y = 20                                      # moving it down
    #     else:
    #         y = 0
    #
    #     x1 = x * 50                                                         # shifting the shape right
    #     for alpha in range(0, 4):                                          # creating the shape
    #         pattern1_Locations.append(pattern1_xLocations[alpha] + x1)
    #         pattern1_Locations.append(pattern1_yLocations[alpha] + y)
    #
    #         pattern1.create_polygon(pattern1_Locations, fill='#7B48DD', outline='black', width=2)     # Creating pattern
    #         print(pattern1_Locations)
def CreatePattern2(pattern2):
    pattern2_xLocations = [14, 2, 10, 2, 14, 22, 30, 42, 34, 42, 30, 22]
    pattern2_yLocations = [75, 75, 50, 25, 25, 0, 25, 25, 50, 75, 75, 100]

    for x in range(0, 10):                              # looping across
        pattern2_Locations = []                         # resetting position
        if x > 4:                                       # loop for bottem row
            x = x - 5                                   # second rows x coordinates move back to the left of the screen
            y = 100                                     # moving it down
        else:
            y = 0
        x1 = x * 40                                                         # shifting the shape right

        for alpha in range(0, 12):                                          # creating the shape
            pattern2_Locations.append(pattern2_xLocations[alpha] + x1)
            pattern2_Locations.append(pattern2_yLocations[alpha] + y)

            pattern2.create_polygon(pattern2_Locations, fill='#7B48DD')     # Creating pattern

def Pattern1(location):
    pattern1 = Canvas(location, name="pattern1", height=200, width=200, bg="#484848")
    pattern1.grid(row=1, column=0, pady=50, padx=50)

    CreatePattern1(pattern1)
    pattern1.bind("<Button-1>", pattern1_clicked)
def Pattern2(location):
    pattern2 = Canvas(location, name="pattern2", height=200, width=200, bg="#484848")
    pattern2.grid(row=1, column=1, pady=50, padx=50)

    CreatePattern2(pattern2)
    pattern2.bind("<Button-1>", pattern2_clicked)


def Homepage_Prices():
    pattern1_display = Label(main_window, text="Welcome to the DIY Store!", height=10, width=10, bg="white")
    pattern1_display.grid(row=2, column=0, sticky="n")

    pattern2_display = Label(main_window, text="Welcome to the DIY Store!", height=10, width=10, bg="white")
    pattern2_display.grid(row=2, column=1, sticky="n")


def pattern1_selected():                        # Opens a page to specify an order of wallpaper patter 1
    pattern1_page = Tk()
    pattern1_page.title("Pattern One")
    pattern1_page.geometry("680x360")

    pattern1 = Canvas(pattern1_page, name="pattern1", height=200, width=200, bg="#484848")
    pattern1.grid(row=0, column=0, pady=50, padx=50)
    Pattern1(location=pattern1_page)

    Options(pattern1_page)

def pattern2_selected():                        # Opens a page to specify an order of wallpaper pattern 2
    pattern2_page = Tk()
    pattern2_page.title("Pattern Two")
    pattern2_page.geometry("680x360")

    pattern2 = Canvas(pattern2_page, name="pattern2", height=200, width=200, bg="#484848")
    pattern2.grid(row=1, column=0, rowspan=1, pady=50, padx=50, sticky="nws")
    Pattern2(location=pattern2_page)

    Options(pattern2_page)

def checkout_selected():
    checkout_page = Tk()
    checkout_page.title("Checkout")

def menu_selected():
    menu_page = Tk()
    menu_page.title("Checkout")

def Options(location):
    options = Frame(location, relief=RIDGE, width=100, name="options")
    options.grid(row=1, column=2, pady=50, padx=50)

    options.columnconfigure(0, weight=1)
    options.columnconfigure(1, weight=1)
    options.rowconfigure(0, weight=1)
    options.rowconfigure(1, weight=2)

    #colour_selector(options)

    colour_selector = Frame(options, bg="blue", width=100, height=100)     #DEFO LATER PROBLEM
    colour_selector.grid(row=0, column=0, columnspan=2, sticky="news")

    # Length of the Wallpaper
    length_label = Label(options, text="Length (M):")
    length_label.grid(row=1, column=0, pady="3", sticky="news")

    length_entry = Entry(options, width=10, bg="#484848", name="length")
    length_entry.grid(row=1, column=1, pady="3", sticky="news")

    # Quality of the Wallpaper
    quality_label = Label(options, text="Paper:")
    quality_label.grid(row=2, column=0, pady="3", sticky="news")

    quality_combo = ttk.Combobox(options, values=["Standard Paper","Expensive Paper"], state="readonly", name="quality")
    quality_combo.grid(row=2, column=1, pady="3", sticky="news")

    # Extras for the Wallpaper
    extras_label = Label(options, text="Extras:")
    extras_label.grid(row=3, column=0, pady="3", sticky="news")

    extras_combo = ttk.Combobox(options, values=["Foil", "Glitter", "Embossing"], state="readonly", name="extras")
    extras_combo.grid(row=3, column=1, pady="3", sticky="news")

    # Lining for the Wallpaper
    lining_lable = Label(options, text="Lining required?")
    lining_lable.grid(row=4, column=0, pady="3", sticky="n")

    lining_tick = ttk.Checkbutton(options, name="lining")
    lining_tick.grid(row=4, column=1, pady="3")

    # Paste for the Wallpaper
    paste_label = Label(options, text="Paste required?")
    paste_label.grid(row=5, column=0, pady="3", sticky="n")

    paste_tick = ttk.Checkbutton(options, name="paste")
    paste_tick.grid(row=5, column=1, pady="3")

    # Add to Checkout Button
    add_to_checkout_button = Button(options, text="Checkout", height=2, width=5, name="add_to_checkout_button")
    add_to_checkout_button.grid(row=6, column=1, pady="3", sticky="ne")
    add_to_checkout_button.bind('<Button-3>')
    add_to_checkout_button.bind("<Button-1>", add_to_checkout_button_clicked)

def colour_selector(location):
    pass


def pattern1_clicked(event):
    print(event.widget._name + " clicked")
    pattern1_selected()

def pattern2_clicked(event):
    print(event.widget._name + " clicked")
    pattern2_selected()

def checkout_button_clicked(event):
    print(event.widget._name + " clicked")
    checkout_selected()

def menu_button_clicked(event):
    print(event.widget._name + " clicked")

def add_to_checkout_button_clicked(event):
    print(event.widget._name + " clicked")


def Homepage():
    Header()
    Pattern1(location=main_window)
    Pattern2(location=main_window)
    #Homepage_Prices()

Homepage()
main_window.mainloop()