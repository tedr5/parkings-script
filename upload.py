import os
import time 
import requests
from mega import Mega
from datetime import datetime
"""
FILE_URL_CSV: 
 
SCRIPT TO PROTECT FROM LOSING DATA IN THE EXTRACTION PROCESS
SEND CSV FILES TO MEGA 

"""
FILE_URL_CSV = "https://opendata.saemes.fr/explore/dataset/places-disponibles-parkings-saemes/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
MEGA_EMAIL = ""
MEGA_PASSWORD = ""


def uploadToMega():
	mega = Mega()
	m = mega.login(MEGA_EMAIL, MEGA_PASSWORD)
	r = requests.get(FILE_URL_CSV, stream = True)
	print('Pass request')
	now = datetime.now() 
	dt_string = now.strftime("%d-%m-%Y_%H-%M-%S.csv")
	name_folder = dt_string[0:10]
	folder_path = f'/CSV/{name_folder}'
	with open(dt_string,"wb") as csv:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				csv.write(chunk)
	print('Pass create CSV')
	folder = m.find(folder_path)
	if folder == None:
		m.create_folder(folder_path)
		print('Create folder not existing!')
		folder = m.find(folder_path)
		m.upload(dt_string,folder[0])
		print('Upload File success!')
	else:
		print('No need to create the folder Again!')
		m.upload(dt_string,folder[0])
		print('Upload file finish!')
	
	print('Pass uploading file')
	os.remove(dt_string)
	print('Pass clean file')


uploadToMega()
		