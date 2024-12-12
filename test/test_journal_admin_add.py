import allure
import pytest
from generators.event_generator import EventGenerator
from endpoints.journal_admin_add import AdminAdd

@allure.suite('Test_positive_Admin_event_add')
class TestPosAdminAdd:

    @pytest.mark.parametrize('eventTipeId',[
        -2147483647,
        0,
        2147483647
    ])
    def test_gz_event_type_id(self, eventTipeId):
        gen_data = EventGenerator(action_type=eventTipeId)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('ctime', [
        0,
        4294967295
    ])
    def test_gz_ctime(self, ctime):
        gen_data = EventGenerator(ctime=ctime)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('host', [
        "",
        "1",
        "Aa",
        "100 символов stoSimvolov 10010010010010010010010101010101001010101010101  СТО 100 100 100 сто сто сто",
        "254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Si",
        "255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255"
    ])
    def test_gz_ctime(self, host):
        gen_data = EventGenerator(ip=host)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()