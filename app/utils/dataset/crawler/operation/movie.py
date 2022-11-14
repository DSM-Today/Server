from selenium import webdriver
from selenium.webdriver.common.by import By

from app.config import get_chromedriver_path


class Movie:

    def crawl(self):
        '''
        :return {
            name: 영화 이름,
            url: 바로 예매하러 가기 url,
            iamge_path: 사진 경로
        }:
        '''
        driver = webdriver.Chrome(get_chromedriver_path())
        driver.get("https://www.megabox.co.kr/")

        movie = driver.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[3]')

        image = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[3]/a/img').get_attribute(
            'src')
        name = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[3]/a/img').get_attribute(
            'alt')

        content = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[3]/a/div[2]/div[1]') \
            .get_attribute('innerHTML')

        content = content.replace(' ', '@').translate(str.maketrans('\n\t<br>', '      ')).replace(' ', '').replace('@',
                                                                                                                    ' ')

        movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[3]/div/div/a').click()

        url = driver.current_url

        return {
            'name': name,
            'url': url,
            'image_path': image,
            'content': content
        }


movie_crawler = Movie()
