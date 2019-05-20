# coding:utf-8
import requests

url = "http://ume1.umetrip.com/MSky_Front/api/msky/p3/airportflystatus?encrypt=2"
s = requests.session()
header ={"Content-Type":"multipart/form-data",
         "Cookie": "X-LB=1.8.9.443301ed",
         "Connection":"keep-alive",
         "Accept": "*/*",
         "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
         "Accept-Encoding": "gzip",
        "Accept-Language": "zh-cn"
}
s.headers.update(header)
data="39CclX5dN5Ock1pWgAfWTT4NbaXD3Jy/6n5J" \
     "p5GdBKZSacgvX5ubruC9ip6B2/DGv9GP+A8BUY83" \
     "+VNupfJ874vs5iYmbgr3rrpb5y1Ji+6q4sRYXbLlgVf" \
     "6POvm0+VgUI/Tqt+FYL8crQYwrQKK+ca84cLqAVpREoqarQOqY" \
     "yNknzWlu5E8sQVroT6peJsTQfrVNBIu48C5KJF8NEwkaLvM0507SAcub" \
     "bF2onLbTtbxsoJQtHyVlFIgK6QczVsEwPWB7vdDig8XRQRfOAdUCNj4c4v4MXu1" \
     "cgBokOUrApFKfKgj2tOednP6lzKi+hlzQ9u6Vq4IKQ8QABxo5E+7uwRUPBfYq9V17e" \
     "WD8j8EihBg+9SzLOtR7xQxM6YeooCue+mRxO+Ka13S7ktp1W4GdY35tgvCbJq/41pSE" \
     "KysTcEwyoCxcrK8BcjQb1HnWqaL9ST5QduweUPK16ZVXW1U14y1LOAs1Snxwwzjkfd49g0" \
     "DCHaINqCTtwKtVPsnRwk+J6ikpfmOXaE/p6G9gXOEYL/Y1rU92mEz7v7+vSRmLCm0dIr88voge" \
     "tpPfT/FI1DMnlgvMTm9EVkdiDRr6vXZtdmulsUMPP9GuGQoU65iDqdExjnkRLj8BwQQQpmipg2R8I" \
     "9ryGth5t2mnqc8CkpCxpIfH3VxL9C3B0qRSjqu0GonrnQzIxJ8z1B5yu4X5b4CM/P+LAHFzPCIgXW4q6" \
     "pBq00TAvUPf4CdXGT++ukxjZPwBaHGtl3gSJXlTgsxmUmInX+fisc9ofu8gOFPI8+nWIm4acPnaSCO0TBP" \
     "kJ7FpQrnLpIi81BqLeDJ/Ay5p/KhU3Y0o18MxVFnEe/g53mPxmCIz0ua76h1v1M59/cx1UvxlCM0ApwUxRXzY0" \
     "Q++oi/yY9sISTeTZaPEVjmvv22Rg=="
r = s.post(url,data=data,verify=False)
print(r.text)
