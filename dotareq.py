import requests
import json
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import testq21 as iml

def winrate(date,label):
	r=requests.get('https://api.opendota.com/api/players/'+date+'/wl')
	x=r.text
	y=json.loads(x)
	win=y["win"]
	lose=y["lose"]
	sum=win+lose

	try:
		wr=win/sum*100
	except:
		print(" ")
		label["text"]="Неверно введен dota 2 id или профиль приватный."
		label.pack(anchor=NW,padx=6,pady=6)
	try:
		wr=round(wr,2)
		label["text"]=f'Победы/поражения\n Количество побед: {win}\n Количество поражений: {lose}\n Соотншение побед к поражениям: {wr}%'
		label = ttk.Label()
		label.pack(anchor=NW, padx=6, pady=6)
	except:
		print(" ")
		
def profile(steamid,label,img):
	r=requests.get('https://api.opendota.com/api/players/'+ steamid)
	x=r.text
	y=json.loads(x)
	try:
		label["text"]=f' Информация по аккаунту:\n Dota 2 Id:{y["profile"]["account_id"]}\n Никнейм: {y["profile"]["personaname"]}\n Steam Id: {y["profile"]["steamid"]}\n Профиль steam: {y["profile"]["profileurl"]}\n'
		iml.load_image(steamid,img)
		label.pack(anchor=NW,padx=6,pady=6)	
		
	except:
		print("pwpwpw")

def dpi(steamid):
	r=requests.get('https://api.opendota.com/api/players/'+ steamid)
	x=r.text
	y=json.loads(x)
	try:
		img_data = requests.get(y["profile"]["avatarfull"]).content 
		with open('image_name.png', 'wb') as handler: 
			handler.write(img_data)
		print("\nФото профиля скачено в корневую папку программы.")
	except:
			print(" ")

def recentmatch(steamid,label,img):
	r=requests.get(f"https://api.opendota.com/api/players/{steamid}/matches")
	x=r.text
	y=json.loads(x)
	rad=y[0]["radiant_win"]
	if rad==True:
		win="Силы Света"
	elif rad==False:
		win="Силы Тьмы"
	else:
		print("err")
	if(y[0]["player_slot"]<=127):
		side="Силы Света"
	elif(y[0]["player_slot"]>=128):
		side="Силы Тьмы"
	dur=y[0]["duration"]//60
	rank=y[0]["average_rank"]
	r_num=str(y[0]["average_rank"])
	
	avg_text=" "
	if(rank>=10 and rank<=15):
		avg_txt="Рекрут "+r_num[1]
	elif(rank>=20 and rank<=25):
		avg_text="Страж "+r_num[1]
	elif(rank>=30 and rank<=35):
		avg_text="Рыцарь "+r_num[1]
	elif(rank>=40 and rank<=45):
		avg_text="Герой "+r_num[1]
	elif(rank>=50 and rank<=55):
		avg_text="Легенда "+r_num[1]
	elif(rank>=60 and rank<=65):
		avg_text="Властелин "+r_num[1]
	elif(rank>=70 and rank<=75):
		avg_text="Божество "+r_num[1]
	elif(rank>=80 and rank<=85):
		avg_text="Титан "
	r2=requests.get('https://api.opendota.com/api/heroes')
	x2=r2.text
	y2=json.loads(x2)
	id=y[0]["hero_id"]-2
	locname=y2[id]["localized_name"]
	label["text"]=f' Последний матч: {y[0]["match_id"]}\n Сыгранно за {side}\n Победили {win}\n Длительность - {dur} минут\n Сыгранно на {locname}\n K/D/A - {y[0]["kills"]}/{y[0]["deaths"]}/{y[0]["assists"]}\n Средний ранг - {avg_text}\n'
	label.pack()