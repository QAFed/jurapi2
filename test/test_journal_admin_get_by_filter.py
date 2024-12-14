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

