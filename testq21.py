from io import BytesIO 
from PIL import Image, ImageTk 
import tkinter as tk
import requests
import json
from urllib.request import urlopen



root = tk.Tk()
def load_image(steamid,label):
	url='https://api.opendota.com/api/players/'+ steamid
	label.config(text='Loading an image...') 
	root.update() 
	try: 
		response = requests.get(url, timeout=10) 
		x=response.text
		y=json.loads(x)
		rawdata=urlopen(y["profile"]["avatarfull"]).read()
	except requests.exceptions.Timeout: 
		label.config(text='Timeout error') 
	else: 
		if response.status_code != 200:
			 label.config(text=f'HTTP error {response.status_code}') 
		else: pil_image = Image.open(BytesIO(rawdata)) 
		image = ImageTk.PhotoImage(pil_image)
		label.config(image=image, text='') 
		label.image=image
		label.place(x="700",y="450")
		
		
def load_hero(label,id):
	url='https://api.opendota.com/api/heroStats'
	label.config(text='Loading an image...') 
	root.update() 
	try: 
		response = requests.get(url, timeout=10) 
		x=response.text
		y=json.loads(x)
		rawdata=urlopen(y[id]["img"]).read()
	except requests.exceptions.Timeout: 
		label.config(text='Timeout error') 
	else: 
		if response.status_code != 200:
			 label.config(text=f'HTTP error {response.status_code}') 
		else: pil_image = Image.open(BytesIO(rawdata)) 
		image = ImageTk.PhotoImage(pil_image)
		label.config(image=image, text='') 
		label.image=image
		label.place(x="700",y="450")
