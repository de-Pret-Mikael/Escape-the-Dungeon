import tkinter
from PIL import ImageGrab, ImageTk


class App(tkinter.Tk):
    def __init__(self, title, minSize=None, maxSize=None, laby=None, hero=None):
        tkinter.Tk.__init__(self)
        self.title(title)
        self.laby = laby
        self.hero = hero
        if minSize != None:
            pipe = {"width": minSize[0], "height": minSize[1]}
            self.minsize(**pipe)
        if maxSize != None:
            pipe = {"width": maxSize[0], "height": maxSize[1]}
            self.maxsize(**pipe)

    def build_can(self, height=None, width=None, bg=None):
        self.can = tkinter.Canvas(self, height=height, width=width, background=bg)

    def pack_can(self):
        self.can.pack()

    def draw_img(self, x, y, anchor, img):
        self.can.create_image(x, y, anchor=anchor, image=img)

    def update_can(self, anchor):
        self.can.create_image(2, 2, anchor=anchor, image=self.dungeon)
        self.can.pack()
        self.can.update()

    def save_can(self, img):
        self.dungeon = img

    def place_can(self, x=None, y=None, relx=None, rely=None, anchor=None):
        self.can.place(x=x, y=y, relx=relx, rely=rely, anchor=anchor)

    def launch(self):
        self.mainloop()

    def add_bind(self, sequence, fct):
        self.bind(sequence=sequence, func=fct)


if __name__ == "__main__":
    myapp = App("test")
    myapp.build_can(height=50, width=50, bg="black")
    myapp.pack_can()
    print(myapp.can.__dict__)
    myapp.mainloop()
