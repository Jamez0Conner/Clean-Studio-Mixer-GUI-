from tkinter import *


root = Tk()
root.resizable(width=False,height=False)
root.geometry("1000x320")
root.title("Clean Mixer")


img = PhotoImage(file="/Users/mini/Desktop/Miscellaneous/on.png")
img2 = PhotoImage(file="/Users/mini/Desktop/Miscellaneous/logo.png")

imgs = Label(root, image=img2)
imgs.place(x=440,y=-120,relwidth=1,relheight=1)

texts = Label(root,fg="black",text="🎶"+" CLEAN STUDIO MIXER ")
texts.place(x=-180,y=-120,relwidth=1,relheight=1)

btn = Button(root,image=img,fg="white",padx=10,pady=10)
btn.pack(padx=7,pady=9)
btn.place(x=10,y=10)


# MUTE BTN

#1
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=30,y=130)
#2
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=120,y=130)
#3
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=220,y=130)
#4
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=320,y=130)
#5
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=420,y=130)
#6
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=520,y=130)
#7
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=620,y=130)
#8
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=720,y=130)
#9
btn = Button(root,fg="red",text="Mute",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=820,y=130)


# SOLO BTN


#1
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=30,y=90)
#2
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=120,y=90)
#3
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=220,y=90)
#4
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=320,y=90)
#5
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=420,y=90)
#6
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=520,y=90)
#7
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=620,y=90)
#8
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=720,y=90)
#9
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=820,y=90)
#10
btn = Button(root,fg="brown",text="Solo",padx=1,pady=1)
btn.pack(padx=1,pady=1)
btn.place(x=927,y=285)


# SLIDERS

Stereo_Out1 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.1", padx=8,pady=15)
Stereo_Out2 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.2", padx=8,pady=15)
Stereo_Out3 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.3", padx=8,pady=15)
Stereo_Out4 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.4", padx=8,pady=15)
Stereo_Out5 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.5", padx=8,pady=15)
Stereo_Out6 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.6", padx=8,pady=15)
Stereo_Out7 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.7", padx=8,pady=15)
Stereo_Out8 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.8", padx=8,pady=15)
Stereo_Out9 = LabelFrame(root, bg="white",bd=0,fg="black", text="       Ch.9", padx=8,pady=15)



Stereo_Out10 = LabelFrame(root, bg="white",bd=0,fg="black", text="""     I/O

     Master""", padx=12,pady=25)
 


Stereo_Out1.pack(padx=8,pady=35)
Stereo_Out2.pack(padx=8,pady=35)
Stereo_Out3.pack(padx=8,pady=35)
Stereo_Out4.pack(padx=8,pady=35)
Stereo_Out5.pack(padx=8,pady=35)
Stereo_Out6.pack(padx=8,pady=35)
Stereo_Out7.pack(padx=8,pady=35)
Stereo_Out8.pack(padx=8,pady=35)
Stereo_Out9.pack(padx=8,pady=35)

Stereo_Out10.pack(padx=12,pady=45)

Stereo_Out_Slider1 = Scale(Stereo_Out1,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider2 = Scale(Stereo_Out2,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider3 = Scale(Stereo_Out3,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider4 = Scale(Stereo_Out4,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider5 = Scale(Stereo_Out5,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider6 = Scale(Stereo_Out6,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider7 = Scale(Stereo_Out7,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider8 = Scale(Stereo_Out8,troughcolor="brown",from_=10,to=0, orient=VERTICAL)
Stereo_Out_Slider9 = Scale(Stereo_Out9,troughcolor="brown",from_=10,to=0, orient=VERTICAL)

Stereo_Out_Slider10 = Scale(Stereo_Out10,troughcolor="brown",from_=12,to=0, orient=VERTICAL)


Stereo_Out_Slider1.pack()
Stereo_Out_Slider2.pack()
Stereo_Out_Slider3.pack()
Stereo_Out_Slider4.pack()
Stereo_Out_Slider5.pack()
Stereo_Out_Slider6.pack()
Stereo_Out_Slider7.pack()
Stereo_Out_Slider8.pack()
Stereo_Out_Slider9.pack()

Stereo_Out_Slider10.pack()

Stereo_Out1.place(x=10,y=170)
Stereo_Out2.place(x=100,y=170)
Stereo_Out3.place(x=200,y=170)
Stereo_Out4.place(x=300,y=170)
Stereo_Out5.place(x=400,y=170)
Stereo_Out6.place(x=500,y=170)
Stereo_Out7.place(x=600,y=170)
Stereo_Out8.place(x=700,y=170)
Stereo_Out9.place(x=800,y=170)

Stereo_Out10.place(x=900,y=80)

root.mainloop()