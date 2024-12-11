from endpoints.base_class import Base
import requests
from config import ConfigCl
from deepdiff import DeepDiff

class AdminAdd(Base):
    endpoint = "/journal/admin"

    def send_request(self, payload):
        self.response = requests.put(ConfigCl.HOST_API+self.endpoint, json=payload)
        self.send_payload = payload

    def compare_payload_n_response(self):
        mod_response = self.response.json()
        mod_response.pop('id')
        if self.send_payload["extInfo"] == None:
            self.send_payload.pop("extInfo")
        diff = DeepDiff(self.send_payload, mod_response, ignore_order=True)
        if diff:
            raise AssertionError(diff)
        assert not diff





