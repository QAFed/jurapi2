import pytest
from endpoints.journal_admin_get_by_filter import AdminGetByFilter
from generators.serial_send import SerialSender


class TestPosAdminGetByFilter:

    @pytest.mark.parametrize('eventTimeFrom',[
        0,
        4294967295
    ])
    def test_gz_event_time_from(self, eventTimeFrom, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'event_time_from':eventTimeFrom})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('eventTimeTo', [
        0,
        4294967295
    ])
    def test_gz_event_time_to(self, eventTimeTo, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'event_time_to': eventTimeTo, 'event_time_from': 0})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)


    @pytest.mark.parametrize('actionType',[
        -2147483647,
        0,
        2147483647
    ])
    def test_gz_action_type(self, actionType, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'action_type': actionType})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('ip', [
        "",
        "1",
        "Aa",
        "100 символов stoSimvolov 10010010010010010010010101010101001010101010101  СТО 100 100 100 сто сто сто",
        "254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Si",
        "255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255"
    ])
    def test_gz_ip(self, ip, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'ip': ip})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('sortOrder', [
        "asc",
        "desc"
    ])
    def test_gz_sort_order(self, sortOrder, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'sort_order': sortOrder})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('adminIds', [
        [-2147483647, 0, 2147483647],
        [-2147483647, -2147483647, -2147483647],
        [2147483647, 2147483647, 2147483647],
        [0, 0, 0],
        [1, 2, 3]
    ])
    def test_gz_admin_ids(self, adminIds, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'admin_ids': adminIds})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('sessionId', [
        "",
        "1",
        "Aa",
        "100 символов stoSimvolov 10010010010010010010010101010101001010101010101  СТО 100 100 100 сто сто сто",
        "254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Si",
        "255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255"
    ])
    def test_gz_session_id(self, sessionId, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'session_id': sessionId})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('sort_by', [
        "adminId",
        "time",
        "host",
        "sessionId"
        ])
    def test_gz_sort_by(self, sort_by, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'sort_by': sort_by})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('page_num', [
        0,
        1,
        2
    ])
    def test_gz_page_num(self, page_num, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', page_params={'page': page_num, 'pageSize': 2})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('page_size', [
        1,
        2,
        3,
        10
    ])
    def test_gz_page_size(self, page_size, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', page_params={'page': 0, 'pageSize': page_size})
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

    @pytest.mark.parametrize('pop_param', [
        'eventTimeFrom',
        'eventTimeTo',
        'actionType',
        'ip',
        'info',
        'sortOrder',
        'adminIds',
        'sessionId'
    ])
    def test_status_code_200_if_one_param_not_send(self, pop_param, allure_attach_request_n_response_body,
                                                   before_n_after_clear_db):
        serial_sender = SerialSender('adm')
        serial_sender.send_requests(5)
        serial_sender.create_custom_page()
        get_by_filter = AdminGetByFilter()
        mod_diction = serial_sender.payload_filter
        mod_diction.pop(pop_param)
        get_by_filter.send_request(mod_diction, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(200)
        get_by_filter.compare_response(serial_sender.final_page)

class TestNegAdminGetByFilter:

    @pytest.mark.parametrize('event_time_from', [
        4294967296,
        104294967296,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_event_time_from(self, event_time_from, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        serial_sender.send_requests(5)
        get_by_filter = AdminGetByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['eventTimeFrom'] = event_time_from
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(400)

    @pytest.mark.parametrize('event_time_to', [
        4294967296,
        104294967296,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_event_time_to(self, event_time_to, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        serial_sender.send_requests(5)
        get_by_filter = AdminGetByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['eventTimeTo'] = event_time_to
        get_by_filter.send_request(serial_sender.payload_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(400)

    @pytest.mark.parametrize('action_type', [
        -2147483648,
        2147483648,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_action_type(self, action_type, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        serial_sender.send_requests(5)
        get_by_filter = AdminGetByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['actionType'] = action_type
        get_by_filter.send_request(mod_filter, serial_sender.page_params)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), get_by_filter.response.text,
                                              request_params=serial_sender.page_params,
                                              status_code=get_by_filter.response.status_code)
        get_by_filter.check_status_code(400)