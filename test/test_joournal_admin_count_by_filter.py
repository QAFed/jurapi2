import pytest
from endpoints.journal_admin_count_by_filter import AdminCountByFilter
from generators.serial_send import SerialSender

class TestPosAdminCountByFilter:

    @pytest.mark.parametrize('event_time_from', [
        0,
        4294967295
    ])
    def test_gz_event_time_from(self, event_time_from, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'event_time_from': event_time_from})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)


    @pytest.mark.parametrize('event_time_to', [
        0,
        4294967295
    ])
    def test_gz_event_time_to(self, event_time_to, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'event_time_to': event_time_to})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

    @pytest.mark.parametrize('action_type',[
        -2147483647,
        0,
        2147483647
    ])
    def test_gz_action_type(self, action_type, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'action_type': action_type})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

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
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

    @pytest.mark.parametrize('sort_order', [
        "asc",
        "desc"
    ])
    def test_gz_sort_order(self, sort_order, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'sort_order': sort_order})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

    @pytest.mark.parametrize('admin_ids', [
        [-2147483647, 0, 2147483647],
        [-2147483647, -2147483647, -2147483647],
        [2147483647, 2147483647, 2147483647],
        [0, 0, 0],
        [1, 2, 3]
    ])
    def test_gz_admin_ids(self, admin_ids, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'admin_ids': admin_ids})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

    @pytest.mark.parametrize('session_id', [
        "",
        "1",
        "Aa",
        "100 символов stoSimvolov 10010010010010010010010101010101001010101010101  СТО 100 100 100 сто сто сто",
        "254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Simvols 254 Cимвола Si",
        "255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255 SIMvols Символов 255"
    ])
    def test_gz_session_id(self, session_id, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'session_id': session_id})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

    @pytest.mark.parametrize('sort_by', [
        "adminId",
        "time",
        "host",
        "sessionId"
    ])
    def test_gz_sort_by(self, sort_by, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm', ext_data={'sort_by': sort_by})
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        count_filter.send_request(serial_sender.payload_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

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
        count_iter = 5
        serial_sender.send_requests(count_iter)
        mod_diction = serial_sender.payload_filter
        mod_diction.pop(pop_param)
        count_filter = AdminCountByFilter()
        count_filter.send_request(mod_diction)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(200)
        count_filter.assert_count(count_iter)

class TestNegAdminCountByFilter:

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
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['eventTimeFrom'] = event_time_from
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

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
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['eventTimeTo'] = event_time_to
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

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
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['actionType'] = action_type
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

    @pytest.mark.parametrize('ip', [
        "256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов " \
        "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов " \
        "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов S"
        "257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов " \
        "Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 " \
        "Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 С",
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов " \
        "Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov " \
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 " \
        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 " \
        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov " \
        "505 Символов Simvolov 505 Символов Simvolov",
        {'slo': 'var'},
        ["spisok", 1],
        107,
        ""
    ])
    def test_status_code_400_gz_ip(self, ip, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['ip'] = ip
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

    @pytest.mark.parametrize('admin_ids', [
        [-2147483648, 2147483648],
        [-2147483648, -2147483648, -2147483648],
        [2147483648, 2147483648, 2147483648],
        [],
        [""],
        ['', ''],
        ["1", "2"],
        [1, ""],
        [[1, 2], [3, 4]],
        [[1]],
        [{2}],
        [{1: "dict"}, {"2": "dict2"}]
    ])
    def test_status_code_400_gz_admin_ids(self, admin_ids, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['adminIds'] = admin_ids
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

    @pytest.mark.parametrize('session_id', [
        "256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов " \
        "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов " \
        "Simvolov 256 Символов Simvolov 256 Символов Simvolov 256 Символов S"
        "257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов " \
        "Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 " \
        "Символов Simvolov257 Символов Simvolov257 Символов Simvolov257 С",
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов " \
        "Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov " \
        "505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 " \
        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 " \
        "Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov 505 Символов Simvolov " \
        "505 Символов Simvolov 505 Символов Simvolov",
        {'slo': 'var'},
        ["spisok", 1],
        107,
        ""
    ])
    def test_status_code_400_gz_session_id(self, session_id, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['sessionId'] = session_id
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)

    @pytest.mark.parametrize('sort_by', [
        107,
        "Cтрока Strora",
        {'slo': 'var'},
        ["spisok", 1],
        ""
    ])
    def test_status_code_400_gz_sort_order(self, sort_by, allure_attach_request_n_response_body):
        serial_sender = SerialSender('adm')
        count_iter = 5
        serial_sender.send_requests(count_iter)
        count_filter = AdminCountByFilter()
        mod_filter = serial_sender.payload_filter
        mod_filter['sortBy'] = sort_by
        count_filter.send_request(mod_filter)
        allure_attach_request_n_response_body(str(serial_sender.payload_filter), count_filter.response.text,
                                              status_code=count_filter.response.status_code)
        count_filter.check_status_code(400)