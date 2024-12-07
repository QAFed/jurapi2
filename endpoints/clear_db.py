from endpoints.base_class import Base
import requests
from config import ConfigCl


class ClearDB(Base):
    endpoint = "/clearDB"

    def send_request(self):
        self.response = requests.post(ConfigCl.HOST_API+self.endpoint)
