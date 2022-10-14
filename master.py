from logging import PlaceHolder
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
from pytube import YouTube
from tkinter.filedialog import askdirectory
#import moviepy.editor as mp
import re
import os
import webbrowser



##############cores############
cor1='black'
cor2='white'
cor3='orange'
cor4='blue sky'
cor5='green'
cor6='red'

master = tk.Tk()

master.title('Grupo Anthonys')
master.geometry('620x400')
master.config(bg=cor1)
my_tree = Treeview(master)
master.resizable(False, False)
master.iconphoto(False, tk.PhotoImage(file='logo.png'))



# tk.Frame 

frame_title = tk.Frame (master, width=800, height=60, bg=cor5, relief='flat')
frame_title.grid(row=0, column=0)


frame_campus = tk.Frame (master, width=800, height=740, bg=cor1, relief='flat')
frame_campus.grid(row=1, column=0, padx=0, pady=1, sticky=tk.NSEW)

#frame_cop = Frame (master, width=750, height=20, bg=cor2, relief='flat')
#frame_cop.place(x=0, y=380)



# tk.Label title
title_label = tk.Label(frame_title, width=22, text='CONVERSOR   YOUTUBE', font='Poppins, 25', fg=cor2, bg=cor5)
title_label.place(x=85, y=7)

# Label copyright
title_cop = tk.Label(master, width=22, text='© 2022 grupo Anthonys', font='Poppins, 8', fg=cor2, bg=cor1)
title_cop.place(x=220, y=380)

# Url
label_url = tk.Label (frame_campus, width=19, height=2, text="Cole aqui o link do vídeo", font='Poppins 12', fg=cor2, bg=cor1, anchor=tk.W)
label_url.place(x=10, y=10)

entry_url = tk.Entry(frame_campus, width=30, font='poppins 14')
entry_url.place(x=10, y=50)






############ Função Destino do arquivo

def open():
    path = askdirectory(title='Select Folder')

botao_url = tk.Button(frame_campus, command=open, width=15, text='DESTINO', font='poppins, 10', bg=cor5, fg=cor2)
botao_url.place(x=460, y= 49)




########## label Opções de Download

label_opc = tk.Label (frame_campus, width=30, height=2, text="Clicar em 'Download' para começar! ", font='Poppins 12', fg=cor2, bg=cor1, anchor=tk.W)
label_opc.place(x=10, y=100)


'''
########### Funções Download

def mp3(i): # Opção de Download em MP3
    YouTube (i).streams.first().download()
    yt  =  YouTube (i) 
    yt.streams
    print('TERMINOU O DOWNLOAD EM MP3...')
    messagebox.showinfo( "CONVERSOR YOUTUBE", "O seu download MP3 terminou!")
    

botao_mp4 = tk.Button(frame_campus, width=8, text='MP3', font='poppins, 10', bg=cor5, fg=cor2,command=lambda: mp3(entry_url.get()))
botao_mp4.place(x=10, y= 150)

'''


def mp4(i):# Opção de Download em MP4

    print('fazendo download')
    VIDEO_URL = (i)
    yt = YouTube(VIDEO_URL)
    yt.streams
    for stream in yt.streams:
        print(stream)

    video = yt.streams.get_highest_resolution()
    video.download()
    print('TERMINOU O DOWNLOAD EM MP4...')
    messagebox.showinfo( "Prontinho!", "O seu download terminou!")


botao_hd = tk.Button(frame_campus, width=15, text='DOWNLOAD', font='poppins, 10', bg=cor5, fg=cor2, command=lambda: mp4(entry_url.get()))
botao_hd.place(x=10, y= 150)




'''
label_arq = tk.Label (frame_campus, width=30, height=2, text="Fazendo Donwload...", font='Poppins 12', fg=cor2, bg=cor1, anchor=tk.W)
label_arq.place(x=10, y=200)
'''

'''
########## Definindo a qualidade do arquivo 

label_arq = tk.Label (frame_campus, width=30, height=2, text="Defina a qualidade do arquivo", font='Poppins 12', fg=cor2, bg=cor1, anchor=tk.W)
label_arq.place(x=10, y=200)

'''




################### Botão YOUTBE 

def openweb():
    url = 'https://www.youtube.com/?themeRefresh=1'
    webbrowser.open(url)


botao_avi = tk.Button(frame_campus, command=openweb, width=15, text='ABRIR YOUTUBE', font='poppins, 10 ', bg=cor5, fg=cor2)
botao_avi.place(x=230, y= 150)


botao_avi = tk.Button(frame_campus, command=master.destroy, width=15, text='SAIR', font='poppins, 10', bg=cor5, fg=cor2)
botao_avi.place(x=460, y= 150)





master.mainloop()


