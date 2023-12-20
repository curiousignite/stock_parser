import time
import requests
# from playsound import playsound
# url = "https://www2.hm.com/hmwebservices/service/product/tr/availability/1134755.json"

url = input("H&M ürün linki: ")


def extract_source(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        json_output = requests.get(url, headers=agent).json()
        print(json_output, time.ctime())
        for i in json_output["availability"]:
            # TODO : Bedenleri listele ve hardcode' çıkart
            if i != "1134755003006":
                # playsound("../media/alarm.wav")
                print("works")
    except:
        print("timeout", time.ctime())


while True:
    extract_source(url)
    time.sleep(30)
