class MalformedRequestException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 400 (Bad Request) error has occurred while making a request to the API. The request could not be understood by the server due to malformed syntax. Please check modify your request before retrying. The original message was: {message}"
        )


class AuthenticationFailedException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 401 (Unauthorized) error has occurred while making a request to the API. Please check your credentials are correct before retrying. The original message was: {message}"
        )


class PermissionsFailedException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 403 (Forbidden) error has occurred while making a request to the API. You may be attempting to access a resource you do not have the appropriate permissions for. The original message was: {message}"
        )


class NotFoundException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 404 (Not Found) error has occurred while making a request to the API. You may be attempting to access a resource that has been moved or deleted. The original message was: {message}"
        )


class MethodNotAllowedException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 405 (Method Not Allowed) error has occurred while making a request to the API. This resource does not support the HTTP method you are trying to use. The original message was: {message}"
        )


class ConflictException(Exception):
    def __init__(
        self,
        message,
    ):
        super().__init__(
            f"A HTTP 409 (Conflict) error has occurred while making a request to the API. This resource is possibly in use or conflicts with another record. The original message was: {message}"
        )