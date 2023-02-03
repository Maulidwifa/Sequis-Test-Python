import requests
from assertpy import assert_that


def test_list_friend_with_valid_credentials():
    param = {
        "email": "test@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list", json=param)

    status_code = resp.status_code
    resp_json = resp.json().get("friends")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_json).is_type_of(list)
    assert_that(resp_time).is_less_than(1000000)


def test_list_a_friend_without_wrong_format_email():
    param = {
        "email": "test"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list", json=param)

    status_code = resp.status_code
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to("invalid email")
    assert_that(resp_time).is_less_than(1000000)


def test_list_a_friend_without_email_credentials():
    param = {
        "email": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list", json=param)

    status_code = resp.status_code
    resp_msg = resp.json().get("message")
    resp_scss = resp.json().get("success")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_scss).is_equal_to(False)
    assert_that(resp_err).is_equal_to(
        "Key: 'ListRequest.Email' Error:Field validation for 'Email' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_list_a_friend_without_invalid_email():
    param = {
        "email": "exam@example.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list", json=param)

    status_code = resp.status_code
    resp_friend = resp.json().get("friends")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(201)
    assert_that(resp_friend).is_none()
    assert_that(resp_time).is_less_than(1000000)
