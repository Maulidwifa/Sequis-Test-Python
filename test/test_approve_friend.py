import requests
from assertpy import assert_that


def test_approve_a_friend_with_valid_credentials():
    param = {
        "requestor": "maulid@mail.com",
        "to": "fairuz@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_approve_a_friend_without_credential_to():
    param = {
        "requestor": "maulid@mail.com",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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


def test_approve_a_friend_without_credential_requestor():
    param = {
        "requestor": "",
        "to": "fairuz@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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


def test_approve_a_friend_without_validation_credentials():
    param = {
        "requestor": "",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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


def test_approve_a_friend_invalid_credential_to():
    param = {
        "requestor": "maulid@mail.com",
        "to": "exam@example.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_approve_a_friend_invalid_credential_requestor():
    param = {
        "requestor": "ex@example.com",
        "to": "fairus@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_time).is_less_than(1000000)


def test_approve_a_friend_credential_requestor_wrong_format_email():
    param = {
        "requestor": "maulid",
        "to": "fairuz@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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


def test_approve_a_friend_credential_to_wrong_format_email():
    param = {
        "requestor": "maulid@mail.com",
        "to": "fairuz"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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


def test_approve_a_friend_validation_without_format_email():
    param = {
        "requestor": "maulid",
        "to": "fairuz"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/approve", json=param)

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