import requests
import time
import sched
from datetime import datetime

 
POST = { "login" : "FREEWIFI_ID",
         "password" : "FREEWIFI_PASSWORD",
         "submit" : "Valider" }

def check_wifi_auth():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        url = "http://google.fr"
        url_redirect = requests.get(url).url  # redirection de url de freewifi.

     
        #https://wifi.free.fr/?url=http://google.fr/
        if "wifi.free.fr" in url_redirect:
            req = requests.get("https://wifi.free.fr/Auth", params=POST, verify=False)
            #print(req.text)
            print("{} : Authentication succeed.".format(dt_string))
        else:
            print("{} : You are connected.".format(dt_string))
    except:
        print("{} : Connection failure, check your network settings".format(dt_string))


s = sched.scheduler(time.time, time.sleep)

while True:
    check_wifi_auth()
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        break

