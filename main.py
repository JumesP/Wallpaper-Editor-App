'''
    Wallpaper Editor Prototype
'''
import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import ttk


class Wallpaper:
    def __init__(self, pattern, colour, length, extras, quality, lining, paste, price):
        self.pattern = pattern
        self.colour = colour
        self.length = length
        self.extra = extras
        self.quality = quality
        self.lining = lining
        self.paste = paste
        self.price = price


# Initialising Window
main_window = Tk()
main_window.title("DIY Store")
main_window.geometry("750x500")

# Formatting Homepage Grid
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=2)
main_window.rowconfigure(2, weight=1)

# Creating Initial Variables
colours = ["purple", "darkSlateGray4", "deepSkyBlue", "lightSeaGreen", "violetRed2", "gold"]
order = {}
order_reference_num = 0

# =========  THE HOMEPAGE  =========

def header(location):
    header = Frame(location, height=66, width=5, bg="#484848")
    header.grid(row=0, column=0, columnspan=2, sticky="nwe")

    header.columnconfigure(0, weight=1)
    header.columnconfigure(1, weight=2)
    header.columnconfigure(2, weight=1)

    menu_button = Button(header, text="Menu", height=2, width=5, name="menu_button")
    menu_button.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
    menu_button.bind("<Button-1>", homepage_clicked)

    title = Label(header, text="Welcome to the DIY Store!", padx=50, pady=0, name="diy_store", bg="#484848")
    title.grid(row=0, column=1, padx=100, pady=10, sticky="ew")

    checkout_button = Button(header, text="Checkout", height=2, width=5, name="checkout_button")
    checkout_button.grid(row=0, column=2, padx=20, pady=10, sticky="ne")

    if location == main_window: # Binding Function Exclusively to the Homepage
        checkout_button.bind("<Button-1>", homepage_clicked)


def footer(location):
    footer = Frame(location, height=66, width=5, bg="#484848")
    footer.grid(row=4, column=0, columnspan=2, sticky="nwe")

    footer.columnconfigure(0, weight=1)
    footer.columnconfigure(1, weight=1)
    footer.columnconfigure(2, weight=2)
    footer.columnconfigure(3, weight=1)
    footer.columnconfigure(4, weight=1)

    back_button = Button(footer, text="Back", height=2, width=12, name="back_button", command=location.destroy)
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    clear_checkout_button = Button(footer, text="Clear Checkout", height=2, width=10, name="clear_checkout_button")
    clear_checkout_button.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
    clear_checkout_button.bind("<Button-1>", homepage_clicked)

    title = Label(footer, text="Thank you for Shopping at the DIY Store!", name="diy_store", bg="#484848")
    title.grid(row=0, column=2, padx=50, pady=1, sticky="ew")

    close_program = Button(footer, text="Close Program", height=2, width=10, name="close_button")
    close_program.grid(row=0, column=3, padx=10, pady=10, sticky="ne")
    close_program.bind("<Button-1>", homepage_clicked)

    export_to_txt = Button(footer, text="Export To Text File", height=2, width=12, name="export_button")
    export_to_txt.grid(row=0, column=4, padx=10, pady=10, sticky="ne")
    export_to_txt.bind("<Button-1>", homepage_clicked)


def create_pattern_1(pattern1): # Creating Pattern 1
    for x in range(0, 4):
        x *= 50
        for y in range(0, 10):
            y *= 20
            pattern1.create_polygon(2 + x, 24 + y, 12 + x, 4 + y, 42 + x, 4 + y, 52 + x, 24 + y,
                                    fill=edit.colour, outline='black', width=2)


def place_pattern_1(location):
    global pattern1
    pattern1 = Canvas(location, name="pattern1", height=200, width=200, bg="white")
    pattern1.grid(row=1, column=0, pady=50, padx=50)

    create_pattern_1(pattern1)
    homepage_description(location, 0)

    if location == main_window:
        pattern1.bind("<Button-1>", homepage_clicked)


def create_pattern_2(pattern2): # Creating Pattern 2
    pattern2_xLocations = [14, 2, 10, 2, 14, 22, 30, 42, 34, 42, 30, 22]
    pattern2_yLocations = [80, 80, 60, 40, 40, 20, 40, 40, 60, 80, 80, 100]

    for shapes in range(0, 10):
        pattern2_Locations = []
        if shapes > 4:
            shapes = shapes - 5
            y = 80
        else:
            y = 0
        x = shapes * 40

        for digit in range(0, 12):  # creating the shape
            pattern2_Locations.append(pattern2_xLocations[digit] + x)
            pattern2_Locations.append(pattern2_yLocations[digit] + y)
            pattern2.create_polygon(pattern2_Locations, fill=edit.colour, outline="black", width=0)

def place_pattern_2(location):
    global pattern2
    pattern2 = Canvas(location, name="pattern2", height=200, width=200, bg="white")
    pattern2.grid(row=1, column=1, pady=50, padx=50)

    create_pattern_2(pattern2)
    homepage_description(location, 1)
    if location == main_window:
        pattern2.bind("<Button-1>", homepage_clicked)    # only binds to function if on homepage


def homepage_description(location, row):  # Homepage display
    homepage_display = Label(location,
                             text="From £156.78 per 10.05m \n Avaliable in all colours \n Click Wallpaper to View",
                             height=4, width=1, bg="#484848")
    homepage_display.grid(row=2, column=row, sticky="news", padx=10, pady=10)


# =========  OUTSIDE THE HOMEPAGE  =========

def pattern_1_selected():   # Pattern 2 Customisation Page
    global pattern1_page
    pattern1_page = Toplevel()
    pattern1_page.title("Pattern One")
    pattern1_page.geometry("680x360")

    edit.pattern = "pattern1"
    edit.colour = colours[0]

    pattern1 = Canvas(pattern1_page, name="pattern1", height=200, width=200, bg="white")
    pattern1.grid(row=0, column=0, pady=50, padx=50)

    place_pattern_1(location=pattern1_page)
    options(location=pattern1_page)

def pattern_2_selected():  # Pattern 2 Customisation Page
    global pattern2_page
    pattern2_page = Toplevel()
    pattern2_page.title("Pattern Two")
    pattern2_page.geometry("680x360")

    edit.pattern = "pattern2"
    edit.colour = colours[0]

    pattern2 = Canvas(pattern2_page, name="pattern2", height=200, width=200, bg="white")
    pattern2.grid(row=1, column=0, pady=50, padx=50)

    place_pattern_2(location=pattern2_page)
    options(location=pattern2_page)


def checkout_selected():  # Creating The Checkout Page
    global checkout_page
    checkout_page = Toplevel()
    checkout_page.title("Checkout")
    checkout_page.geometry("1000x800")

    checkout_page.columnconfigure(0, weight=1)
    checkout_page.rowconfigure(0, weight=0)
    checkout_page.rowconfigure(1, weight=3)
    checkout_page.rowconfigure(2, weight=1)

    header(location=checkout_page)
    checkout_display(location=checkout_page)
    footer(location=checkout_page)
    export_wallpapers()


def checkout_display(location):
    # Display orders, header titles and all details
    checkout_display = Canvas(location)
    checkout_display.grid(row=1, column=0, sticky="news")

    checkout_headers = "Order ID", "Pattern", "Colour", "Length(M)", "Extras", "Quality", "Lining", "Paste", "Price(£)"

    checkout_table = tkinter.ttk.Treeview(checkout_display, columns=checkout_headers, show="headings", height=10)

    for headers in checkout_headers:
        checkout_table.column(headers, anchor=CENTER, stretch=YES, width=100)
        checkout_table.heading(headers, text=headers)

    checkout_table.pack(fill="both", expand=True)
    for orderid in order:   # presentation within the treetable!
        orderx = []
        orderx.append(orderid)
        for order_spec in order[orderid]:
            orderx.append(order_spec)

        checkout_table.insert(parent="", index=tkinter.END, values=orderx)

    order_total = 0
    for orderid in order:
        order_total += order[orderid][7]

    checkout_total = Label(checkout_display, text=f"Your total today is: £{order_total}")
    checkout_total.pack(side=BOTTOM)


def menu_selected():  # Creating The Menu Page
    menu_page = Toplevel()
    menu_page.title("Menu")

    menu = Label(menu_page, text="Thank you for using our software\nCreated By 2210425", bg="#484848", padx=10, pady=10)
    menu.pack()


def options(location):
    global lining, paste, price_label, options_panel, add_to_checkout_button
    lining = IntVar()
    paste = IntVar()

    options_panel = Frame(location, width=100, name="options_panel")
    options_panel.grid(row=1, column=2, pady=20, padx=50)

    options_panel.columnconfigure(0, weight=1)
    options_panel.columnconfigure(1, weight=1)
    options_panel.rowconfigure(0, weight=1)
    options_panel.rowconfigure(1, weight=2)

    colour_selector(options_panel)

    # Length of the Wallpaper
    length_label = Label(options_panel, text="Length (M):")
    length_label.grid(row=1, column=0, pady=3, sticky="news")

    length_entry = Entry(options_panel, width=10, bg="#484848", name="length")
    length_entry.grid(row=1, column=1, pady=3, sticky="news")
    length_entry.bind("<KeyRelease>", wallpaper_editor)

    # Quality of the Wallpaper
    quality_label = Label(options_panel, text="Paper:")
    quality_label.grid(row=2, column=0, pady="3", sticky="news")

    quality_combo = ttk.Combobox(options_panel, values=["Standard Paper", "Expensive Paper"],
                                 state="readonly", name="quality")
    quality_combo.grid(row=2, column=1, pady=3, sticky="news")
    quality_combo.bind("<<ComboboxSelected>>", wallpaper_editor)

    # Extras for the Wallpaper
    extras_label = Label(options_panel, text="Extras:")
    extras_label.grid(row=3, column=0, pady=3, sticky="news")

    extras_combo = ttk.Combobox(options_panel, values=["None", "Foil", "Glitter", "Embossing"],
                                state="readonly", name="extras")
    extras_combo.grid(row=3, column=1, pady=3, sticky="news")
    extras_combo.bind("<<ComboboxSelected>>", wallpaper_editor)

    # Lining for the Wallpaper
    lining_label = Label(options_panel, text="Lining required?")
    lining_label.grid(row=4, column=0, pady=3, sticky="n")

    lining_tick = ttk.Checkbutton(options_panel, name="lining", variable=lining)
    lining_tick.grid(row=4, column=1, pady=3)
    lining_tick.bind("<Button>", wallpaper_editor)

    # Paste for the Wallpaper
    paste_label = Label(options_panel, text="Paste required?")
    paste_label.grid(row=5, column=0, pady=3, sticky="n")

    paste_tick = ttk.Checkbutton(options_panel, name="paste", variable=paste)
    paste_tick.grid(row=5, column=1, pady=3)
    paste_tick.bind("<Button>", wallpaper_editor)

    # Add to Checkout Button
    add_to_checkout_button = Button(options_panel, text="Add to Checkout", height=2, width=10,
                                    name="add_to_checkout_button", command=location.destroy)
    add_to_checkout_button.grid(row=6, column=1, pady=3, sticky="n")
    add_to_checkout_button.bind("<Button-1>", homepage_clicked)

    price()


def price():
    len = round(((edit.length // 10.05) * 10.05) + 10.05, 2)    # Rounding up the size to per roll
    total_rolls = round(len / 10.05)

    lining_len = round(((edit.length // 20) * 20) + 20, 2)
    lining_rolls = round(lining_len / 20, 2)

    edit.price = round((52 * (len * 100)) * 0.003, 2)

    if edit.quality == "Expensive":
        edit.price *= 2

    if edit.extra == "Foil":
        edit.price += len*0.12
    elif edit.extra == "Glitter":
        edit.price += len*0.18
    elif edit.extra == "Embossing":
        edit.price += len*0.6

    if edit.lining:
        edit.price += lining_rolls * 7.63

    wp_and_lining_len = len + lining_len
    paste_tins_needed = round((len // 102) + 1, 2)
    lining_paste_tins_needed = round((lining_len // 102) + 1, 2)

    if edit.paste:
        edit.price += paste_tins_needed * 13.99
        if edit.lining:
            edit.price += lining_paste_tins_needed * 13.99

    edit.price = round(edit.price, 2)

    price_label = Label(options_panel, text=f"£{edit.price}", height=2, width=10, name="price", bg="#484848")
    price_label.grid(row=6, column=0, pady=3, sticky="n")


def colour_selector(options_panel):
    colour_selector = Frame(options_panel, bg="blue", width=100, height=100)
    colour_selector.grid(row=0, column=0, columnspan=2, sticky="news")

    for num_presented in range(len(colours)):
        colour_box = Canvas(colour_selector, width=100, height=50, name=colours[num_presented].lower())
        colour_box.create_rectangle(0, 0, 100, 50, outline="black", fill=colours[num_presented])
        if num_presented > 2:
            x, y = num_presented - 3, 1
        else:
            x, y = num_presented, 0
        colour_box.grid(row=y, column=x)
        colour_box.bind("<Button>", colour_selected)


def homepage_clicked(event):
    if event.widget._name == "pattern1":
        pattern_1_selected()

    elif event.widget._name == "pattern2":
        pattern_2_selected()

    elif event.widget._name == "checkout_button":
        checkout_selected()

    elif event.widget._name == "menu_button":
        menu_selected()

    elif event.widget._name == "add_to_checkout_button":
        store_edit()

    elif event.widget._name == "close_button":
        import sys; sys.exit()

    elif event.widget._name == "export_button":
        export_wallpapers()

    elif event.widget._name == "clear_checkout_button":
        order.clear()
        checkout_display(location=checkout_page)


def wallpaper_editor(event):
    if event.widget._name == "length":
        x = 0
        while x < 5:
            x += 1
            try:
                edit.length = float(event.widget.get())
                add_to_checkout_button["state"] = "active"
            except ValueError:
                add_to_checkout_button["state"] = "disabled"
            else:
                break
        price()

    elif event.widget._name == "quality":
        if event.widget.get() == "Standard Paper":
            edit.quality = "Standard"
        else:
            edit.quality = "Expensive"
        price()

    elif event.widget._name == "extras":
        edit.extra = event.widget.get()
        price()

    elif event.widget._name == "lining":
        if lining.get() == 0:
            edit.lining = True
        else:
            edit.lining = False
        price()

    elif event.widget._name == "paste":
        if paste.get() == 0:
            edit.paste = True
        else:
            edit.paste = False
        price()


def colour_selected(event):
    edit.colour = event.widget._name
    if edit.pattern == "pattern1":
        place_pattern_1(pattern1_page)
    else:
        place_pattern_2(pattern2_page)


def store_edit():
    global order_reference_num, order_id, order, edit
    order_id = "DIY00" + str(order_reference_num)
    order_reference_num += 1
    order[order_id] = edit.pattern, edit.colour, edit.length, edit.extra, edit.quality, edit.lining, edit.paste, edit.price
    edit = Wallpaper("pattern1", "purple", 1, "None", "Standard", False, False, 0)


def export_wallpapers():
    order_headers = ["Pattern", "Colour ", "Length(m)", "Extras ", "Quality", "Lining?", "Paste? ", "Price(£)"]
    file = open("customer_order", 'w')
    file.write("Users Custom Wallpaper Specifications: \n\n")

    for orderid in order:
        file.write("Order ID:\t" + orderid)

        for details in range(len(order_headers)):
            file.write("\n" + order_headers[details] + ":\t" + str(order[orderid][details]))

        file.write("\n\n")

    file.close()

def homepage():
    header(location=main_window)
    place_pattern_1(location=main_window)
    place_pattern_2(location=main_window)

edit = Wallpaper("pattern1", "purple", 1, "None", "Standard", False, False, 0)

homepage()
main_window.mainloop()
