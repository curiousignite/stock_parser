import re
import requests
import time
# from playsound import playsound


def detect_site(url):
    head = url[:30]
    hm_pattern = re.compile(r"https.+.hm\.com/.+?")
    match = re.match(hm_pattern, head)
    if match:
        hm_parser(url)
        return "hm"
    mango_pattern = re.compile(r"https.+.mango\.com/.+?")
    match = re.match(mango_pattern, head)
    if match:
        mango_parser(url)
        return "mango"
    zara_pattern = re.compile(r"https.+.zara\.com/.+?")
    match = re.match(zara_pattern, head)
    if match:
        return "zara"


def mango_parser(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        source_code = requests.get(url, headers=agent).text
        pattern = re.compile(r"\"sizeAvailability\":.+?\"", re.MULTILINE | re.DOTALL)
        match = re.findall(pattern, source_code)
        sizeAvailability = match[0][20:-1].split(",")
        if len(sizeAvailability):
            # playsound("../media/alarm.wav")
            print("Stoktaki bedenler:", sizeAvailability, time.ctime())
        else:
            print("Stoklar boş", time.ctime())
    except:
        print(time.ctime(), "timeout")


# H&M Part


def hm_parser(url):
    pattern = re.compile(r"productpage.\d*.html")
    product_page = re.search(pattern, url)
    if product_page:
        id = product_page.group()[12:-8]
        url = (
            "https://www2.hm.com/hmwebservices/service/product/tr/availability/"
            + id
            + ".json"
        )
    elif url[-5:] == ".json":
        pass
    else:
        print("H&M ERROR")
        return 1
    agent = {"User-Agent": "Mozilla/5.0"}
    try:
        json_output = requests.get(url, headers=agent).json()
        # print(json_output, time.ctime())
        print("Stoktaki bedenler: ")
        for i in json_output["availability"]:
            # playsound("../media/alarm.wav")
            print(i)
    except:
        print("timeout", time.ctime())


def zara_parser(url):
    pass


# while True:
#     mango_parser(url)
#     time.sleep(30)
def main():
    url = input("Mango, H&M veya ZARA ürün linki: ")
    site = detect_site(url)
    match site:
        case "hm":
            hm_parser(url)
        case "mango":
            mango_parser(url)
        case "zara":
            zara_parser(url)


if __name__ == "__main__":
    main()
