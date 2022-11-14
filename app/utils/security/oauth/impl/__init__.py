from abc import ABC, abstractmethod


class OAuth(ABC):

    @abstractmethod
    def query_client_id(self):
        pass

    @abstractmethod
    def check_id_token_verify(self, id_token: str):
        pass


def duc_query_client_id(oauth: OAuth):
    return oauth.query_client_id()


def duc_check_id_token_verify(oauth: OAuth, id_token: str):
    return oauth.check_id_token_verify(id_token)
