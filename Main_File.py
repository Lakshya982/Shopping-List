from tkinter import *
from tkinter import ttk

ws=Tk()
ws.title('Shopping List')
ws.geometry('500x500')

game_frame = Frame(ws)
game_frame.pack()

#Scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side = RIGHT, fill = Y)

game_scroll = Scrollbar(game_frame,orient = "horizontal")
game_scroll.pack(side = BOTTOM, fill = X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)

my_game.pack()

game_scroll.config(command = my_game.yview)
game_scroll.config(command= my_game.xview)

#Define column

my_game['columns']= ('Item', 'Amount','Where','Month')
my_game.column("#0", width=0,  stretch=NO)
my_game.column("Item",anchor=CENTER, width=80)
my_game.column("Amount",anchor=CENTER, width=80)
my_game.column("Where",anchor=CENTER, width=80)
my_game.column("Month",anchor=CENTER,width = 80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("Item",text="Item",anchor=CENTER)
my_game.heading("Amount",text="Amount",anchor=CENTER)
my_game.heading("Where",text="Where",anchor=CENTER)
my_game.heading("Month",text="Month",anchor=CENTER)

global count
count = 0

Input_frame = Frame(ws)
Input_frame.pack()

item = Label(Input_frame,text="Item")
item.grid(row=0,column=0)

amount = Label(Input_frame,text="Amount")
amount.grid(row=0,column=1)

where = Label(Input_frame,text="Where")
where.grid(row=0,column=2)

month = Label(Input_frame,text = "Month")
month.grid(row=0,column=3)

item_entry = Entry(Input_frame)
item_entry.grid(row=1,column=0)

amount_entry = Entry(Input_frame)
amount_entry.grid(row=1,column=1)

where_entry = Entry(Input_frame)
where_entry.grid(row=1,column=2)

month_entry = Entry(Input_frame)
month_entry.grid(row=1,column=3)

def input_record():
    

    global count
   
    my_game.insert(parent='',index='end',iid = count,text='',values = (item_entry.get(),amount_entry.get(),where_entry.get(),month_entry.get()))
    count += 1

   
    item_entry.delete(0,END)
    amount_entry.delete(0,END)
    where_entry.delete(0,END)
    month_entry.delete(0,END)

def select_record():
    item_entry.delete(0,END)
    amount_entry.delete(0,END)
    where_entry.delete(0,END)
    month_entry.delete(0,END)
    
    selected = my_game.focus()
    values = my_game.item(selected,'values')

    item_entry.insert(0,values[0])
    amount_entry.insert(0,values[1])
    where_entry.insert(0,values[2])
    month_entry.insert(0,values[3])

def update_record():
    selected = my_game.focus()
    my_game.item(selected, text = "", values = (item_entry.get(), amount_entry.get(), where_entry.get(),month_entry.get()))
    item_entry.delete(0,END)
    amount_entry.delete(0,END)
    where_entry.delete(0,END)
    month_entry.delete(0,END)
    
#button
Input_button = Button(ws,text = "Input Record",command= input_record)
Input_button.pack()

update_button = Button(ws, text = "Save Record", command = update_record)
update_button.pack(pady = 10)

select_button = Button(ws,text="Select Record", command=select_record)
select_button.pack(pady =10)

ws.mainloop()
