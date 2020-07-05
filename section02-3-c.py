# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)

import requests
import lxml.html


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """
    # 세션 사용 권장
    # session = requests.Session()
    # session.get('https://www.naver.com/')

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com/")
    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    # 결과 출력
    for url in urls:
        # url
        print(url)
        # 파일 쓰기
        # 생략


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []
    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    # 문서내 경로 절대 경로 변환
    # root.make_links_absolute(response.url)

    for a in root.cssselect(".thumb_box > .popup_wrap > a.btn_popup"):
        # 링크
        url = a.get("href")
        # class 중복으로 인한 # 제거 방법
        if len(url) >= 2:
            # 리스트 삽입
            urls.append(url)
        else:
            pass
    return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
