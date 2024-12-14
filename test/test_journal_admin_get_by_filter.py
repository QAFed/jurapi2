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





