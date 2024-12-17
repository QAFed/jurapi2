
import allure
import pytest

from conftest import allure_attach_request_n_response_body, before_n_after_clear_db
from generators.event_generator import EventGenerator
from endpoints.journal_admin_add import AdminAdd

@allure.suite('Test_positive_Admin_event_add')
@pytest.mark.usefixtures('before_n_after_clear_db')
class TestPosAdminAdd:

    @pytest.mark.parametrize('eventTipeId',[
        -2147483647,
        0,
        2147483647
    ])
    def test_gz_event_type_id(self, eventTipeId, allure_attach_request_n_response_body):
        gen_data = EventGenerator(action_type=eventTipeId)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('ctime', [
        0,
        4294967295
    ])
    def test_gz_ctime(self, ctime, allure_attach_request_n_response_body):
        gen_data = EventGenerator(ctime=ctime)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
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
    def test_gz_host(self, host, allure_attach_request_n_response_body):
        gen_data = EventGenerator(ip=host)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('admin_ids', [
        [-2147483647],
        [0],
        [2147483647]
    ])
    def test_gz_admin_id(self, admin_ids, allure_attach_request_n_response_body):
        gen_data = EventGenerator(admin_ids=admin_ids)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
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
    def test_gz_session_id(self, session_id, allure_attach_request_n_response_body):
        gen_data = EventGenerator(session_id=session_id)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    @pytest.mark.parametrize('info', [
        "{}",
        "{\"login\":\"qwe\",\"vInfo\":1}"
         ])
    def test_gz_ext_info(self, info, allure_attach_request_n_response_body):
        gen_data = EventGenerator(info=info)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

    def test_ext_info_not_required(self, allure_attach_request_n_response_body):
        gen_data = EventGenerator()
        mod_diction = gen_data.get_dict_reg_event_adm()
        mod_diction.pop("extInfo")
        admin_add = AdminAdd()
        admin_add.send_request(mod_diction)
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()

@allure.suite('Test_negative_Admin_event_add')
@pytest.mark.usefixtures('before_n_after_clear_db')
class TestNegAdminAdd:
    @pytest.mark.parametrize('pop_param', [
        "eventTypeId",
        "ctime",
        "host",
        "adminId",
        "sessionId"
    ])
    def test_status_code_400_if_one_param_not_send(self, pop_param, allure_attach_request_n_response_body):
        gen_data = EventGenerator()
        mod_diction = gen_data.get_dict_reg_event_adm()
        mod_diction.pop(pop_param)
        admin_add = AdminAdd()
        admin_add.send_request(mod_diction)
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)

    @pytest.mark.parametrize('eventTipeId', [
        -2147483648,
        2147483648,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_event_type_id(self, eventTipeId, allure_attach_request_n_response_body):
        gen_data = EventGenerator(action_type=eventTipeId)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)

    @pytest.mark.parametrize('adminId', [
        [-2147483648],
        [2147483648],
        ["Cтрока Strora"],
        [{'slo': 'var'}],
        [["spisok", 1]],
        [""]
    ])
    def test_status_code_400_gz_admin_id(self, adminId, allure_attach_request_n_response_body):
        gen_data = EventGenerator(admin_ids=adminId)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)

    @pytest.mark.parametrize('ctime', [
        4294967296,
        104294967295,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_ctime(self, ctime, allure_attach_request_n_response_body):
        gen_data = EventGenerator(ctime=ctime)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)

    @pytest.mark.parametrize('host', [
        "256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов "\
            "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов "\
                "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов S"
        "257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов "\
            "Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 "\
                "Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 С",
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов "\
            "Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov "\
                "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 "\
                    "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 "\
                        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov "\
                            "505 Символов Simvolov 505 Символов Simvolov",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_host(self, host, allure_attach_request_n_response_body):
        gen_data = EventGenerator(ip=host)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)

    @pytest.mark.parametrize('session_id', [
        "256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов "\
            "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов "\
                "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов S"
        "257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов "\
            "Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 "\
                "Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 С",
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов "\
            "Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov "\
                "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 "\
                    "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 "\
                        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov "\
                            "505 Символов Simvolov 505 Символов Simvolov",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_session_id(self, session_id, allure_attach_request_n_response_body):
        gen_data = EventGenerator(session_id=session_id)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        allure_attach_request_n_response_body(str(gen_data.get_dict_reg_event_adm()), admin_add.response.text)
        admin_add.check_status_code(400)