from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
import shutil 


#functions
def select_path():
    #allows user to select the path from explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():    
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #download viedo
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selecter directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')

screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500, height=500, background='#4A4A4A')
canvas.pack()

# get the path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# construct the path to the image file relative to the script directory
image_path = os.path.join(script_dir, "image.png")

# load the image using PhotoImage
logo_image = PhotoImage(file=image_path)
logo_image = logo_image.subsample(3)

# create a label for the logo image and add it to the canvas
logo_label = Label(screen, image=logo_image, bg="#4A4A4A")
canvas.create_window(250, 100, window=logo_label)

#link field
link_field = Entry(screen, width=30, font=('Arial', 15))
link_label = Label(screen, text="Enter Download Link:", font=('Arial', 15), pady='10', padx='22', fg='black')

#Select path for saving the file
path_label = Label(screen, text="Select Path Below:", font=('Arial', 15), fg='black')
select_btn =  Button(screen, text="Select Path", bg='grey', padx='22', pady='5',font=('Arial', 15), fg='black', command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Addd widget to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#downlad buttons
download_btn = Button(screen, text="Download File",bg='grey', padx='22', pady='5',font=('Arial', 15), fg='black', command=download_file)

#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop() 