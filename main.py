import re
import requests
import time
import pygame

pygame.init()  # for playing sound
alarm_sound = pygame.mixer.Sound("alarm.wav")


def detect_site(url):
    head = url[:30]
    hm_pattern = re.compile(r"https.+.hm\.com/.+?")
    match = re.match(hm_pattern, head)
    if match:
        return "hm"
    mango_pattern = re.compile(r"https.+.mango\.com/.+?")
    match = re.match(mango_pattern, head)
    if match:
        return "mango"
    zara_pattern = re.compile(r"https.+.zara\.com/.+?")
    match = re.match(zara_pattern, head)
    if match:
        return "zara"


def hm_parser(url, size=-1):
    pattern = re.compile(r"productpage.\d*.html")
    product_page = re.search(pattern, url)
    product_id = url[-15:-8]
    color_id = url[-8:-5]
    if product_page:
        url = (
            "https://www2.hm.com/hmwebservices/service/product/tr/availability/"
            + product_id
            + ".json"
        )
    elif url[-5:] == ".json":
        pass
    else:
        print("H&M ERROR")
        return 1
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        json_output = requests.get(url, headers=agent).json()["availability"]
        for _ in json_output:
            if _[-6:-3] != color_id:
                json_output.remove(_)
        if size >= 0:
            for _ in json_output:
                size_id = _[-3:]
                if int(size_id) == int(size):
                    print(size, " numaralı beden mevcut!", time.ctime())
                    alarm_sound.play()
        else:
            print("Stoktaki bedenler: ", json_output, time.ctime())
    except:
        print("timeout", time.ctime())


def mango_parser(url, size=-1):
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        source_code = requests.get(url, headers=agent).text
        pattern = re.compile(r"\"sizeAvailability\":.+?\"", re.MULTILINE | re.DOTALL)
        match = re.findall(pattern, source_code)
        sizeAvailability = match[0][20:-1].split(",")
        if size >= 0:
            if sizeAvailability[size]:
                print(sizeAvailability[size], "beden mevcut!", time.ctime())
                alarm_sound.play()
            else:
                print("Stok yok...", time.ctime())
        else:
            print("Stoktaki bedenler:", sizeAvailability, time.ctime())
        # if len(sizeAvailability):
        #
        # else:
        #     print("Stoklar boş", time.ctime())
    except:
        print("timeout", time.ctime())


def zara_parser(url, size=-1):
    pattern = re.compile(r"\?v1=[0-9]{6,12}")
    product_page = re.search(pattern, url)
    if product_page:
        id = product_page.group()[4:]
        url = (
            "https://www.zara.com/itxrest/1/catalog/store/11766/product/id/"
            + id
            + "/availability"
        )
    elif url[-12:] == "availability":
        pass
    else:
        print("ZARA ERROR")
        return 1
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        json_output = requests.get(url, headers=agent).json()["skusAvailability"]
        print("Stoktaki bedenler: ", time.ctime())
        sorted_dict = {}
        for i in range(len(json_output)):
            sorted_dict[json_output[i]["sku"]] = json_output[i]["availability"]
        sorted_dict = dict(sorted(sorted_dict.items()))
        print(sorted_dict)
    except:
        print("timeout", time.ctime())


def main():
    url = input("Mango, H&M veya ZARA ürün linki: ")
    size = int(input("İstediğin beden numarası(En küçük beden 0 olacak şekilde)"))

    site = detect_site(url)
    while True:
        match site:
            case "hm":
                hm_parser(url, size)
            case "mango":
                mango_parser(url, size)
            case "zara":
                zara_parser(url, size)
        time.sleep(30)


if __name__ == "__main__":
    main()
