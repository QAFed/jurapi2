import pytest
from generators.event_generator import EventGenerator
from endpoints.journal_admin_add import AdminAdd

class TestPosAdminAdd:

    @pytest.mark.parametrize('eventTipeId',[
        -2147483647,
        0,
        2147483647,
    ])
    def test_gz_event_type_id(self, eventTipeId):
        gen_data = EventGenerator(action_type=eventTipeId)
        admin_add = AdminAdd()
        admin_add.send_request(gen_data.get_dict_reg_event_adm())
        admin_add.check_status_code(200)
        admin_add.compare_payload_n_response()




