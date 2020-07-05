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