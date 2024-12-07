from endpoints.journal_admin_add import AdminAdd

PAYLOAD = {
            "eventTypeId": 0,
            "ctime": 100,
            "extInfo": 1,
            "host": "192.168.111.111",
            "adminId": 7,
            "sessionId": "string123"
            }

add_admin_event = AdminAdd()
add_admin_event.send_request(PAYLOAD)
add_admin_event.check_status_code(400)
add_admin_event.assert_payload_n_response()
