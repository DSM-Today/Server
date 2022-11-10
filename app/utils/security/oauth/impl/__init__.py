from abc import ABC, abstractmethod


class OAuth(ABC):

    @abstractmethod
    def query_oauth_link(self):
        pass

    @abstractmethod
    def query_access_token(self, code: str):
        pass

    @abstractmethod
    def query_birthday(self, access_token: str):
        pass

    @abstractmethod
    def query_userinfo(self, access_token: str):
        pass


def duc_query_oauth_link(oauth: OAuth):
    return oauth.query_oauth_link()


def duc_query_access_token(oauth: OAuth, code: str):
    return oauth.query_access_token(code)


def duc_query_birthday(oauth: OAuth, access_token: str):
    return oauth.query_birthday(access_token)


def duc_query_userinfo(oauth: OAuth, access_token: str):
    return oauth.query_userinfo(access_token)
