from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox



root = Tk()
root.iconbitmap('Youtube_Video_Download.ico')
root.resizable(False,False)
Img = Image.open('Youtube_2_11.png')
Img.resize((200,100))
Img1 = ImageTk.PhotoImage(Img)
Label(root, image=Img1 , background='white', bd=0).place(x=370,y=310)
Link1 = Entry(root , bd=3 , selectbackground="#808080", font=("SamsungOne-700",30),background='white',insertbackground="#808080")
Path_1 = Entry(root , bd=3 , selectbackground="#808080", font=("SamsungOne-700",30),background='white',insertbackground="#808080")
Label(root, text="Enter Path here: ", font=('SamsungOne-700',20 ), fg='black', bd=0 , bg='white').place(x=20 , y=215 )
Link1.place(x=20, y=60)
Path_1.place(x=20 ,y=260 )


def Extracter_low():
   Url = Link1.get()
   Path = Path_1.get()
   try:
    my_vid = YouTube(Url)
    Path_2 = Path
   except:
      messagebox.showerror("Error",'Link Incorrect Or connection Error')
   my_vid1 = my_vid.streams.get_lowest_resolution()
   my_vid1.download(Path_2)
   messagebox.showinfo("Youtube Video Downlaoder", "Operation successfully! Thanks For Use App")
   Label(root,text="Thanks For Using App  For More AppS \n Youtube: Saad Studios ", bg='white', bd=0 , font=('arial', 10)).place(x=10 , y=420)
def Extracter_High():
   
   Url = Link1.get()
   Path = Path_1.get()
   try:
    my_vid = YouTube(Url)
    Path_2 = Path
   except:
      messagebox.showerror("Error",'Link Incorrect Or connection Error')
   Url = Link1.get()
   my_vid = YouTube(Url)
   my_vid1 = my_vid.streams.get_highest_resolution()
   my_vid1.download(Path_2)
   messagebox.showinfo("Youtube Video Downloader", 'Operation successfully! Thanks For Use App')
   Label(root,text="Thanks For Using App  For More Apps \n Youtube: Saad Studios ", bg='white', bd=0 , font=('arial', 10)).place(x=10 , y=420)


root.geometry('600x500')
root.configure(bg='white', bd=0)
root.title('Youtube Video Downloader')
txt = Label(root , text="Enter The Link of Video Here :", font=("SamsungOne-700", 20), bg='White', bd=0, fg="black").place(x=20,y=20)
lowest_Resulotion =Button(root, text="Low", bg='red', fg='black', bd=0, font=('SamsungOne-700', 20),command=Extracter_low, border=0).place(x=120, y=150)
High_Resulotion = Button(root, text="High", bg='red', fg='black', bd=0, font=('SamsungOne-700', 20),command=Extracter_High, border=0).place(x=20, y=150)



mainloop()