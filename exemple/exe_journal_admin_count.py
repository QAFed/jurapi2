from endpoints.journal_admin_count import AdminCountByFilter

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


count_by_filter = AdminCountByFilter()
count_by_filter.send_request(PAYLOAD)
count_by_filter.assert_count(2)