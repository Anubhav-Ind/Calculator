# Calculator

from tkinter import *
import math
import os

root = Tk()
root_width = "548"
root_height = "634"
root.geometry(f"{root_width}x{root_height}")
root.resizable(height=False, width=False)
root.title("Calculator")
root.wm_iconbitmap("Icons\\Calculator.ico")


def mode():
    global digit_key_color
    global frame_color
    global digit_fg_color
    global background_color
    global mode_off
    global operator_key_color
    global operator_fg_color
    global outputbar_color
    global outputbar_fgcolor
    if mode_off == "Dark":
        digit_key_color = "black"
        frame_color = "black"
        digit_fg_color = "white"
        background_color = "black"
        mode_off = "Light"
        operator_key_color = "lightblue"
        operator_fg_color = "black"
        outputbar_fgcolor = "white"
        outputbar_color = "grey"
    elif mode_off == "Light":
        digit_key_color = "lightyellow"
        frame_color = "lightgrey"
        digit_fg_color = "black"
        background_color = "lightgrey"
        mode_off = "Dark"
        operator_key_color = "orange"
        operator_fg_color = "black"
        outputbar_color = "lightyellow"
        outputbar_fgcolor = "black"
    root.configure(bg=f"{background_color}")
    outputbar.config(bg=f"{outputbar_color}", fg=f"{outputbar_fgcolor}")
    key_mode.config(text=f"{mode_off}Mode", bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_1.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_2.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_3.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_4.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_5.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_6.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_7.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_8.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_9.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_0.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_00.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_dot.config(bg=f"{digit_key_color}", fg=f"{digit_fg_color}")
    key_plus.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_minus.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_mult.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_div.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_rem.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_eq.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_x.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_tut.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_C.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_open.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_close.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_sqrt.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_fact.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_sin.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_cos.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_log.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    key_pi.config(bg=f"{operator_key_color}", fg=f"{operator_fg_color}")
    digitframe.configure(background=f"{frame_color}")
    operator_row.configure(background=f"{frame_color}")
    row1.configure(background=f"{frame_color}")
    row2.configure(background=f"{frame_color}")
    row3.configure(background=f"{frame_color}")
    row4.configure(background=f"{frame_color}")
    math_row.configure(background=f"{frame_color}")


def pop(event):
    global output_var
    try:
        x = output_var.get()
        k = len(x)
        output_var.set(f"{x[:(k - 1)]}")
    except:
        pass


def click(event):
    global output_var
    text = event.widget.cget('text')
    output_var.set(f"{output_var.get() + text}")


def res(event):
    global output_var
    try:
        output = eval(output_var.get())
        output_var.set(f"{output}")
    except:
        output_var.set("Error")
        outputbar.update()


def clear(event):
    global output_var
    output_var.set("")


def tut(event):
    tutpath = "Tutorial\\Tutorial.pyw"
    os.startfile(tutpath)

digit_key_color = "lightyellow"
frame_color = "lightgrey"
digit_fg_color = "black"
background_color = "lightgrey"
mode_off = "Dark"
operator_key_color = "orange"
operator_fg_color = "black"
outputbar_color = "lightyellow"
outputbar_fgcolor = "black"

output_var = StringVar()
output_var.set("")
outputbar = Entry(root, font="comicsans 25 bold", justify=RIGHT,
                  borderwidth=2, bg=f"{outputbar_color}", textvariable=output_var, bd=5, fg=f"{outputbar_fgcolor}")
outputbar.bind('<Return>', res)
outputbar.bind('<Escape>', clear)
outputbar.focus()
outputbar.pack(side=TOP, fill=X, ipadx=10, ipady=10)

digitframe = Frame(root, borderwidth=2, bg=f"{frame_color}")

math_row = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_sin = Button(math_row, text="math.sin()", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                  relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_sin.pack(side=LEFT, padx=5, pady=5)
key_sin.bind("<Button>", click)
key_cos = Button(math_row, text="math.cos()", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                   relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_cos.pack(side=LEFT, padx=5, pady=5)
key_cos.bind("<Button>", click)
e=math.e
key_log = Button(math_row, text="math.log(,e)", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                  relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_log.pack(side=LEFT, padx=5, pady=5)
key_log.bind("<Button>", click)
key_pi = Button(math_row, text="math.pi", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                 relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_pi.pack(side=LEFT, padx=5, pady=5)
key_pi.bind("<Button>", click)
key_fact = Button(math_row, text="math.factorial()", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                 relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_fact.pack(side=LEFT, padx=5, pady=5)
key_fact.bind("<Button>", click)


math_row.pack(side=TOP)



operator_row = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_plus = Button(operator_row, text="+", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                  relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_plus.pack(side=LEFT, padx=5, pady=5)
key_plus.bind("<Button>", click)
key_minus = Button(operator_row, text="-", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                   relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_minus.pack(side=LEFT, padx=5, pady=5)
key_minus.bind("<Button>", click)
key_mult = Button(operator_row, text="*", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                  relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_mult.pack(side=LEFT, padx=5, pady=5)
key_mult.bind("<Button>", click)
key_div = Button(operator_row, text="/", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                 relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_div.pack(side=LEFT, padx=5, pady=5)
key_div.bind("<Button>", click)
key_rem = Button(operator_row, text="%", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                 relief=SUNKEN, height=4, width=12, font="lucida 9 bold")
key_rem.pack(side=LEFT, padx=5, pady=5)
key_rem.bind("<Button>", click)

operator_row.pack(side=TOP)


row1 = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_9 = Button(row1, text="9", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_9.bind("<Button>", click)
key_9.pack(side=LEFT, padx=5, pady=5)
key_8 = Button(row1, text="8", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_8.pack(side=LEFT, padx=5, pady=5)
key_8.bind("<Button>", click)
key_7 = Button(row1, text="7", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_7.pack(side=LEFT, padx=5, pady=5)
key_7.bind("<Button>", click)
key_sqrt = Button(row1, text="math.sqrt()", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN,
               height=4, width=12, font="lucida 9 bold")
key_sqrt.pack(side=LEFT, padx=5, pady=5)
key_sqrt.bind('<Button>', click)
key_x = Button(row1, text="(——", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN,
               height=4, width=12, font="lucida 9 bold")
key_x.pack(side=LEFT, padx=5, pady=5)
key_x.bind('<Button>', pop)
row1.pack(side=TOP)
row2 = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_6 = Button(row2, text="6", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_6.pack(side=LEFT, padx=5, pady=5)
key_6.bind("<Button>", click)
key_5 = Button(row2, text="5", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_5.pack(side=LEFT, padx=5, pady=5)
key_5.bind("<Button>", click)
key_4 = Button(row2, text="4", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_4.pack(side=LEFT, padx=5, pady=5)
key_4.bind("<Button>", click)
key_open = Button(row2, text="(", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_open.pack(side=LEFT, padx=5, pady=5)
key_open.bind("<Button>", click)
key_close = Button(row2, text=")", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_close.pack(side=LEFT, padx=5, pady=5)
key_close.bind("<Button>", click)
row2.pack(side=TOP)

row3 = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_3 = Button(row3, text="3", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_3.pack(side=LEFT, padx=5, pady=5)
key_3.bind("<Button>", click)
key_2 = Button(row3, text="2", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_2.pack(side=LEFT, padx=5, pady=5)
key_2.bind("<Button>", click)
key_1 = Button(row3, text="1", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_1.pack(side=LEFT, padx=5, pady=5)
key_1.bind("<Button>", click)
key_C = Button(row3, text="CE", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN,
               height=4, width=12, font="lucida 9 bold")
key_C.pack(side=LEFT, padx=5, pady=5)
key_C.bind('<Button>', clear)
key_eq = Button(row3, text="=", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN,
                height=4, width=12, font="lucida 9 bold")
key_eq.bind('<Button>', res)
key_eq.pack(side=LEFT, padx=5, pady=5)

row3.pack(side=TOP)

row4 = Frame(digitframe, borderwidth=2, bg=f"{frame_color}")
key_00 = Button(row4, text="00", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN,
                height=4, width=12, font="lucida 9 bold")
key_00.pack(side=LEFT, padx=5, pady=5)
key_00.bind("<Button>", click)
key_0 = Button(row4, text="0", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_0.pack(side=LEFT, padx=5, pady=5)
key_0.bind("<Button>", click)
key_dot = Button(row4, text=".", borderwidth=2, bg=f"{digit_key_color}", fg=f"{digit_fg_color}", relief=SUNKEN,
                 height=4, width=12, font="lucida 9 bold")
key_dot.pack(side=LEFT, padx=5, pady=5)
key_dot.bind("<Button>", click)
key_tut = Button(row4, text="Tutorial", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}", relief=SUNKEN, height=4,
               width=12, font="lucida 9 bold")
key_tut.pack(side=LEFT, padx=5, pady=5)
key_tut.bind("<Button>", tut)
key_mode = Button(row4, text=f"{mode_off}Mode", borderwidth=2, bg=f"{operator_key_color}", fg=f"{operator_fg_color}",
                  relief=SUNKEN, height=4, width=12,
                  font="lucida 9 bold", command=mode)

key_mode.pack(side=LEFT, padx=5, pady=5)
root.update()
row4.pack(side=TOP)

digitframe.pack(pady=25, side="left", fill="y", padx=10)
root.configure(background=f"{background_color}")
root.mainloop()
