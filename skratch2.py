import os
from tkinter import *
from PIL import Image, ImageTk

def submit():
    score = [first_team_score.get(), second_team_score.get()]
    print(f"The score is: {score[0]} to {score[1]}")

def clear():
    first_team_score.delete(0,END) #deletes the line of text
    second_team_score.delete(0,END)

window = Tk()
window.title("PREDICT GAME")
window.geometry("810x520")
wc_icon = PhotoImage(file = "wc_icon.png")
window.iconphoto(False, wc_icon)

flag_path = os.getcwd() + '/Country-Flags/'

cur_team = 'World_Cup'
wc_logo = flag_path + cur_team + '.png'
trophy_image = Image.open(wc_logo)
trophy_resize = trophy_image.resize((150, 105)) # SQUARE
wc_trophy = ImageTk.PhotoImage(trophy_resize)
trophy_label = Label(image = wc_trophy)

first_team = Label(window,text="Argentina")
first_team.config(font=("Ariel",30))

new_path = flag_path + 'Argentina.png'
new_im = Image.open(new_path)
img_resized = new_im.resize((320, 200)) # SQUARE
first_tk_image = ImageTk.PhotoImage(img_resized)
first_flag = Label(image=first_tk_image)

versus = Label(window,text="VS")
versus.config(font=("Ariel",50))

second_team = Label(window,text="Morocco")
second_team.config(font=("Ariel",30))
new_path = flag_path + 'Morocco.png'
new_im = Image.open(new_path)
# print(f"Original size : {new_im.size}") # 5464x3640
img_resized = new_im.resize((320, 200)) # SQUARE
# print(f"New size : {img_resized.size}") # 5464x3640
second_tk_image = ImageTk.PhotoImage(img_resized)
second_flag = Label(image=second_tk_image)


first_team_score = Entry(justify = RIGHT, width = 2, font=('Roboto',40), bg='#111111', fg='#00FF00')

second_team_score = Entry(width = 2, font=('Roboto',40), bg='#111111', fg='#00FF00')

submit = Button(window, text="Submit",command=submit, font=('Ariel',30))
clear = Button(window, text="clear",command=clear, font=('Ariel',16))

# first_team.pack(side= LEFT)
# second_team.pack(side=RIGHT)
# entry.pack(side = LEFT)
# newentry.pack(side = RIGHT)

trophy_label.grid(row = 0, column = 1)

first_flag.grid(row = 1, column = 0)
first_team.grid(row = 2, column = 0)
first_team_score.grid(row = 3, column = 0)


versus.grid(row = 2, column = 1)

second_flag.grid(row = 1, column = 2)
second_team.grid(row = 2, column = 2)
second_team_score.grid(row = 3, column = 2)

clear.grid(row = 4, column = 1)
submit.grid(row = 5, column = 1)

#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character

window.mainloop()