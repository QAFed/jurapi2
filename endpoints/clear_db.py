from base_class import Base
import requests 
from config import Config


class ClearDB(Base):
    endpoint = "/clearDB"

    def clear_db(self):
        self.response = requests.post(Config.API_HOST+self.endpoint)
