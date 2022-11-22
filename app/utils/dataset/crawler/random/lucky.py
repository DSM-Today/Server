from requests import get
from bs4 import BeautifulSoup as bs4

from app.utils.type_changer import str_to_month_with_day


class Lucky:

    def __init__(self):
        self._date_list = [
            ['0120', '0218'],
            ['0219', '0320'],
            ['0321', '0419'],
            ['0420', '0520'],
            ['0521', '0621'],
            ['0622', '0722'],
            ['0723', '0822'],
            ['0823', '0923'],
            ['0924', '1022'],
            ['1023', '1122'],
            ['1123', '1224'],
            ['1225', '0119'],
        ]
        self._star_list = ['물병자리', '물고기자리', '양자리', '황소자리', '쌍둥이자리', '게자리', '사자자리', '처녀자리', '천칭자리', '전갈자리', '사수자리',
                           '염소자리']

        self._image_list = [
            'https://user-images.githubusercontent.com/80697064/202733905-594adf0b-eaa1-413e-bb59-04f61ad6bce7.png',
            'https://user-images.githubusercontent.com/80697064/202733899-680435bb-9efc-4ed7-8021-1ec417b7f453.png',
            'https://user-images.githubusercontent.com/80697064/202733886-bb23a685-2d7b-4997-86c5-a12d9e54da83.png',
            'https://user-images.githubusercontent.com/80697064/202733879-b2e5761b-4509-4d86-8602-8a3282e2840d.png',
            'https://user-images.githubusercontent.com/80697064/202733865-7f498670-2cb7-4e40-8bd9-e65d7856f993.png',
            'https://user-images.githubusercontent.com/80697064/202733830-b2054819-fb51-4298-9a76-2b3519d18aad.png',
            'https://user-images.githubusercontent.com/80697064/202733815-e642ac5f-2b19-4d01-85c7-0797cebb3a36.png',
            'https://user-images.githubusercontent.com/80697064/202733801-41d66efa-74c7-4ce2-9bf7-f74c357ecef4.png',
            'https://user-images.githubusercontent.com/80697064/202733791-84fbb8b1-3560-4391-9ead-88f3d12dc36c.png',
            'https://user-images.githubusercontent.com/80697064/202733774-2fd6d4f6-71b3-432e-9540-f0a9bf624eda.png',
            'https://user-images.githubusercontent.com/80697064/202733756-ca20a30a-46ef-49d1-bc72-3bf640373d7e.png',
            'https://user-images.githubusercontent.com/80697064/203261670-74de5869-7537-4849-8d27-41bc2334e80d.png'
        ]

    def crawl(self, mmdd: int):
        '''
        :param mmdd:
        :returns {
            name: 운세,
            period: 운세 기간,
            content: 운세 소개
        }:
        '''

        star = self._get_star(mmdd)

        response = self._get_response(star)

        start_at, end_at = self._date_list[star]
        return {
            'name': self._star_list[star],
            'start_at': str_to_month_with_day(start_at),
            'end_at': str_to_month_with_day(end_at),
            'content': self._parse(response),
            'image_path': self._image_list[star]
        }

    def _get_star(self, mmdd: int):
        for i, day in enumerate(self._date_list):
            s, e = day

            if int(e) < int(s):
                return i

            if int(s) <= mmdd <= int(e):
                return i

    def _get_response(self, sequence_num: int):
        return get(
            f'https://search.naver.com/search.naver?query={self._star_list[sequence_num] + " 운세"}'
        ).text

    def _parse(self, response_html: str):
        return bs4(response_html, 'lxml').find(class_='text _cs_fortune_text').contents[0]


luck_crawler = Lucky()
