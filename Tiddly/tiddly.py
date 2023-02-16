from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk, Image
from datetime import datetime
from tkcalendar import Calendar
from tkinter import ttk

#------------------------ WRITE USERNAME PAGE -------------------------------------------
def start():
    global menu_img
    menu_img = ImageTk.PhotoImage(file="static/username_menu.png")
    menu_background_label = Label(main_frame, bg="white", image=menu_img)
    menu_background_label.pack()
    menu_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    start_button.destroy()
    
    #---------- entry bar ------------#
    global name_entry_button
    name_entry_button = Entry(main_frame, font=(
        "Helvetica", 30,), width=50, borderwidth=4)
    name_entry_button.place(x=100, y=300)

    #---------- Submit Name ------------#
    global submit_img
    global submit_button
    submit_img = PhotoImage(file="static\submit_button.png")
    submit_button = Button(main_frame, image=submit_img, font=("Helvetica"), background= "white", highlightbackground="white", command=save_username)
    submit_button.place(relx=0.50, rely=0.58, anchor=CENTER)

def save_username():
    global user_name_info
    # LINE BELOW IS THE VARIABLE THAT HAS THE USERNAME STORED
    user_name_info = name_entry_button.get()
    user_dashboard()

#----------------------------------------------------------------------------------------------------------------

def start_timer():
    global time_left
    time_left = int(time_entry.get()) * 60  # convert minutes to seconds
    update_timer()

def pause_timer():
    main_menu.after_cancel(after_id)  # cancel the scheduled function

def reset_timer():
    global time_left
    time_left = 0
    timer_label.config(text="Enter time in minutes:")
    pause_timer()

def update_timer():
    global time_left
    if time_left > 0:
        hours = time_left // 3600
        minutes = (time_left // 60) % 60
        seconds = time_left % 60
        timer_label.config(text=f"Time left: {hours:02d}:{minutes:02d}:{seconds:02d}")
        time_left -= 1
        global after_id
        after_id = main_menu.after(1000, update_timer)  # schedule the function to run after 1 second (1000 ms)
    else:
        timer_label.config(text="Time's up!")

def user_dashboard ():

    name_entry_button.destroy()
    submit_button.destroy()
    main_frame.destroy()

    style = ttk.Style(main_menu)
    style.theme_use('alt')

    today = datetime.today()
    cal = Calendar(main_menu, selectmode='day', year=today.year, month=today.month, day=today.day,background="black", disabledbackground="gray", bordercolor="gray", 
                headersbackground="white", normalbackground="white", foreground='white', 
                normalforeground='black', headersforeground='gray')
    cal.config(background = '#FBAA19')
    cal.place(relx=0.5, rely=0.37, anchor=CENTER)

    global calendar_img
    calendar_img = PhotoImage(file="static/calendar_label.png")
    dash_title = Label(main_menu, image=calendar_img, background= "white")
    dash_title.place(relx=0.5, rely=0.2, anchor=CENTER)


    global dash_img
    dash_img = PhotoImage(file="static/productivity_dashboard_title.png")
    dash_title = Label(main_menu, image=dash_img, background= "white")
    dash_title.place(relx=0.01, rely=0.02, anchor=NW)

    global to_do_img
    to_do_img = PhotoImage(file="static/to_do_button.png")
    label_title = Label(main_menu, image=to_do_img, background= "white")
    label_title.place(relx=0.15, rely=0.2, anchor=CENTER)

    global entry_task
    entry_task = Entry(main_menu, width=30,font=("Helvetica", 15,), borderwidth=2)
    entry_task.place(relx=0.16, rely=0.27, anchor=CENTER)

    global add_img
    add_img = PhotoImage(file="static\dd_btn.png")
    button_add_task = Button(main_menu, image=add_img, command=add_task)
    button_add_task.place(relx=0.09, rely=0.34, anchor=CENTER)

    global del_img
    del_img = PhotoImage(file="static\del_btn.png")
    button_delete_task = Button(main_menu, image=del_img, command=delete_task)
    button_delete_task.place(relx=0.23, rely=0.34, anchor=CENTER)

    global listbox_tasks
    listbox_tasks = Listbox(main_menu, width=37, font=25)
    listbox_tasks.place(relx=0.16, rely=0.52, anchor=CENTER)

    global timer_label_img
    timer_label_img = PhotoImage(file="static/timer_label.png")
    dash_title = Label(main_menu, image=timer_label_img, background= "white")
    dash_title.place(relx=0.75, rely=0.18, anchor=NW)

    global time_left, timer_label, time_entry
    time_left = 0  # time left in seconds
    timer_label = Label(main_menu, text="Enter time in minutes:", font=("Helvetica", 13), background="white")
    timer_label.place(relx=0.75, rely=0.24, anchor=NW)

    time_entry = Entry(main_menu, width=30,font=("Helvetica", 15,), borderwidth=2)
    time_entry.place(relx=0.68, rely=0.28, anchor=NW)

    
    global play_img
    play_img = PhotoImage(file="static\play_btn.png")
    start_button = Button(main_menu, image=play_img, command=start_timer)
    start_button.place(relx=0.68, rely=0.34, anchor=NW)

    global pause_img
    pause_img = PhotoImage(file="static\pause_btn.png")
    pause_button = Button(main_menu, image=pause_img, command=pause_timer)
    pause_button.place(relx=0.73, rely=0.34, anchor=NW)

    global reset_img
    reset_img = PhotoImage(file="static\start_over_btn.png")
    reset_button = Button(main_menu, image=reset_img, command=reset_timer)
    reset_button.place(relx=0.79, rely=0.34, anchor=NW)

    










tasks = []

# Define the function to add a task to the list
def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        entry_task.delete(0, END)
        update_listbox()

# Define the function to delete a task from the list
def delete_task():
    task = listbox_tasks.get(ACTIVE)
    if task in tasks:
        tasks.remove(task)
        update_listbox()

# Define the function to update the listbox with the current tasks
def update_listbox():
    listbox_tasks.delete(0, END)
    for task in tasks:
        listbox_tasks.insert(END, task)



main_menu = Tk()
main_menu.geometry("1280x720")
main_menu.title("Tiddly: Your Ultimate Productivity App")
main_menu["bg"] = "white"

#-------------------------------------------------------------------#

main_frame = Frame(main_menu, background="white", width=1280, height=720)
main_frame.pack()
main_frame.place(anchor="center", relx=0.5, rely=0.5)

global menu_img
menu_img = ImageTk.PhotoImage(file="static\main_menu.png")


menu_background_label = Label(main_frame, bg="white", image=menu_img)
menu_background_label.pack()
menu_background_label.place(x=0, y=0, relwidth=1, relheight=1)

strt_img = PhotoImage(file="static\start_btn.png")
start_button = Button(main_frame, image=strt_img, font=("Helvetica"), background= "white", highlightbackground="white", fg="black", command=start)
start_button.place(relx=0.55, rely=0.65, anchor=CENTER)
#-------------------------------------------------------------------#


main_menu.mainloop()