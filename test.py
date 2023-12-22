from main import hm_parser, mango_parser, zara_parser

print("=====MANGO=====")
print(
    "https://shop.mango.com/tr/kadin/kazaklar-ve-h%C4%B1rkalar-kazak/v-yaka-ince-triko-kazak_57064406.html"
)
mango_parser(
    "https://shop.mango.com/tr/kadin/kazaklar-ve-h%C4%B1rkalar-kazak/v-yaka-ince-triko-kazak_57064406.html",
    -1,
)
print("=====HM=====")
hm_parser("https://www2.hm.com/tr_tr/productpage.1162785012.html")
print("=====ZARA=====")
print(
    "https://www.zara.com/tr/tr/zw-collection-astar-detayli-yunlu-kaban-p07522264.html?v1=318573411"
)
zara_parser(
    "https://www.zara.com/tr/tr/uzun-boy-kemerli-yun-karisimli-kaban-p08452102.html?v1=322414746",
    1,
)
# while True:
#     hm_parser("https://www2.hm.com/tr_tr/productpage.1162785012.html")
