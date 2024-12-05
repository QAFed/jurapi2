


class Base:
    response = None


    def check_status_code(self, status_code):
        assert self.response == status_code

