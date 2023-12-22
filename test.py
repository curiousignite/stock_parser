from main import hm_parser, mango_parser, zara_parser

print("=====MANGO=====")
mango_parser(
    "https://shop.mango.com/tr/kadin/kazaklar-ve-h%C4%B1rkalar-kazak/v-yaka-ince-triko-kazak_57064406.html",
    -1,
)
print("=====HM=====")
hm_parser("https://www2.hm.com/tr_tr/productpage.1162785012.html")
print("=====ZARA=====")
zara_parser(
    "https://www.zara.com/tr/tr/zw-collection-yunlu-kisa-kaban-p08353724.html?v1=327778756"
)
