import requests
import json
import dotareq as dr
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import testq21 as im

def show_mess():
	steamid=entry.get()
	label['text']=steamid
	return steamid
	
root=Tk()
root.title("Dota Analize")
root.geometry("500x300")
title=ttk.Label()
title["text"]="Dota Analize"
title["background"]="dark grey"
title["font"]="Arial",16
title.pack(anchor=CENTER)

entry = ttk.Entry()
entry["justify"]="center"
entry.pack(pady=10)

def getid():
	img.place(x="10000",y="10000")
	label["text"]=" "
	steamid=entry.get()
	dr.winrate(steamid,label)
def prof():
	img.place(x="10000",y="10000")
	label["text"]=" "
	steamid=entry.get()
	dr.profile(steamid,label,img)
def recentmatch():
	img.place(x="10000",y="10000")
	label["text"]=" "
	steamid=entry.get()
	dr.recentmatch(steamid,label,img)

confirm = ttk.Button(text="Winrate", command=getid)
confirm["width"]=25
confirm.pack(pady=10)

profile_btn = ttk.Button(text="Profile", command=prof)
profile_btn["width"]=25
profile_btn.pack()

recmatch=ttk.Button(text="Последний матч", command=recentmatch)
recmatch["width"]=25
recmatch.pack(pady=10)

label=ttk.Label()
label.pack(anchor=NW, padx=8,pady=8)

img=ttk.Label()
img.pack()

root.mainloop()