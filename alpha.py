from Tkinter import Label,Button,Tk,X
def alphatrain_callback():import alpha_train
def alphatest_callback():import alpha_test
top = Tk()
l=Label(top,text = "Welcome to \n Alpha Protocol",bg="lavender")
l.pack()
l1=Label(top,text = "Please select if you wish to train or test",bg="lavender")
l1.pack()
b1=Button(top,text="Training",command=alphatrain_callback,bg="lavender")
b1.pack(fill=X)
b2=Button(top,text="Testing",command=alphatest_callback,bg="lavender")
b2.pack(fill=X)
top.maxsize(1600,1420)
top.configure(bg="lavender")

top.mainloop()
