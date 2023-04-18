from tkinter import *
from tkinter import ttk

main_window = Tk()                      # Creates main window
main_window.title("DIY Store")          # Renames the Page
main_window.geometry("1000x1000")
# main_window.geometry("775x500")         # Alters the Size
# main_window.configure(bg="white")    # Changes background FOR EDITING PURPOSES

# define a grid
main_window.columnconfigure(0, weight = 1)
main_window.columnconfigure(1, weight = 1)
main_window.rowconfigure(0, weight = 1)
main_window.rowconfigure(1, weight = 1)

def Homepage():
    header = Frame(main_window, height=750, width=100, padx=150, bg="green")
    header.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="se")

    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=10)
    main_window.columnconfigure(2, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)

    menu = Button(main_window, text="Menu", height=2, width=5, name="menu_button", bg="yellow")
    menu.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
    menu.bind('<Button-3>')

    title = Label(main_window, text="Welcome to the DIY Store!", padx=50, pady=0, name="diy_store", bg="yellow")
    title.grid(row=0, column=1, rowspan=1, padx=0, pady=10, sticky="n")

    checkout = Button(main_window, text="Checkout", height=2, width=5, name="checkout_button", bg="yellow")
    checkout.grid(row=0, column=2, padx=20, pady=10, sticky="ne")
    checkout.bind('<Button-3>')


def createPattern1():
    pattern1 = Canvas(main_window, name="pattern1", height=200, width=200)
    pattern1.grid(row=1, column=0, pady=75, padx=75)

    # pattern1.create_rectangle(0, 0, 200, 200, fill="white", outline="white") # background for pattern 1
    # for x in range(0, 4): #looping across
    #     x *= 50
    #     for i in range(0, 10): #looping down
    #         i *= 20
    #         pattern1.create_polygon(2 + x, 24 + i, 12 + x, 4 + i, 42 + x, 4 + i, 52 + x, 24 + i, fill='#7B48DD', outline='black', width=2)

    pattern1.bind("<Button-1>", pattern2_clicked)
def createPattern2():
    pattern2 = Canvas(main_window, name="pattern2", height=200, width=200)
    pattern2.grid(row=1, column=1, pady=75, padx=75)

    # pattern2.create_rectangle(0, 0, 200, 200, fill="white", outline="white")
    # xlocations = [2, 14, 22, 30, 42, 34, 42, 30, 22, 14, 2, 10]
    # ylocations = [25, 25, 0, 25, 25, 50, 75, 75, 100, 75, 75, 50]

    # for x in range(0, 5):
    #     x *= 40
    #     for i in range(0, 2):
    #         i *= 100
    #         pattern2.create_polygon(2 + x, 25 + i, 14 + x, 25 + i, 22 + x, 0 + i, 30 + x, 25 + i, 42 + x, 25 + i, 34 + x, 50 + i, 42 + x, 75 + i, 30 + x, 75 + i, 22 + x, 100 + i, 14 + x, 75 + i, 2 + x, 75 + i, 10 + x, 50 + i, fill='#7B48DD')
    #
    # pattern2.bind("<Button-1>", pattern2_clicked)

def pattern2_clicked(event):
    print(event.widget._name + " clicked")
def pattern2_clicked(event):
    print(event.widget._name + " clicked")

createPattern1()
createPattern2()

Homepage()
main_window.mainloop()