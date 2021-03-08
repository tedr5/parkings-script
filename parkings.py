import requests
import pandas as pd
import sqlalchemy as sqla

url = "https://opendata.saemes.fr/explore/dataset/places-disponibles-parkings-saemes/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
req = requests.get(url)
url_content = req.content
csv_file = open('downloaded.csv', 'wb') 
csv_file.write(url_content)
csv_file.close()

df = pd.read_csv('downloaded.csv',sep=';',skiprows=range(1,6)) 
print(df)

df['Date'] = df['Date'].str[0:10] +' '+df['Date'].str[11:19]
df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={'Date': 'horodatage','Nom parking': 'nom','Type de parc': 'type_parking',"Horaires d'accès au public (pour les usagers non abonnés)": 'horaires',
    'Code parking': 'code_parking','Type de compteur': 'type_compteur', 'Places disponibles': 'places_disponibles'})
df_places_parking = df.loc[: ,['code_parking','type_compteur','type_parking','nom','horaires','horodatage','places_disponibles']]
host = ''
db = ''
user = ''
psw = ''
name_table = 'places_parking'
engine = sqla.create_engine('mysql://'+user+':'+psw+'@'+host+'/'+db)
df_places_parking.to_sql(name_table,engine,if_exists='append',index=False,chunksize=1024,dtype={'id': sqla.Integer,'code_parking': sqla.String(255),'type_compteur': sqla.String(255),'type_parking': sqla.String(255),'nom': sqla.String(255),'horaires':  sqla.String(255),'horodatage': sqla.DateTime,'places_disponibles': sqla.Integer})

print('Finished export to Database!!\n')