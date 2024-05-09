from tkinter import Tk, BOTH, Canvas, Button

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Calculator")
        self.__canvas = Canvas(self.__root, bg='black', width=width, height=height)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('Window Closed')

    def close(self):
        self.__running = False
    
    def add_button(self, text, command, x, y):
        btn = Button(self.__root, text=text, command=command)
        btn.place(x=x, y=y)


