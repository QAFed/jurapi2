from base_class import Base
import requests
from config import ConfigCl


class ClearDB(Base):
    endpoint = "/clearDB"

    def clear_db(self):
        self.response = requests.post(ConfigCl.HOST_API+self.endpoint)
