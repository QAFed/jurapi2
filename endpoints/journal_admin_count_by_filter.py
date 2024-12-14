from endpoints.base_class import Base
import requests
from config import ConfigCl
from deepdiff import DeepDiff

class AdminCountByFilter(Base):
    endpoint = "/journal/admin/count"

    def send_request(self, payload):
        self.response = requests.post(ConfigCl.HOST_API+self.endpoint, json=payload)
        self.send_payload = payload

    def assert_count(self, expected_count):
        assert self.response.json() == expected_count
