# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기

import json
import urllib.request as req
from fake_useragent import UserAgent


# Fake Header 정보(가상으로 User-Agent 생성)
ua = UserAgent()

# IE
# print(
#     ua.ie
# )  # Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)

# # EDGE
# print(
#     ua.msie
# )  # Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)

# # 크롬
# print(
#     ua.chrome
# )  # Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36

# # 사파리
# print(
#     ua.safari
# )  # Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27

# 랜덤
# print(ua.random)

# 헤더 선언
headers = {"User-Agent": ua.ie, "referer": "https://finance.daum.net/"}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode("utf-8")

# 응답 데이터 확인(Json Data)
# print("res", res)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)["data"]

# 중간 확인
print("중간 확인 : ", rank_json, "\n")

for elm in rank_json:
    # print(type(elm)) #Type 확인
    print(
        "순위 : {}, 금액 : {}, 회사명 : {}".format(
            elm["rank"], elm["tradePrice"], elm["name"]
        ),
    )
