import requests
from assertpy import assert_that


def test_reject_friend_request_with_valid_credentials():
    param = {
        "requestor": "test2@mail.com",
        "to": "test1@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_without_credential_to():
    param = {
        "requestor": "test2@mail.com",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'FriendRequest.To' Error:Field validation for 'To' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_without_credential_requestor():
    param = {
        "requestor": "",
        "to": "test1@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'FriendRequest.Requestor' Error:Field validation for 'Requestor' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_without_validation_credentials():
    param = {
        "requestor": "",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'FriendRequest.Requestor' Error:Field validation for 'Requestor' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_invalid_credential_to():
    param = {

        "requestor": "test2@mail.com",
        "to": "zz@examp.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_invalid_credential_requestor():
    param = {
        "requestor": "aa@eba.com",
        "to": "test1@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_reject_friend_request_credential_requestor_Without_format_email():
    param = {

        "requestor": "test2",
        "to": "test1@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

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


def test_reject_friend_request_credential_to_Without_format_email():
    param = {

        "requestor": "test2@mail.com",
        "to": "test1"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

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


def test_reject_friend_request_Without_format_email():
    param = {

        "requestor": "test2",
        "to": "test1"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/reject", json=param)

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
