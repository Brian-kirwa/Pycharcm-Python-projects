from tkinter import *
def submit():
    food=[]
    for index in listbox.curselection():
        food.append(listbox.get(index))

    print("You selected the following:")

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())



window = Tk()


listbox=Listbox(window,width=12,font=("Consolas",20),fg="black",bg="blue",selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Humberger")
listbox.insert(3,"garlic Bread")
listbox.insert(4,"Soup")
listbox.insert(5,"Garlic")

listbox.config(height=listbox.size())

entry=Entry(window,font=("Consolas",20),fg="black",bg="blue")
entry.pack()

submit=Button(window,text="Submit",fg="black",bg="red",command=submit)
submit.pack()

add=Button(window,text="Add",fg="black",bg="red",command=add)
add.pack()

delete=Button(window,text="Delete",fg="black",bg="red",command=delete)
delete.pack()


window.mainloop()