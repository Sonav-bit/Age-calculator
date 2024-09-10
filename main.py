from tkinter import*
root=Tk()
root.title('Age calculator app')
root.geometry('400x400')

l1=Label(root,int(input('Enter the Current year')))
l2=Label(root,int(input('Enter your Birth year: ')))

e1=Entry(root)
e2=Entry(root)

def greet():
    DOB=e1.get()
    Current=e2.get()
    message="Hey your Current age is"+(Current-DOB)+'Congrats'
    l4=Label(root,text=message)
    l4.grid(row=4,column=2)
b1=Button(root,text='Display',command=greet)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1.grid(row=3,column=2)
root.mainloop()