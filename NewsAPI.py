# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 19:09:51 2022

@author: Ziyah
"""

from tkinter import*
import requests
import json

root = Tk()
root.title("News")
root.geometry("500x600")
root.configure(bg="aliceblue")

heading_label = Label(root,text = "BBC News Update",bg="aliceblue",fg="navy",font=("times",25,"bold"))
heading_label.place(relx=0.5,rely=0.05,anchor=CENTER)

news1_label = Label(root,bg="aliceblue",fg="red",font=("times",15,"bold"),wraplength=500)
news1_label.place(relx=0.5,rely=0.1,anchor=CENTER)

news2_label = Label(root,bg="aliceblue",fg="red",font=("times",15,"bold"),wraplength=500)
news2_label.place(relx=0.5,rely=0.3,anchor=CENTER)

news3_label = Label(root,bg="aliceblue",fg="red",font=("times",15,"bold"),wraplength=500)
news3_label.place(relx=0.5,rely=0.5,anchor=CENTER)

news4_label = Label(root,bg="aliceblue",fg="red",font=("times",15,"bold"),wraplength=500)
news4_label.place(relx=0.5,rely=0.7,anchor=CENTER)

news5_label = Label(root,bg="aliceblue",fg="red",font=("times",15,"bold"),wraplength=500)
news5_label.place(relx=0.5,rely=0.9,anchor=CENTER)


description1_label = Label(root,bg="aliceblue",fg="midnightblue",font=("times",15,"bold"),wraplength=500)
description1_label.place(relx=0.5,rely=0.2,anchor=CENTER)

description2_label = Label(root,bg="aliceblue",fg="midnightblue",font=("times",15,"bold"),wraplength=500)
description2_label.place(relx=0.5,rely=0.4,anchor=CENTER)

description3_label = Label(root,bg="aliceblue",fg="midnightblue",font=("times",15,"bold"),wraplength=500)
description3_label.place(relx=0.5,rely=0.6,anchor=CENTER)

description4_label = Label(root,bg="aliceblue",fg="midnightblue",font=("times",15,"bold"),wraplength=500)
description4_label.place(relx=0.5,rely=0.8,anchor=CENTER)

description5_label = Label(root,bg="aliceblue",fg="midnightblue",font=("times",15,"bold"),wraplength=500)
description5_label.place(relx=0.5,rely=0.95,anchor=CENTER)

def show_news():
    api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d8850b8928f544ac9965f3489189f71e")
    open_bbc_page = json.loads(api_request.content)
    
    title1=open_bbc_page["articles"][0]["title"]
    title2=open_bbc_page["articles"][1]["title"]
    title3=open_bbc_page["articles"][2]["title"]
    title4=open_bbc_page["articles"][3]["title"]
    title5=open_bbc_page["articles"][4]["title"]
    
    description1=open_bbc_page["articles"][0]["description"]
    description2=open_bbc_page["articles"][1]["description"]
    description3=open_bbc_page["articles"][2]["description"]
    description4=open_bbc_page["articles"][3]["description"]
    description5=open_bbc_page["articles"][4]["description"]
    
    show_btn.destroy()
    
    news1_label["text"]="Title1 : " + title1
    news2_label["text"]="Title2 : " + title2
    news3_label["text"]="Title3 : " + title3
    news4_label["text"]="Title4 : " + title4
    news5_label["text"]="Title5 : " + title5
    
    description1_label["text"]="Description1 : " + description1
    description2_label["text"]="Description2 : " + description2
    description3_label["text"]="Description3 : " + description3
    description4_label["text"]="Description4 : " + description4
    description5_label["text"]="Description5 : " + description5
    
    


show_btn= Button(root,text = "SHOW NEWS", bg="darkviolet",command=show_news)
show_btn.place(relx=0.5,rely=0.1,anchor=CENTER)



root.mainloop()








