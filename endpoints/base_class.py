class Base:
    response = None

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code
        # try:
        #     assert self.response.status_code == status_code, f"expect {status_code} or fact {self.response.status_code}"
        # except AssertionError as e:
        #     print(f"Warning: {e}")

