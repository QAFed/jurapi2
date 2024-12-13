
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

    @pytest.mark.parametrize('admin_ids', [
        [-2147483647],
        [0],
        [2147483647]
    ])
    def test_gz_admin_id(self, admin_ids):
        gen_data = EventGenerator(admin_ids=admin_ids)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('session_id', [
        "",
        "1",
        "Aa",
        "100 символов stoSimvolov 10010010010010010010010101010101001010101010101  СТО 100 100 100 сто сто сто",
        "254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Si",
        "255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255"
    ])
    def test_gz_session_id(self, session_id):
        gen_data = EventGenerator(session_id=session_id)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('info', [
        "{}",
        "{\"login\":\"qwe\",\"vInfo\":1}"
         ])
    def test_gz_ext_info(self, info):
        gen_data = EventGenerator(info=info)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    def test_ext_info_not_required(self):
        gen_data = EventGenerator()
        mod_diction = gen_data.get_dict_reg_event_adm()
        mod_diction.pop("extInfo")
        admin_add = AdminAdd()
        admin_add.send_request(mod_diction)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

class TestNegAdminAdd:
    @pytest.mark.parametrize('pop_param', [
        "eventTypeId",
        "ctime",
        "host",
        "adminId",
        "sessionId"
    ])
    def test_status_code_if_one_param_not_send(self, pop_param):
        gen_data = EventGenerator()
        mod_diction = gen_data.get_dict_reg_event_adm()
        mod_diction.pop(pop_param)
        admin_add = AdminAdd()
        admin_add.send_request(mod_diction)
        admin_add.check_status_code(400)

