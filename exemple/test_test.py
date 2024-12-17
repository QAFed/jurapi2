from endpoints.journal_admin_add import AdminAdd
from endpoints.journal_admin_get_by_filter import AdminGetByFilter
from generators.event_generator import EventGenerator
from generators.serial_send import SerialSender


PAYLOAD = {
            "eventTypeId": 0,
            "ctime": 100,
            "extInfo": "1",
            "host": "192.168.111.111",
            "adminId": 7,
            "sessionId": "string123"
            }
class TestAdmEvent:
    def test_add_admin_event(self):
        add_admin_event = AdminAdd()
        add_admin_event.send_request(PAYLOAD)
        add_admin_event.compare_payload_n_response()
        add_admin_event.check_status_code(200)

    def test_add_admin_from_generator(self):
        add_admin_event = AdminAdd()
        gen_event = EventGenerator()
        add_admin_event.send_request(gen_event.get_dict_reg_event_adm())
        add_admin_event.check_status_code(200)
        add_admin_event.compare_payload_n_response()

    def test_get_admin_by_filter(self):
        serial_sender = SerialSender("adm")
        get_by_filter = AdminGetByFilter()
        serial_sender.send_requests(3)
        serial_sender.create_custom_page()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        get_by_filter.compare_response(serial_sender.final_page)


