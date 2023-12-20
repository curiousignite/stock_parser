import re
import requests
import time

# from playsound import playsound

url = input("Mango ürün linki: ")


def extract_source(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        source_code = requests.get(url, headers=agent).text
        pattern = re.compile(r"\"sizeAvailability\":.+?\"", re.MULTILINE | re.DOTALL)
        x = re.findall(pattern, source_code)
        sizeAvailability = x[0][20:-1].split(",")
        if len(sizeAvailability):
            # playsound("../media/alarm.wav")
            print("Stoktaki bedenler:", sizeAvailability, time.ctime())
        else:
            print("Stoklar boş", time.ctime())
    except:
        print(time.ctime(), "timeout")


while True:
    extract_source(url)
    time.sleep(30)
