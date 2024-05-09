from graphics import Window, Buttons
from tkinter import Tk, Button

def button_clicked():
    print('button clicked')


def main():
    screen_x = 800
    screen_y = 600

    # win = Tk()
    # win.geometry(f'{screen_x}x{screen_y}')
    win = Window(screen_x, screen_y)
    # btn = Button(win, text='click', command=win.destroy)
    # btn.place(x=100,y=20)

    win.add_button('click', button_clicked, 100, 20)

    # test = Buttons(50, 50, "hello", win, button_clicked)
    # test.place(x=50, y=50)

    # win.mainloop() 

    win.wait_for_close()

main()


