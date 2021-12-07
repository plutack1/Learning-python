import tkinter
window = tkinter.Tk()
window.title('my first GUI program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="NAME", font=('arial', 24, 'bold'))
my_label.pack()


window.mainloop()