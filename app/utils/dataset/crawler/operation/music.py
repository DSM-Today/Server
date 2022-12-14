from requests import get

from random import randint
from typing import Optional

from app.utils.type_changer import str_to_date


def generate_random_int(maximum: int, minimum: Optional[int] = None):
    minimum = 1 if minimum is None else minimum
    return randint(minimum, maximum)


class Music:

    def __init__(self):
        self._situation_id_list = [1, 4, 11, 12, 2, 13, 5, 6, 14, 15, 3, 17, 18, 19, 10, 122, 123]
        self._situation_name_list = ['드라이브', '공부/독서', '사랑', '이별', '운동/헬스', '산책/여행', '아침', '밤/새벽', '카페', '휴식/힐링', '출/퇴근',
                                     '혼술/혼밥', '내 방', '노래방', '호텔/라운지', '펍/바', '일/작업']


    def crawl(self):
        '''
        :return {
            situation: 듣기 좋은 상황
            playlist_provider: 플레이리스트 제공자
            playlist_direct_url: 플레이리스트 바로가기 url
            is_adult: 성인 여부
            image_path: 이미지 바로 가기
            album_name: 앨범 이름
            released_at: 발매일
            title: 곡 제목
            play_time: 재생 시간
            song_writer: 작곡가
        }:
        '''
        random_int = generate_random_int(len(self._situation_name_list) - 1)

        self._situation = self._situation_name_list[random_int]
        self._situation_id = self._situation_id_list[random_int]

        channel_id = self._get_random_playlist_id()

        playlist_detail = self._get_playlist_detail(channel_id)

        return self._parse_playlist_detail(playlist_detail)

    def _get_random_playlist_id(self) -> int:
        channel_list = get(
            f'https://www.music-flo.com/api/display/v1/browser/SITTN/{self._situation_id}?sortType=RECOMMEND'
        ).json()['data']['chnlList']

        random_int = generate_random_int(len(channel_list) - 1)

        return channel_list[random_int]['id']

    @staticmethod
    def _get_playlist_detail(playlist_id: int) -> dict:
        return get(
            f'https://www.music-flo.com/api/meta/v1/channel/{playlist_id}'
        ).json()['data']

    def _parse_playlist_detail(self, playlist_detail: dict):
        random_int = generate_random_int(playlist_detail['trackCount'] - 1)
        track = playlist_detail['trackList'][random_int]
        return {
            'situation': self._situation + ' 때 듣기 좋아요!!',
            'direct_url': f"https://www.music-flo.com/search/theme?keyword={playlist_detail['name'].replace(' ', '%20')}&sortType=ACCURACY",
            'image_path': track['album']['imgList'][2]['url'],
            'published_at': str_to_date(track['album']['releaseYmd']),
            'title': track['name'],
            'song_writer': track['representationArtist']['name']
        }


music_crawler = Music()
