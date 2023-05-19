from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
import user as u

myw =Tk()
myw.title('ADN Game')
myw.geometry("800x600")

global is_count
is_count=True

global user_press
user_press=True

global login_check
login_check=False

class functions:
    def __init__(self):
        pass

    def open_snake(self):
        if login_check:
            self.snake= 'snake.py'
            os.system('"%s"' %self.snake)
        else:
            messagebox.showwarning('ADN LOGIN ERROR','Login to play!')

    def open_space(self):
        if login_check:
            self.space= 'INVADETHESPACE.py'
            os.system('"%s"' %self.space)
        else:
            messagebox.showwarning('ADN LOGIN ERROR','Login to play!')

    def open_number(self):
        if login_check:
            self.num= '2048.py'
            os.system('"%s"' %self.num)
        else:
            messagebox.showwarning('ADN LOGIN ERROR','Login to play!')
    
    def new_user(self):
        global user_press
        if user_press:
            global secondwindow
            secondwindow=Toplevel()
            secondwindow.title('ADN Login')
            secondwindow.geometry("600x600")
            global new_pic
            logo_lbl=Label(secondwindow,image=new_pic)
            logo_lbl.pack(pady=10)
            lb1=Label(secondwindow,text='Enter Username',font=("Helvectia",15))
            lb1.pack(pady=5)
            global e1
            e1=Entry(secondwindow)
            e1.pack(pady=5)
            lb2=Label(secondwindow,text='Enter Password',font=("Helvectia",15))
            lb2.pack(pady=5)
            global e2
            e2=Entry(secondwindow)
            e2.pack(pady=5)
            btn=Button(secondwindow,text='Login',command=f1.mycheck)
            btn.pack(pady=10)
            global lbl3
            lbl3=Label(secondwindow,text='')
            lbl3.pack(pady=20)

    def mycheck(self):
        global e1
        global e2
        global login_check
        if e1.get() in u.registered_users.keys() and e2.get() in u.registered_users.values():
            messagebox.showinfo('ADN LOGIN',f'Welcome user {e1.get()}, enjoy ypur game.Now you have successfully entered the ADN Game interface!')
            secondwindow.destroy()
            login_check=True

        else:
            messagebox.showwarning('ADN LOGIN ERROR','Either the password or the username you have entered is not correct, please try again!')
            login_check=False

    def show_tiles(self):
        global is_count
        if is_count:
            snake_temp.place_forget()
            num_temp.place_forget()
            space_temp.place_forget()
            is_count=False
        else:
            snake_temp.place(x=50,y=400)
            num_temp.place(x=300,y=400)
            space_temp.place(x=550,y=400)
            is_count=True

f1=functions()

#this class contains hovering functions
class hovering:
    def __init__(self):
        pass

    def button_hover(self,b):
        global login_check
        global e1
        global user_press
        if login_check:
            user_btn.config(image=new_user_hover,borderwidth=1)
            user_label.config(text='logged in successfully')
            user_press=False
        else:
            user_btn.config(image=new_user_hover,borderwidth=1)
            user_label.config(text='Not logged in')
    
    def button_leave(self,b):
        user_btn.config(image=new_user,borderwidth=0)
        user_label.config(text='')

    def button_enter(self,b):
        menu_btn.config(image=new_tiles_hover,borderwidth=1)
        
    def button_exit(self,b):
        menu_btn.config(image=new_tiles,borderwidth=0)

    def snake_hover(self,b):
        snake_temp.config(image=new_snake_hover,borderwidth=1)

    def snake_hover_exit(self,b):
        snake_temp.config(image=new_snake,borderwidth=0)

    def num_hover(Self,b):
        num_temp.config(image=new_num_hover,borderwidth=1)

    def num_hover_exit(self,b):
        num_temp.config(image=new_num,borderwidth=0)

    def space_hover(self,b):
        space_temp.config(image=new_space_hover,borderwidth=1)
    
    def space_hover_exit(self,b):
        space_temp.config(image=new_space,borderwidth=0)

f2= hovering()

#images
logo=Image.open("Images/logo.png")
user=Image.open("Images/newuser.png")
user_hover=Image.open("Images/newuser_hover.png")
tiles=Image.open("Images/menu.png")
tiles_hover=Image.open("Images/menu_hover.png")
snake=Image.open("Images/snake.jpg")
snake_hover=Image.open("Images/snake_hover.jpg")
space=Image.open("Images/space.jpg")
space_hover=Image.open("Images/space_hover.jpg")
num=Image.open("Images/2048.jpg")
num_hover=Image.open("Images/2048_hover.jpg")

#resize
resized= logo.resize((390,295), Image.ANTIALIAS)
new_pic =ImageTk.PhotoImage(resized)
    #for user and menu btn hover
new_tiles=ImageTk.PhotoImage(tiles)
new_tiles_hover=ImageTk.PhotoImage(tiles_hover)
new_user=ImageTk.PhotoImage(user)
new_user_hover=ImageTk.PhotoImage(user_hover)
    #for game tiles
new_snake=ImageTk.PhotoImage(snake)
new_snake_hover=ImageTk.PhotoImage(snake_hover)
new_space=ImageTk.PhotoImage(space)
new_space_hover=ImageTk.PhotoImage(space_hover)
new_num=ImageTk.PhotoImage(num)
new_num_hover=ImageTk.PhotoImage(num_hover)

#heading
logo_lbl=Label(myw,image=new_pic)
logo_lbl.pack(pady=10)


#user buttons
user_btn=Button(myw,image=new_user,borderwidth=0,command=f1.new_user)
user_btn.place(x=700,y=35)
menu_btn=Button(myw,image=new_tiles,borderwidth=0,command=f1.show_tiles)
menu_btn.place(x=50,y=40)


#label for user 
user_label=Label(myw,text='',anchor=E,font=("Helvectia",14))
user_label.pack(side=BOTTOM,fill=X,ipady=2)


#for user buttons hovering
user_btn.bind("<Enter>",f2.button_hover)
user_btn.bind("<Leave>",f2.button_leave)
menu_btn.bind("<Enter>",f2.button_enter)
menu_btn.bind("<Leave>",f2.button_exit)


#for gaming tiles
snake_temp=Button(myw,image=new_snake,command=f1.open_snake,borderwidth=0)
snake_temp.place(x=50,y=400)
num_temp=Button(myw,image=new_num,command=f1.open_number,borderwidth=0)
num_temp.place(x=300,y=400)
space_temp=Button(myw,image=new_space,command=f1.open_space,borderwidth=0)
space_temp.place(x=550,y=400)


#for gaming tiles hover
snake_temp.bind("<Enter>",f2.snake_hover)
snake_temp.bind("<Leave>",f2.snake_hover_exit)
num_temp.bind("<Enter>",f2.num_hover)
num_temp.bind("<Leave>",f2.num_hover_exit)
space_temp.bind("<Enter>",f2.space_hover)
space_temp.bind("<Leave>",f2.space_hover_exit)

mainloop()



    
