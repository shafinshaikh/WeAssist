from tkinter import *
import tkinter as tk
import customtkinter
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random
import sys
from PIL import Image, ImageTk
import os
import time
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
#root = tk.Tk()
#ctypes.windll.shcore.SetProcessDpiAwareness(1)
app.title("weAssist")
app.state("zoomed")
app.iconbitmap("./Assets/weAssist.ico")

bg = PhotoImage(file="./Assets/background.png")
Label = tk.Label(app, image=bg, border=0)
Label.place(relx=0, y=0)

Frame1 = tk.Frame(app,bg="white", width=782, height=943)
Frame1.place(x=190,y=0)

Frame1_Default_img=PhotoImage(file="./Assets/Frame 1 Default.png")
Frame1_img=PhotoImage(file="./Assets/Frame 1.png")
Frame1_img_label=tk.Label(Frame1, image=Frame1_Default_img, border=0)
Frame1_img_label.place(x=0,y=0)

Frame2 = tk.Frame(app,bg="white", width=782, height=943)
Frame2.place(x=958,y=0)

Frame2_Default_img=PhotoImage(file="./Assets/Frame 2 Default.png")
Frame2_img=PhotoImage(file="./Assets/Frame 2.png")
Frame2_img_label=tk.Label(Frame2, image=Frame2_Default_img, border=0)
Frame2_img_label.place(x=0,y=0)

def Mute(RightOrLeft):
    #subprocess.Popen('cmd /k cd D:\mini project\sem5\hand_gesture\yolov5-master', shell=True)
    #subprocess.Popen('python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source 0', shell=True)
    if RightOrLeft=="Left":
        Frame1_img_label.config(image=Frame1_img)
        Mic_Button_Left.place_forget()
        Textbox_Label_Left.place_forget()
        textEntry_Blind_Left.place_forget()
        Speak_Button_Left.place_forget()


        Speak_Button_Left.place(x=160, y=170)
        Textbox_Label_Left.place(x=147,y=670)
        textEntry_Mute_Left.place(x=169,y=686)
    else :
        Frame2_img_label.config(image=Frame2_img)
        Mic_Button_Right.place_forget()
        Textbox_Label_Right.place_forget()
        textEntry_Blind_Right.place_forget()
        Speak_Button_Right.place_forget()

        Speak_Button_Right.place(x=217, y=195)
        Textbox_Label_Right.place(x=200,y=670)
        textEntry_Mute_Right.place(x=215,y=686)

def Blind(RightOrLeft):
    if RightOrLeft=="Left":
        Frame1_img_label.config(image=Frame1_img)
        Speak_Button_Left.place_forget()
        Textbox_Label_Left.place_forget()
        textEntry_Mute_Left.place_forget()
        Mic_Button_Left.place_forget()

        Mic_Button_Left.place(x=160, y=170)
        Textbox_Label_Left.place(x=147,y=670)
        textEntry_Blind_Left.place(x=169,y=686)
    else :
        Frame2_img_label.config(image=Frame2_img)
        Speak_Button_Right.place_forget()
        Textbox_Label_Right.place_forget()
        textEntry_Mute_Right.place_forget()

        Mic_Button_Right.place(x=217, y=195)
        Textbox_Label_Right.place(x=200,y=670)
        textEntry_Blind_Right.place(x=215,y=686)

def Deaf(RightOrLeft):
    if RightOrLeft=="Left":
        Frame1_img_label.config(image=Frame1_img)
        Speak_Button_Left.place_forget()
        Textbox_Label_Left.place_forget()
        textEntry_Mute_Left.place_forget()
        Mic_Button_Left.place_forget()

        Mic_Button_Left.place(x=160, y=170)
        Textbox_Label_Left.place(x=147,y=670)
        textEntry_Blind_Left.place(x=169,y=686)
    else :
        Frame2_img_label.config(image=Frame2_img)
        Speak_Button_Right.place_forget()
        Textbox_Label_Right.place_forget()
        textEntry_Mute_Right.place_forget()

        Mic_Button_Right.place(x=217, y=195)
        Textbox_Label_Right.place(x=200,y=670)
        textEntry_Blind_Right.place(x=215,y=686)

#app madhle tabs.
Visual_Label=tk.Label(app, text="Visual", bg="#13102A", fg="white", border=0, font=("Calibri", 15, "bold"))
eye_button_img_Hover_left = PhotoImage(file="./Assets/eye_Hover.png")
def on_enter_eye_Left(e):
    eye_button_left.configure(image=eye_button_img_Hover_left)
    Visual_Label.place(x=150,y=380)
def on_leave_eye_Left(e):
    eye_button_left.configure(image=eye_button_img_left)
    Visual_Label.place_forget()
eye_button_img_left = PhotoImage(file="./Assets/eye.png")
eye_button_left = customtkinter.CTkButton(app, image=eye_button_img_left, fg_color="#14112C", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#14112C", command=lambda RightOrLeft="Left": Blind(RightOrLeft))
eye_button_left.place(x=35, y=280)
eye_button_left.bind('<Enter>', on_enter_eye_Left)
eye_button_left.bind('<Leave>', on_leave_eye_Left)

Vocal_Label=tk.Label(app, text="Vocal", bg="#181436", fg="white", border=0, font=("Calibri", 15, "bold"))
Lips_button_img_Hover_left = PhotoImage(file="./Assets/Lips_Hover.png")
def on_enter_Lips_Left(e):
    Lips_button_left.configure(image=Lips_button_img_Hover_left)
    Vocal_Label.place(x=150,y=480)
def on_leave_Lips_Left(e):
    Lips_button_left.configure(image=Lips_button_img_left)
    Vocal_Label.place_forget()
Lips_button_img_left = PhotoImage(file="./Assets/Lips.png")
Lips_button_left = customtkinter.CTkButton(app, image=Lips_button_img_left, fg_color="#1A1638", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#1A1638", command=lambda RightOrLeft="Left": Mute(RightOrLeft))
Lips_button_left.place(x=35, y=370)
Lips_button_left.bind('<Enter>', on_enter_Lips_Left)
Lips_button_left.bind('<Leave>', on_leave_Lips_Left)

Auditory_Label=tk.Label(app, text="Auditory", bg="#201B45", fg="white", border=0, font=("Calibri", 15, "bold"))
ear_button_img_Hover_left = PhotoImage(file="./Assets/ear_Hover.png")
def on_enter_ear_Left(e):
    ear_button_left.configure(image=ear_button_img_Hover_left)
    Auditory_Label.place(x=150,y=580)
def on_leave_ear_Left(e):
    ear_button_left.configure(image=ear_button_img_left)
    Auditory_Label.place_forget()
ear_button_img_left = PhotoImage(file="./Assets/ear.png")
ear_button_left = customtkinter.CTkButton(app, image=ear_button_img_left, fg_color="#221D49", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#221D49", command=lambda RightOrLeft="Left": Deaf(RightOrLeft))
ear_button_left.place(x=35, y=460)
ear_button_left.bind('<Enter>', on_enter_ear_Left)
ear_button_left.bind('<Leave>', on_leave_ear_Left)

Visual_Label_Right=tk.Label(app, text="Visual", bg="#28244F", fg="white", border=0, font=("Calibri", 15, "bold"))
eye_button_img_Hover_Right = PhotoImage(file="./Assets/eye_Right_Hover.png")
def on_enter_eye_Right(e):
    eye_button_Right.configure(image=eye_button_img_Hover_Right)
    Visual_Label_Right.place(x=1690,y=380)
def on_leave_eye_Right(e):
    eye_button_Right.configure(image=eye_button_img_Right)
    Visual_Label_Right.place_forget()
eye_button_img_Right = PhotoImage(file="./Assets/eye_right.png")
eye_button_Right = customtkinter.CTkButton(app, image=eye_button_img_Right, fg_color="#28244F", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#28244F", command=lambda RightOrLeft="Right": Blind(RightOrLeft))
eye_button_Right.place(x=1420, y=280)
eye_button_Right.bind('<Enter>', on_enter_eye_Right)
eye_button_Right.bind('<Leave>', on_leave_eye_Right)

Vocal_Label_Right=tk.Label(app, text="Vocal", bg="#221E43", fg="white", border=0, font=("Calibri", 15, "bold"))
Lips_button_img_Hover_Right = PhotoImage(file="./Assets/Lips_Right_Hover.png")
def on_enter_Lips_Right(e):
    Lips_button_Right.configure(image=Lips_button_img_Hover_Right)
    Vocal_Label_Right.place(x=1700,y=480)
def on_leave_Lips_Right(e):
    Lips_button_Right.configure(image=Lips_button_img_Right)
    Vocal_Label_Right.place_forget()
Lips_button_img_Right = PhotoImage(file="./Assets/Lips_right.png")
Lips_button_Right = customtkinter.CTkButton(app, image=Lips_button_img_Right, fg_color="#221E43", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#221E43", command=lambda RightOrLeft="Right": Mute(RightOrLeft))
Lips_button_Right.place(x=1420, y=370)
Lips_button_Right.bind('<Enter>', on_enter_Lips_Right)
Lips_button_Right.bind('<Leave>', on_leave_Lips_Right)

Auditory_Label_Right=tk.Label(app, text="Auditory", bg="#1A1736", fg="white", border=0, font=("Calibri", 15, "bold"))
ear_button_img_Hover_Right = PhotoImage(file="./Assets/ear_Right_Hover.png")
def on_enter_ear_Right(e):
    ear_button_Right.configure(image=ear_button_img_Hover_Right)
    Auditory_Label_Right.place(x=1660,y=580)
def on_leave_ear_Right(e):
    ear_button_Right.configure(image=ear_button_img_Right)
    Auditory_Label_Right.place_forget()
ear_button_img_Right = PhotoImage(file="./Assets/ear_right.png")
ear_button_Right = customtkinter.CTkButton(app, image=ear_button_img_Right, fg_color="#1A1736", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#1A1736", command=lambda RightOrLeft="Right": Deaf(RightOrLeft))
ear_button_Right.place(x=1420, y=460)
ear_button_Right.bind('<Enter>', on_enter_ear_Right)
ear_button_Right.bind('<Leave>', on_leave_ear_Right)

textEntry_Name_Right= Text(app, wrap=WORD, width=6, height=1, bg="#373075", fg="white", border=0, font=("Calibri", 11, "bold"), yscrollcommand=True)
textEntry_Name_Right.insert(INSERT,"NAME")
textEntry_Name_Right.tag_configure("tag_name", justify='center')
textEntry_Name_Right.tag_add("tag_name", "1.0", "end")
textEntry_Name_Right.place(x=54,y=890)
textEntry_Name_Left= Text(app, wrap=WORD, width=6, height=1, bg="#0D0B1F", fg="white", border=0, font=("Calibri", 11, "bold"), yscrollcommand=True)
textEntry_Name_Left.insert(INSERT,"NAME")
textEntry_Name_Left.tag_configure("tag_name", justify='center')
textEntry_Name_Right.tag_add("tag_name", "1.0", "end")
textEntry_Name_Left.place(x=1796,y=890)

#App madhle tabs.

Speaking = PhotoImage(file="./Assets/Speaking.png")
Speaking_Label=tk.Label(Frame2, image=Speaking, border=0)

#required ahe ha code ekdam
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
#tya voice madhe 0,1,..vagre pass karun avaj badaltat
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)

# he speech recognition sathicha actual function ahe
def startHearing(RightOrLeft):
    if RightOrLeft=="Left" :
        textEntry_Blind_Left.delete("1.0","end")
        textEntry_Blind_Left.insert(INSERT,"Listening for you...")
    else :
        textEntry_Blind_Right.delete("1.0","end")
        textEntry_Blind_Right.insert(INSERT,"Listening for you...")
    print("Listening Mode...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you: {query}\n")
        # ithe label update hotay dispText ya aplya label cha
        if RightOrLeft=="Left":
            textEntry_Blind_Left.delete("1.0","end")
            textEntry_Blind_Left.insert(INSERT,str(query))
            print("done")
        else :
            textEntry_Blind_Right.delete("1.0","end")
            textEntry_Blind_Right.insert(INSERT,str(query))

    except Exception as e:
        # print(e)
        print("Say that again please...")
        errorMsg = "Error in recognizing speech!\nThis maybe due to:\n1. Background noise\n2. Unclear pronunciations "
        if RightOrLeft=="Left":
            textEntry_Blind_Left.insert(INSERT,errorMsg)
        else :
            textEntry_Blind_Right.insert(INSERT,errorMsg)
        return "None"
    return query

def speak(audio):
            engine.say(audio)
            engine.runAndWait()

def speakText(RightOrLeft):
        #Speaking_Label.place(x=370, y=560)
        tospeak_Right = textEntry_Mute_Right.get("1.0", "end-1c")
        tospeak_Left = textEntry_Mute_Left.get("1.0", "end-1c")
        if RightOrLeft=="Left":
            tospeak=tospeak_Left
        else :
            tospeak=tospeak_Right
        print("Speaking Assist mode")
        speak(tospeak)
        if RightOrLeft=="Left":
            textEntry_Mute_Left.delete("1.0","end")
        else :
            textEntry_Mute_Right.delete("1.0","end")
        Speaking_Label.place_forget()

Mic = PhotoImage(file="./Assets/Mic.png")
Mic_Button_Right = customtkinter.CTkButton(Frame2, image=Mic, fg_color="#1D1A3C", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#100D29", command=lambda RightOrLeft="Right" : startHearing(RightOrLeft))
Mic_Button_Left = customtkinter.CTkButton(Frame1, image=Mic, fg_color="#100D23", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#100D29", command=lambda RightOrLeft="Left" : startHearing(RightOrLeft))

Speak = PhotoImage(file="./Assets/Speak.png")
Speak_img_Left=PhotoImage(file="./Assets/Speak_Left.png")
Speak_Button_Right = customtkinter.CTkButton(Frame2, image=Speak, fg_color="#1D1A3C", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#1D1A37", command=lambda RightOrLeft="Right" : speakText(RightOrLeft))
Speak_Button_Left = customtkinter.CTkButton(Frame1, image=Speak_img_Left, fg_color="#100D23", border_width=0, width=0, text="", bg_color="#100D23", hover_color="#1D1A37", command=lambda RightOrLeft="Left" : speakText(RightOrLeft))

Textbox = PhotoImage(file="./Assets/Textbox.png")
Textbox_Label_Left=tk.Label(Frame1, image=Textbox, bg="#100D23", border=0)
Textbox_Label_Right=tk.Label(Frame2, image=Textbox, bg="#100D23", border=0)

textEntry_Blind_Left= Text(Frame1, wrap=WORD, width=26, height=5, bg="#100D23", fg="white", border=0, font=("Calibri", 15, "bold"), yscrollcommand=True)
textEntry_Blind_Left.insert(INSERT,"Spoken Text Appears Here.")
textEntry_Blind_Right= Text(Frame2, wrap=WORD, width=26, height=5, bg="#100D23", fg="white", border=0, font=("Calibri", 15, "bold"), yscrollcommand=True)
textEntry_Blind_Right.insert(INSERT,"Spoken Text Appears Here.")

textEntry_Mute_Right= Text(Frame2, wrap=WORD, width=26, height=5, bg="#100D23", fg="white", border=0, font=("Calibri", 15, "bold"), yscrollcommand=True)
textEntry_Mute_Right.insert(INSERT,"Write Text Here to say it aloud.")
textEntry_Mute_Left= Text(Frame1, wrap=WORD, width=26, height=5, bg="#100D23", fg="white", border=0, font=("Calibri", 15, "bold"), yscrollcommand=True)
textEntry_Mute_Left.insert(INSERT,"Write Text Here to say it aloud.")

weAssist_Hover_img = PhotoImage(file="./Assets/weAssist_Hover.png")
weAssist_Hover = tk.Label(app, image=weAssist_Hover_img, border=0)
def on_enter_weAssist(e):
    weAssist_Hover.place(x=180,y=50)
def on_leave_weAssist(e):
    weAssist_Hover.place_forget()
weAssist_Logo=PhotoImage(file="./Assets/weAssist.png")
weAssist=tk.Button(app, image=weAssist_Logo, fg="#14112C", bg="#0D0B1F", border=0, width=0)
weAssist.place(x=0,y=0)
weAssist.bind('<Enter>', on_enter_weAssist)
weAssist.bind('<Leave>', on_leave_weAssist)

Github_Hover_img = PhotoImage(file="./Assets/Github_Hover.png")
def on_enter_Github(e):
    Github.config(image=Github_Hover_img)
def on_leave_Github(e):
    Github.config(image=Github_Logo)
Github_Logo=PhotoImage(file="./Assets/Github.png")
def Github_link(url):
   webbrowser.open_new_tab(url)
Github=tk.Button(app, image=Github_Logo, fg="#322D61", bg="#322D61", border=0, width=0)
Github.place(x=1730,y=0)
Github.bind('<Enter>', on_enter_Github)
Github.bind('<Leave>', on_leave_Github)
Github.bind('<Button-1>', lambda e:
Github_link("http://github.com/gandhardate/weassist"))

app.mainloop()