import allure

from endpoints.journal_admin_add import AdminAdd
from generators.event_generator import EventGenerator


class SerialSender:
    var_class = {
        "adm": AdminAdd
    }

    def __init__(self, event_type, ext_data=None, page_params=None):
        self.choise_class = event_type
        self.ext_data = ext_data or {}
        self.exp_list = []
        self.num_data = EventGenerator(**self.ext_data)
        self.page_params = page_params or {'page': 0, 'pageSize': 2}
        self.final_page = None
        self.payload_filter = getattr(self.num_data, f'get_dict_filter_{self.choise_class}')()
    @allure.step("Загрузка тестовых данных из serial_sender")
    def send_requests(self, replay_count):

        for num in range(0, replay_count+1):
            num_request = self.var_class[self.choise_class]()
            num_payload = getattr(self.num_data, f'get_dict_reg_event_{self.choise_class}')()
            num_request.send_request(num_payload)
            if num_request.response.status_code != 200:
                raise AssertionError(f"actual status code of load data from serial_sender is {num_request.response.status_code}")
            mod_num_payload = {k: v for k, v in num_payload.items() if v is not None}
            mod_num_payload['id'] = num_request.response.json().get('id')
            self.exp_list.append(mod_num_payload)

    def create_custom_page(self):
        if self.num_data.sort_by == "time":
            filter_sort_by = "ctime"
        else:
            filter_sort_by = self.num_data.sort_by

        filtered_list= sorted(self.exp_list, key=lambda x: x[filter_sort_by], reverse=self.num_data.sort_order == "desc")

        len_list = len(filtered_list)
        num_page = self.page_params["page"]
        count_on_page = self.page_params["pageSize"]
        if len_list % count_on_page == 0 or len_list // count_on_page != num_page:
            self.final_page = filtered_list[count_on_page * num_page : count_on_page * (num_page + 1):]
        else:
            self.final_page = filtered_list[
                   count_on_page * num_page:count_on_page * (num_page + 1) + len_list % count_on_page:]
