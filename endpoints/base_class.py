class Base:
    response = None
    send_payload = None

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code,\
            f"expected status code {status_code}, but actual status code {self.response.status_code}"

