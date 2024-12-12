import random


class EventGenerator:
    def __init__(self, event_time_from=None, event_time_to=None, action_type=None, ip=None, info=None, sort_order=None,
                 admin_ids=None, session_id=None, sort_by=None, ctime=None):
        self.event_time_from = event_time_from or random.choice(range(0, 100))
        self.event_time_to = event_time_to or self.event_time_from + random.choice(range(1, 100))
        self.action_type = action_type or 1
        self.ip = ip or f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        self.info = info
        self.sort_order = sort_order or random.choice(["asc", "desc"])
        self.admin_ids = admin_ids or [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        self.session_id = session_id or random.choice(["string1", "string2"])
        self.sort_by = sort_by or random.choice(["adminId", "time", "host", "sessionId"])
        self.ctime = ctime

        for k, v in locals().items():
            if v == 0:
                setattr(self, k, 0)

    def get_dict_filter_adm(self):
        return {
            'eventTimeFrom': self.event_time_from,
            'eventTimeTo': self.event_time_to,
            'actionType': self.action_type,
            'ip': self.ip,
            'info': self.info,
            'sortOrder': self.sort_order,
            'adminIds': self.admin_ids,
            'sessionId': self.session_id,
            'sortBy': self.sort_by
                }

    def get_dict_reg_event_adm(self):
        return {
            "eventTypeId": self.action_type,
            "ctime": self.ctime if self.ctime is not None else random.choice(range(self.event_time_from, self.event_time_to + 1)),
            "extInfo": self.info,
            "host": self.ip,
            "adminId": random.choice(self.admin_ids),
            "sessionId": self.session_id
                }