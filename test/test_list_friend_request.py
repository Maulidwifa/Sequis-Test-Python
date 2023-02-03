import requests
from assertpy import assert_that


def test_check_list_friend_request_with_valid_credentials():
    param = {
        "email": "test2@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/request", json=param)

    status_code = resp.status_code
    resp_req = resp.json().get("requests")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_req).is_type_of(list)
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_friend_request_Without_validation_credentials_format_email():
    param = {
        "email": "test2"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/request", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to("invalid email")
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_friend_request_Without_email_credentials():
    param = {
        "email": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/request", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'ListRequest.Email' Error:Field validation for 'Email' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_friend_request_Without_invalid_email():
    param = {
        "email": "QA@exmpl.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/request", json=param)

    status_code = resp.status_code
    resp_req = resp.json().get("requests")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_req).is_none()
    assert_that(resp_time).is_less_than(1000000)