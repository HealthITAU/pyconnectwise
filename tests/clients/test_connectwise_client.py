import pytest
from requests.exceptions import Timeout
from requests_mock import Mocker as RequestMocker
from typing_extensions import override

from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config
from pyconnectwise.exceptions import ServerError


class FakeConnectWiseClient(ConnectWiseClient):
    def __init__(self, max_retries: int = 0) -> None:
        super().__init__()
        self.config = Config(max_retries=max_retries)

    @override
    def _get_headers(self) -> dict[str, str]:
        return {}

    @override
    def _get_url(self) -> str:
        raise NotImplementedError()


def test_one_timeout_500(requests_mock: RequestMocker):
    test_url = "https://staging.connectwisedev.com/v2022_2/apis/3.0/system/callbacks"

    # setup requests_mock to return one timeout from the ConnectWise API, and one
    # successful response.  We should get the successful response.

    requests_mock.get(
        test_url,
        [
            {
                "text": '{ "code": "ConnectWiseApi", "message": "A timeout has occured. Please try again."}',
                "status_code": 500,
                "reason": "A timeout has occured. Please try again",
            },
            {
                "text": "Success!",
            },
        ],
    )

    client = FakeConnectWiseClient(max_retries=1)
    response = client._make_request(
        "GET",
        test_url,
    )

    assert response.text == "Success!"
    # Initial try and 1 retry
    assert len(requests_mock.request_history) == 2


@pytest.mark.parametrize(
    "response_text, response_reason, expected_error, should_retry",
    [
        # Timeout errors should be retried, and then bubble up if they persist.
        (
            # Sometimes the ConnectWise API returns this type of timeout
            '{ "code": "ConnectWiseApi", "message": "A timeout has occured. Please try again."}',
            "A timeout has occured. Please try again",
            Timeout,
            True,
        ),
        (
            # Other times it's this timeout
            (
                '{ "code": "ConnectWiseApi", "message": "Timeout expired.  The timeout period elapsed prior to obtaining a'
                " connection from the pool.  This may have occurred because all pooled connections were in use and max"
                ' pool size was reached."}'
            ),
            "",  # I don't have record of what reason is returned with this error.
            Timeout,
            True,
        ),
        (
            # This error was caused by passing invalid data to the API (data has been
            # replaced by '...' in the message since it's unimportant to the test).
            # These errors should bubble-up to the caller without retry.
            '{\r\n  "code": "ConnectWiseApi",\r\n  "message": "Error converting value \\"{...}\\" to type \'...\'. Path \'...\', line 1, position 1."\r\n}',
            "Internal Server Error",
            ServerError,
            False,
        ),
    ],
)
def test_timeout_500(
    response_text: str,
    response_reason: str,
    expected_error: type[Exception],
    should_retry: bool,
    requests_mock: RequestMocker,
):
    test_url = "https://staging.connectwisedev.com/v2022_2/apis/3.0/system/callbacks"

    # Retrying once should be sufficient for testing purposes
    max_retries = 1

    # setup requests_mock to intercept the http requests
    requests_mock.get(
        test_url,
        text=response_text,
        reason=response_reason,
        status_code=500,
    )

    client = FakeConnectWiseClient(max_retries=max_retries)
    with pytest.raises(expected_error):
        client._make_request(
            "GET",
            test_url,
        )

    if should_retry:
        # The initial request, plus retries
        assert len(requests_mock.request_history) == 1 + max_retries
    else:
        assert len(requests_mock.request_history) == 1
