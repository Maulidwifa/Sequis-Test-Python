import requests
from assertpy import assert_that


def test_check_list_common_with_valid_credentials():
    param = {
        "friends": [
            "maulid@mail.com",
            "testing@mail.com"
        ]
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/common", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_frn = resp.json().get("friends")["friends"]
    resp_cnt = resp.json().get("count")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(True)
    assert_that(resp_frn).is_type_of(list)
    assert_that(resp_cnt).is_type_of(int)
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_common_Without_validation_credentials_format_email():
    param = {
        "friends": [
            "maulid",
            "testing"
        ]
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/common", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_msg = resp.json().get("message")
    resp_err = resp.json().get("errors")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(400)
    assert_that(resp_scs).is_equal_to(False)
    assert_that(resp_msg).is_equal_to("Failed to process request")
    assert_that(resp_err).is_equal_to("please check the email list")
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_common_Without_validation_credentials():
    param = {
        "friends": [

        ]
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/common", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_frn = resp.json().get("friends")["friends"]
    resp_cnt = resp.json().get("count")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(True)
    assert_that(resp_frn).is_type_of(list)
    assert_that(resp_cnt).is_type_of(int)
    assert_that(resp_time).is_less_than(1000000)


def test_check_list_common_invalid_credentials():
    param = {
        "friends": [
            "maulid@xmpa.com",
            "qa@xampl.com"
        ]
    }
    resp = requests.post("http://13.229.247.215/api/v1/friend/list/common", json=param)

    status_code = resp.status_code
    resp_scs = resp.json().get("success")
    resp_frn = resp.json().get("friends")["friends"]
    resp_cnt = resp.json().get("count")
    resp_time = resp.elapsed.microseconds

    assert_that(status_code).is_equal_to(200)
    assert_that(resp_scs).is_equal_to(True)
    assert_that(resp_frn).is_type_of(list)
    assert_that(resp_cnt).is_type_of(int)
    assert_that(resp_time).is_less_than(1000000)
