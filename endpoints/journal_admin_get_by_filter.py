from endpoints.base_class import Base
import requests
from config import ConfigCl
from deepdiff import DeepDiff

class AdminGetByFilter(Base):
    endpoint = "/journal/admin"

    def send_request(self, payload, page_params):
        self.response = requests.post(ConfigCl.HOST_API+self.endpoint, json=payload, params=page_params )
        self.send_payload = payload

    def compare_response(self, etalon_page):
        diff = DeepDiff(etalon_page, self.response.json(), ignore_order=True)
        if diff:
            raise AssertionError(diff)
        assert not diff



