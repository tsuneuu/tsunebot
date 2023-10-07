import requests
import time

#api
TG_API = 'https://api.telegram.org/bot'
IMG_FOXES_API = 'https://randomfox.ca/floof/'

#token
TG_TOKEN = '6536795867:AAHeFu-RmvKYpOVMqa8laFABGEBdWaYrSko'

#Requests for TG API
counter = 0
FINAL = 200
offset = -2
fox_photo: str

while counter < FINAL:
    print("Attempts: ", counter)

    event = requests.get(f"{TG_API}{TG_TOKEN}/getUpdates?offset={offset + 1}").json()
    fox_link = requests.get(IMG_FOXES_API)

    if event['result']:
        for result in event['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            fox_photo = fox_link.json()['link']

            requests.get(f"{TG_API}{TG_TOKEN}/sendMessage?chat_id={chat_id}&text=Я всего-лишь лиса!?")
            requests.get(f"{TG_API}{TG_TOKEN}/sendPhoto?chat_id={chat_id}&photo={fox_photo}")
    
    time.sleep(1)
    counter += 1        

