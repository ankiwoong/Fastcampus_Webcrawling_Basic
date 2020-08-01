# Section04-3
# Requests
# requests 사용 스크랩핑(3) - Rest API

import requests

# Rest API GET, POST, DELETE, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY)
# 중요 : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET -> ex> www.movies.com/movies : 영화를 전부 조회
# GET -> ex> www.movies.com/movies/:id : 아이디인 영화를 조회
# POST -> ex> www.movies.com/movies/ : 영화를 생성
# PUT -> ex> www.movies.com/movies/ : 영화를 수정
# DELETE -> ex> www.movies.com/movies/ : 영화를 삭제

# https://jsonplaceholder.typicode.com/posts

# 세션 활성화
s = requests.Session()

"""
GET 방식 예제
"""
# 예제1
r = s.get("https://api.github.com/events")
# 수신 상태 체크
r.raise_for_status()  # 또는 status_code 체크
# 출력
print(r.text)


# 예제2
# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set("name", "niceman", domain="httpbin.org", path="/cookies")
# 요청
r = s.get("http://httpbin.org/cookies", cookies=jar)
# 출력
print(r.text)


# 예제3
# 요청
r = s.get("https://github.com", timeout=5)  # timeout -> 응답을 기다리는 시간
# 출력
print(r.text)


"""
POST 방식
"""
# 예제4
# 요청
r = s.post("http://httpbin.org/post", data={"id": "test77", "pw": "111"}, cookies=jar)
# 출력
print(r.text)
# 헤더 정보
print(r.headers)


# 예제5
# POST 데이터 셋 생성
payload1 = {"id": "test77", "pw": "111"}
payload2 = (("id", "test7777"), ("pw", "11111"))
# 요청
r = s.post("http://httpbin.org/post", data=payload2)
# 출력
print(r.text)


# 예제6(PUT)
# 요청
r = s.put("http://httpbin.org/put", data=payload1)
# 출력
print(r.text)


# 예제7(DELETE)
# 요청
r = s.delete("http://httpbin.org/delete", data={"id": 1})
# 출력
print(r.text)


# 예제7(DELETE)
# 요청
r = s.delete("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)

# 세션 종료
s.close()
