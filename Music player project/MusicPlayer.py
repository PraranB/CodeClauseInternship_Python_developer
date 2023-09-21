import tkinter
import pygame
from tkinter import *
import customtkinter 
import time
import math
#import tkinter.ttk as ttk
from PIL import Image, ImageTk
from threading import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


project = customtkinter.CTk()
project.title('My MP3 Player')
project.geometry('485x600+290')
project.resizable(False, False)
lower_frame = Frame(project, bg= '#C21A09',width= 485, height= 250)
lower_frame.place(x = 0, y= 400)

pygame.mixer.init()

# Adding songs and cover img

songs_list = ['Songs/Binks no sake.mp3', 'Songs/Let Her Go.mp3','Songs/Night Changes.mp3','Songs/Unbreakable(Nightcore).mp3']
cover_list = ['img/brook.jpeg', 'img/passenger.jpg', 'img/Night changes.jpg' ,'img/Unbreakable.jpg']

# Main
n = 0

music_frame = Frame(project)
music_frame.pack()



def get_album_cover(song_name, n) :
    image1 = Image.open(cover_list[n])
    image2 = image1.resize((300,300))
    load = ImageTk.PhotoImage(image2)

    label1 = tkinter.Label(project, image= load)
    label1.image = load
    label1.place(relx= .2, rely= .06)
    stripped_string = song_name[6:]
    song_name_label = tkinter.Label(text= stripped_string, bg= '#03fc7f', fg= 'white')
    song_name_label.place(relx= .4, rely= .6)


def progress():
    a = pygame.mixer.Sound(f'{songs_list[n]}')
    pygame.mixer.music.get_pos() / 1000000
    #converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    global song_len
    song_len = a.get_length() * 3
    #print(song_len)
    for i in range(0, math.ceil(song_len)) :
        time.sleep(.4)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)
    
    #converted_song_length = time.strftime("%M:%S", time.gmtime(song_len))
    #my_slider.config(value= int(current_time) )

'''def slide(x):
    slider_label.config(text= f'{int(my_slider.get())} of {int(song_len)}')'''

def threading() :
    t = Thread(target=progress)
    t.setDaemon(True)
    t.start()


def play_music():
    threading()
    global n 
    current_song = n
    if n>3 :
        n=0
    song_name = songs_list[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops= 0)
    pygame.mixer.music.set_volume(.4)
    get_album_cover(song_name, n)
    n += 1

    #slider length
    slider_length = int(song_len)
    #my_slider.config(to=slider_length, value=0)

global paused
paused = False

def pause_music(is_paused) :
    global paused
    paused = is_paused
    if paused :
        pygame.mixer.music.unpause()
        paused = False
    else :
        pygame.mixer.music.pause()
        paused = True

def next_song() :
    play_music()

def back_song() :
    global n
    n -= 2
    play_music()

def song_volume(value) :
    # print(value)
    pygame.mixer.music.set_volume(value)


# Buttons

play_button = customtkinter.CTkButton(master=project, text='Play',fg_color ='#FC6A03' ,command= play_music )
play_button.place(relx= 0.35, rely= 0.80, anchor= tkinter.CENTER)

pause_button = customtkinter.CTkButton(master= project,text= 'pause', fg_color= '#FC6A03', command= lambda : pause_music(paused) )
pause_button.place(relx= 0.65, rely= 0.80, anchor= tkinter.CENTER)

next = customtkinter.CTkButton(master=project, text='>>', fg_color ='#FC6A03', command= next_song, width= 4 )
next.place(relx= 0.83, rely= 0.80, anchor= tkinter.CENTER)

back = customtkinter.CTkButton(master=project, text='<<', fg_color ='#FC6A03' , command= back_song, width= 4 )
back.place(relx= 0.17, rely= 0.80, anchor= tkinter.CENTER)

volume = customtkinter.CTkSlider(master=project, from_=0, to=1, command= song_volume  )
volume.place(relx= 0.78, rely= 0.88, anchor= tkinter.CENTER)

'''my_slider = ttk.Scale(project, from_=0, to=100, orient= HORIZONTAL, value=0, command= slide, length= 450)
my_slider.place(relx= .5,rely= .72, anchor= tkinter.CENTER)
slider_label = Label(project, text='0')
slider_label.place(relx=0.02, rely=.75 )'''


progressbar= customtkinter.CTkProgressBar(master= project, progress_color= '#03fc7f',width= 350)
progressbar.place(relx = .5, rely = .72, anchor = tkinter.CENTER)

project.mainloop()