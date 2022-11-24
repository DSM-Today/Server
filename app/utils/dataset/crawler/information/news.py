import requests
from bs4 import BeautifulSoup as bs


class News:

    def __init__(self):
        self.url = 'https://news.naver.com/'



    def crawl(self):
        '''
        :return {
            link: 바로 가기,
            image_path: 이미지 경로,
            title: 기사 제목,
            content: 간단 내용
        }:
        '''

        response = requests.get(self.url)

        html_text = response.text

        _soup = bs(html_text, "html.parser")

        arr = _soup.findAll("div", class_="cjs_journal_wrap _item_contents")
        link = arr[0].find_next("a", class_="cjs_news_a _cds_link _editn_link")['href']
        image = arr[0].find_next("img")['src']
        title = arr[0].find_next("div", class_="cjs_t").text
        content = arr[0].find_next("p", class_="cjs_d").text
        return {
            'direct_url': link,
            'image_path': image,
            'title': title,
            'content': content
        }


news_crawler = News()
