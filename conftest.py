import json

import allure
import pytest


@pytest.fixture
def allure_attach_request_n_response_body():
    def _attach(request_body, response_body, request_params=None, status_code=None):
        if request_params:
            allure.attach(json.dumps(request_params), name="request params", attachment_type=allure.attachment_type.JSON)
        allure.attach(request_body, name="request dody", attachment_type=allure.attachment_type.JSON)
        if status_code:
            allure.attach(str(status_code), name="status code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response_body, name="response dody", attachment_type=allure.attachment_type.JSON)

    return _attach