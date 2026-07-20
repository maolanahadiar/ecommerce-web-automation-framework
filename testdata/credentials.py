import pytest

VALID_CREDENTIALS = {
    "username": "redgery25",
    "password": "Testing123",
    "expected_message": "Welcome redgery25"
}

INVALID_CREDENTIALS = [
    pytest.param(
        {
            "case": "Wrong password",
            "username": "redgery25",
            "password": "drowssap_dilavni",
            "error_message": "Wrong password."
        },
        id = "wrong_password"
    ),
    pytest.param(
        {
            "case": "Empty username & password",
            "username": "",
            "password": "",
            "error_message": "Please fill out Username and Password."
        },
        id = "empty_username_and_password"
    ),
    pytest.param(
        {
            "case": "User doesn't exist",
            "username": "resu_dilavni",
            "password": "drowssap_dilavni",
            "error_message": "User does not exist."
        },
        id = "user_does_not_exist"
    )
]