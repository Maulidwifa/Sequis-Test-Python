import requests
from assertpy import assert_that


def test_block_friend_with_valid_credentials():
    param = {
        "requestor": "mauld@mail.com",
        "to": "dafi@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_Without_credential_to():
    param = {
        "requestor": "mauld@mail.com",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_Without_credential_requestor():
    param = {
        "requestor": "",
        "to": "dafi@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Requestor' Error:Field validation for 'Requestor' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_Without_validation_credentials():
    param = {
        "requestor": "",
        "to": ""
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Requestor' Error:Field validation for 'Requestor' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_invalid_credential_to():
    param = {
        "requestor": "mauld@mail.com",
        "to": "qq@diable.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_invalid_credential_requestor():
    param = {
        "requestor": "mm@demble.com",
        "to": "dafi@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_credential_requestor_Without_format_email():
    param = {
        "requestor": "mauld",
        "to": "dafi@mail.com"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_credential_to_Without_format_email():
    param = {
        "requestor": "mauld@mail.com",
        "to": "dafi"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)


def test_block_a_friend_Without_format_email():
    param = {
        "requestor": "mauld",
        "to": "dafi"
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/block", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to(
        "Key: 'BlockRequest.Block' Error:Field validation for 'Block' failed on the 'required' tag")
    assert_that(resp_time).is_less_than(1000000)
