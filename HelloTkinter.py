from tkinter import *


class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        #Changing the name of the master widget
        self.master.title("GUI")

        #allowing the widget to take the full width of the root window
        self.pack(fill=BOTH, expand=1)

        #creating the button instance
        quitButton = Button(self,text="Quit",command=self.client_exit)

        #placing the button into the window
        quitButton.place(x=100, y=100)

    def client_exit(self):
        exit()

root = Tk()

#The size of the window
root.geometry("400x300")

app = Window(root)

root.mainloop()