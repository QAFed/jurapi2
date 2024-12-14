import allure
import pytest


@pytest.fixture
def allure_attach_request_n_response_body():
    def _attach(request_body, response_body):
        allure.attach(request_body, name="request dody", attachment_type=allure.attachment_type.JSON)
        allure.attach(response_body, name="response dody", attachment_type=allure.attachment_type.JSON)
    return _attach