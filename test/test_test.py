from endpoints.journal_admin_add import AdminAdd
from generators.event_generator import EventGenerator


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
        add_admin_event.send_request(gen_event.get_dict_reg_event())
        add_admin_event.check_status_code(200)
        add_admin_event.compare_payload_n_response()

