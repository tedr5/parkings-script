import pathlib
import shutil
import os
import glob
import pandas as pd
import sqlalchemy as sqla

"""
SCRIPT TO FILL THE DATABASE FROM CSV ON MEGA IF LOSE DATA IN PARTICULAR DATE
"""

PATH = "/home/thomas/Documents/TER/AJOUTER_CSV_BDD/"
folder = "test/"
files_used = []
totalFiles = 0
contents = pathlib.Path(PATH+folder).iterdir()
for path in sorted(contents): # utiliser .stem -> nom sans extension fichier / .name -> nom fichier complet
    files_used.append(path.name)
    totalFiles+=1

print(files_used)
print(totalFiles)

li = []

for filename in files_used:
	df = pd.read_csv(PATH+folder+filename,sep=';',skiprows=range(1,6),index_col=0)
	li.append(df)

frame = pd.concat(li)


frame.to_csv("merged.csv",sep=';')
print('FINISH MERGING FILES!')

#Move all files used in folder dest
folder_dest = 'dest'
for file in files_used:
    shutil.move(PATH+folder+file, PATH+folder_dest)
print('FINISH MOVING MERGED FILES!')


df = pd.read_csv('merged.csv',sep=';') 


df['Date'] = df['Date'].str[0:10] +' '+df['Date'].str[11:19]
df = df.rename(columns={'Date': 'horodatage','Nom parking': 'nom','Type de parc': 'type_parking',"Horaires d'accès au public (pour les usagers non abonnés)": 'horaires','Code parking': 'code_parking','Type de compteur': 'type_compteur', 'Places disponibles': 'places_disponibles'})
df['horodatage'] = pd.to_datetime(df['horodatage'])
df = df.loc[: ,['code_parking','type_compteur','horodatage','places_disponibles']]
print('FINISH CLEAN DF!')
print(df)
df.info()

host = ''
port = ''
db = ''
user = ''
psw = ''
name_table = ''


# dialect+driver://username:password@host:port/database
engine = sqla.create_engine('mysql://'+user+':'+psw+'@'+host+':'+port+'/'+db)
print('CONNECTED!')

"""

df.to_sql(name_table,engine,if_exists='append',index=False,chunksize=1024,dtype={'id': sqla.Integer,'code_parking': sqla.String(255),'type_compteur': sqla.String(255),'horodatage': sqla.DateTime,'places_disponibles': sqla.Integer})
print('Finished export to Database!')
"""






