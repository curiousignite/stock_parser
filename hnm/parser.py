import time
import requests
from playsound import playsound


def extract_source():
    url = (
        "https://www2.hm.com/hmwebservices/service/product/tr/availability/1134755.json"
    )
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        json_output = requests.get(url, headers=agent).json()
        print(time.ctime(), json_output)
        for i in json_output["availability"]:
            if i != "1134755003006":
                playsound("../alarm.wav")
                print("works")
    except:
        print(time.ctime(), "timeout")


while True:
    extract_source()
    time.sleep(30)
