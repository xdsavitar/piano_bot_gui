from tkinter import *
from rgb_Color_picker import intiate_rgb_color
from script import main_loop_script




#Memory Values
temp_r_value = ""
temp_delay_value = ""


def mainwindow():
    mainw = Tk()
    mainw.title("Piano Tiles Bot V0.1")
    mainw.geometry("300x300")
    mainw.resizable(0,0)

    #Widgets
    calibrate_bot_settings_window = Button(mainw,text="Calibrate Settings",command=lambda: calibrate_settings(mainw))
    calibrate_bot_settings_window.place(relx=0.33,rely=0.2)

    intiate_bot_button = Button(mainw,text="Start",command=lambda:main_loop_script(temp_r_value))
    intiate_bot_button.place(relx=0.6,rely=0.43,relheight=0.15,relwidth=0.2)

    rgb_color_picker = Button(mainw,text="RGB Color Picker",command=lambda: intiate_rgb_color())
    rgb_color_picker.place(relx=0.33,rely=0.1)

    tile_pos = Button(mainw,text="X,Y Position")
    tile_pos.place(relx=0.33,rely=0.3)

    #Current Settings
    
    delay_between_clicks = Label(mainw,text="Delay Interval: ")
    delay_between_clicks.place(relx=0.05,rely=0.4)

    delay_interval_indicator = Label(mainw,text=temp_delay_value)
    delay_interval_indicator.place(relx=0.32,rely=0.4)

    tile_color_label = Label(mainw,text="Tile R Color: ")
    tile_color_label.place(relx=0.05,rely=0.55)

    tile_color_indicator = Label(mainw,text=temp_r_value)
    tile_color_indicator.place(relx=0.32,rely=0.55)

    mainw.mainloop()


def calibrate_settings(mainw):
    mainw.destroy()
    win = Tk()
    win.title("Calibrate Settings")
    win.resizable(0,0)

    #Widgets

    display_label = Label(win,text="Delay")
    display_label.place(relx=0.4,rely=0.05)
    
    delay_Entry = Entry(win)
    delay_Entry.place(relx=0.2,rely=0.15)

    display_label = Label(win,text="R Value")
    display_label.place(relx=0.4,rely=0.35)

    r_value_entry = Entry(win)
    r_value_entry.place(relx=0.2,rely=0.45)


    calibrate_Button = Button(win,text="Apply",command=lambda: save_script(r_value_entry.get(),delay_Entry.get(),win))
    calibrate_Button.place(relx=0.42,rely=0.65)

    win.geometry("200x200")
    win.mainloop()



def save_script(r_value_entry,delay_Entry,win):
    global mainwindow
    global temp_r_value 
    global temp_delay_value


    temp_r_value = ""
    temp_delay_value = ""

    temp_r_value += r_value_entry
    temp_delay_value += delay_Entry

    print(temp_r_value,temp_delay_value)
    win.destroy()
    mainwindow()


def xyPosWindow():
    winx = Tk()
    winx.geometry("150x200")

    #For Later Purposes


    winx.mainloop()




if __name__ == "__main__":
    #mainwindow()
    xyPosWindow()