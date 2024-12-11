from endpoints.journal_admin_get_by_filter import AdminGetByFilter

PAYLOAD = {
            'eventTimeFrom': 0,
            'eventTimeTo': 100,
            'actionType': 0,
            'ip': "192.168.111.111",
            'info': "1",
            'sortOrder': "asc",
            'adminIds': [7],
            'sessionId': "string123",
            'sortBy': "time"
}

PAGE_DATA = {
            'page': 0,
            'pageSize': 2
}

EXPECTED_LIST = [
    {
            'eventTypeId': 0,
            'ctime': 100,
            'extInfo': '1',
            'host': '192.168.111.111',
            'adminId': 7,
            'sessionId': 'string123'
    }
]
EXPECTED_LIST[0]["id"] = 324

get_by_filter = AdminGetByFilter()
get_by_filter.send_request(PAYLOAD, PAGE_DATA)
get_by_filter.compare_response(EXPECTED_LIST)

