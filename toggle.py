import tkinter as tk
from pynput.mouse import Button, Controller
import time

mouse = Controller()


# --- functions ---

def move(steps=10, distance=0.1):
    if steps > 0:
        # get current position
        relx = float(frame.place_info()['relx'])

        # set new position
        frame.place_configure(relx=relx + distance)

        # repeate it after 10ms
        root.after(10, move, steps - 1, distance)


def toggle(event):
    if button["text"] == "turn on":
        move(25, 0.02)  # 50*0.02 = 1
        button["text"] = "turn off"
        print("Clicked on turn on")
        time.sleep(3)
        while button["text"] == "turn off":
            mouse.click(Button.left, 1)

        else:
            print("stopped")
            toggle(event)

    elif button["text"] == "turn off":
        move(25, -0.02)
        button["text"] = "turn on"
        print("Clicked on off")


# --- main ---

root = tk.Tk()

frame = tk.Frame(root, background='red')
frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

# to center label and button
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(3, weight=1)

button = tk.Button(frame, text='turn on', width=5, height=1)
button.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.1)
button.bind("<Button-1>", toggle)

root.mainloop()
