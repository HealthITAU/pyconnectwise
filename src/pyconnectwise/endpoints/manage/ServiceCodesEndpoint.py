from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceCodesCountEndpoint import ServiceCodesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceCodesIdEndpoint import ServiceCodesIdEndpoint
from pyconnectwise.models.manage import Code
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "codes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceCodesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceCodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceCodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceCodesIdEndpoint: The initialized ServiceCodesIdEndpoint object.
        """
        child = ServiceCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Code]:
        """
        Performs a GET request against the /service/codes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Code]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Code, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Code]:
        """
        Performs a GET request against the /service/codes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Code]: The parsed response data.
        """
        return self._parse_many(Code, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Code:
        """
        Performs a POST request against the /service/codes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Code: The parsed response data.
        """
        return self._parse_one(Code, super()._make_request("POST", data=data, params=params).json())
