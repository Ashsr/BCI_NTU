from Tkinter import Label,Button,Tk,X
def alpha_callback():import alpha
def SMR_callback():import SMR
def theta_callback():import theta
def gamma_callback():import gamma
top = Tk()
l=Label(top,text = "Neurofeedback",bg="lavender")
l.pack()
l1=Label(top,text = "Please select the required protocol you \n wish to train for:",bg="lavender")
l1.pack()
b1=Button(top,text="Theta",command=theta_callback,bg="lavender")
b1.pack(fill=X)
b2=Button(top,text="Alpha",command=alpha_callback,bg="lavender")
b2.pack(fill=X)
b3=Button(top,text="SMR",command=SMR_callback,bg="lavender")
b3.pack(fill=X)
b4=Button(top,text="Gamma",command=gamma_callback,bg="lavender")
b4.pack(fill=X)
top.maxsize(1000,500)
top.configure(bg="lavender")

top.mainloop()
