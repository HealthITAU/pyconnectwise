from __future__ import annotations
from requests import Response
from typing import Any
from typing import TypeVar, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient

TChildEndpoint = TypeVar("TChildEndpoint", bound="ConnectWiseEndpoint")
TSelf = TypeVar("TSelf", bound="ConnectWiseEndpoint")
T = TypeVar("T", bound="BaseModel")


class ConnectWiseEndpoint:
    """
    ConnectWiseEndpoint is a base class for all ConnectWise API endpoint classes.
    It provides a generic implementation for interacting with the ConnectWise API,
    handling requests, parsing responses into model instances, and managing pagination.

    ConnectWiseEndpoint makes use of a generic type variable TModel, which represents
    the expected ConnectWiseModel type for the endpoint. This allows for type-safe
    handling of model instances throughout the class.

    Each derived class should specify the ConnectWiseModel type it will be working with
    when inheriting from ConnectWiseEndpoint. For example:
    class CompanyEndpoint(ConnectWiseEndpoint[CompanyModel]).

    ConnectWiseEndpoint provides methods for making API requests and handles pagination
    using the PaginatedResponse class. By default, most CRUD methods raise a
    NotImplementedError, which should be overridden in derived classes to provide
    endpoint-specific implementations.

    ConnectWiseEndpoint also supports handling nested endpoints, which are referred to as
    child endpoints. Child endpoints can be registered and accessed through their parent
    endpoint, allowing for easy navigation through related resources in the API.

    Args:
        client: The ConnectWiseAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        parent_endpoint (ConnectWiseEndpoint, optional): The parent endpoint, if applicable.

    Attributes:
        client (ConnectWiseAPIClient): The ConnectWiseAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        _parent_endpoint (ConnectWiseEndpoint): The parent endpoint, if applicable.
        model_parser (ModelParser): An instance of the ModelParser class used for parsing API responses.
        _model (Type[TModel]): The model class for the endpoint.
        _id (int): The ID of the current resource, if applicable.
        _child_endpoints (List[ConnectWiseEndpoint]): A list of registered child endpoints.

    Generic Type:
        TModel: The model class for the endpoint.
    """

    def __init__(
        self,
        client: ConnectWiseClient,
        endpoint_url: str,
        parent_endpoint: ConnectWiseEndpoint | None = None,
    ):
        """
        Initialize a ConnectWiseEndpoint instance with the client and endpoint base.

        Args:
            client: The ConnectWiseAPIClient instance.
            endpoint_base (str): The base URL for the specific endpoint.
        """
        self.client = client
        self.endpoint_base = endpoint_url
        self._parent_endpoint = parent_endpoint
        self._id = None
        self._child_endpoints: list[ConnectWiseEndpoint] = []

    def _register_child_endpoint(
        self, child_endpoint: TChildEndpoint
    ) -> TChildEndpoint:
        """
        Register a child endpoint to the current endpoint.

        Args:
            child_endpoint (ConnectWiseEndpoint): The child endpoint instance.

        Returns:
            ConnectWiseEndpoint: The registered child endpoint.
        """
        self._child_endpoints.append(child_endpoint)
        return child_endpoint

    def _url_join(self, *args) -> str:
        """
        Join URL parts into a single URL string.

        Args:
            *args: The URL parts to join.

        Returns:
            str: The joined URL string.
        """
        url_parts = [str(arg).strip("/") for arg in args]
        return "/".join(url_parts)

    def _get_replaced_url(self) -> str:
        if self._id is None:
            return self.endpoint_base
        return self.endpoint_base.replace("{id}", str(self._id))

    def _make_request(
        self,
        method: str,
        endpoint: 'ConnectWiseEndpoint' = None,
        data: dict[str, Any] = None,
        params: dict[str, int | str] = None,
        headers: dict[str, str] = None,
    ) -> Response:
        """
        Make an API request using the specified method, endpoint, data, and parameters.
        This function isn't intended for use outside of this class.
        Please use the available CRUD methods as intended.

        Args:
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, etc.).
            endpoint (str, optional): The endpoint to make the request to.
            data (dict, optional): The request data to send.
            params (dict, optional): The query parameters to include in the request.

        Returns:
            The Response object (see requests.Response).

        Raises:
            Exception: If the request returns a status code >= 400.
        """

        def build_url(other_endpoint: ConnectWiseEndpoint) -> str:
            if other_endpoint._parent_endpoint is not None:
                parent_url = build_url(other_endpoint._parent_endpoint)
                if other_endpoint._parent_endpoint._id is not None:
                    return self._url_join(
                        parent_url,
                        other_endpoint._get_replaced_url(),
                    )
                else:
                    return self._url_join(parent_url, other_endpoint._get_replaced_url())
            else:
                return self._url_join(
                    self.client._get_url(), other_endpoint._get_replaced_url()
                )

        url = build_url(self)
        if endpoint:
            url = self._url_join(url, endpoint)

        return self.client._make_request(method, url, data, params, headers)

    def _parse_many(self, model_type: Type[T], data: list[dict[str, Any]]) -> list[T]:
        return [model_type.model_validate(d) for d in data]

    def _parse_one(self, model_type: Type[T], data: dict[str, Any]) -> T:
        return model_type.model_validate(data)
