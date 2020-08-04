2020.07.05>
1. 크롤링과 스크랩핑의 차이

2. HTML Tag
   - HTML 구조 : 테그로 구성
   - 프론트엔드
   - 백엔드

3. 크롬 개발자 도구
   - F12
   - Elements Tab - CSS Selector
   - Network Tab - Http 처리 과정

4. CSS selector / XPath
   - #movie > div.news_prime > div > ul > li:nth-child(1) : css selector
   - //*[@id="entertain"]/div[1]/div/ul/li[1] : xpath

5. request, response

6. 사전 기초 지식
   - 대상 웹 페이지 조건 확인 - robots.txt
   - 크롤러 분류 - 상태 유무, Javascript 유무
   - Request 요청 주의 할 점 - 서버 부하 고려
   - 콘텐츠 저작권 문제
   - 페이지 구조 변경 가능성 숙지

7. Urllib 사용법 및 기초 스크랩핑

8. Urllib.requeset 기초 사용법
   - 네이버 이미지 다운로드
   - 구글 HTML 정보 다운로드
   - Header 정보 확인 -> status 200 코드(정상 코드)
   - 다운로드 정보 파일 저장

9. Urllib.request 예외 처리
   - 기존 소스 코드 변경
   - 예외처리 추가
   - 기타 리팩토링

10. 패키지 설치
   - pip install lxml
   - pip install requests
   - pip install cssselect

11. 네이버 뉴스 스탠드 스크랩핑(1)
   - 네이버 메인 뉴스 정보 스크랩핑
   - 신문사 정보 리스트 출력
   - CSS 선택자 활용

12. GET / POST

2020.07.19>
13. 네이버 뉴스 스탠드 스크랩핑(2)
   - 네이버 메인 뉴스 정보 스캐립핑
   - 신문사 정보 딕셔너리 출력
   - Session 사용
   - Xpath 활용

14. 사이트 요청 정보 확인
   - encar(엔카) 사이트 정보 수신
   - Get 파라미터 요청
   - 수신 데이터 디코딩(Decoding)
   - 요청 URL 정보 분석

15. 행정안전부 사이트 RSS 데이터 수신
   - RSS란?
   - 반복문을 활용한 연속 요청
   - 요청 URL 정보 분석
   - 수신 XML 데이터 확인
   
2020.07.22>
16. 개발자 도구 송수신 분석 및 실습
   - 다음 주식 정보 분석
   - Fake-UserAgent 사용
   - Header 정보 삽입
   - 수신 데이터 가공 및 추출

2020.07.29>
17. Requests 요청 정보 Payload
   - 세션 활성화 및 비활성화
   - 쿠키 정보 전송
   - User-Agent 정보 전송
   - 수신 상태 코드 확인
   
2020.07.30>
18. Httpbin 사이트를 이용한 JSON 실습
   -   수신 데이터 처리 실습
   -   수신 데이터 -> JSON 변환 출력
   -   Response 다양한 정보 출력

2020.08.01>
19. 개발자 도구 송수신 분석 및 실습
   - Rest API 란?
   - POST, PUT
   - DELETE
   - Requests 최종 정리

20. Beautiful Soup Selector
   - HTML 태그 선택자 이해
   - FIND, FIND_ALL
   - SELECT, SELECT_ONE
   - 다양한 DOM 접근 방법

2020.08.02>
21. Beautiful Soup 이미지 다운로드
   - Naver 이미지 검색 송수신 분석
   - Select, Find_all
   - 이미지 변환 및 저장
   - 예외 처리

22. Session 사용 로그인, 데이터 수집
   - 대상 사이트 로그인 과정 분석
   - 로그인 후 페이지 이동
   - 필요 데이터 추출

23. Selenium 설명 및 기본 설정
   - Driver 설치
   - 웹 자동화의 이해
   - Selenium 기초 학습
   - 다음 사이트 기반 학습

2020.08.04>
24. 데이터 수집 프로젝트 작성
   - 대상 사이트 선정 및 분석
   - Explicitly wait
   - Implicitly wait
   - 필요 정보 추출