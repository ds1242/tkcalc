from graphics import Window

def button_clicked():
    print('button clicked')


def main():
    screen_x = 800
    screen_y = 600

    win = Window(screen_x, screen_y)
    button_symbols = ['0', '1', '2', '3', '4', '5','6', '7','8', '9', '+','-', '*', '/','.']
    for symbol in button_symbols:
        
        win.add_button(symbol, button_clicked, 100, 30)
    # win.add_button('1', button_clicked, 100, 30)
    # win.add_button('2', button_clicked, 100, 70)

    # test = Buttons(50, 50, "hello", win, button_clicked)
    # test.place(x=50, y=50)

    # win.mainloop() 

    win.wait_for_close()

main()


