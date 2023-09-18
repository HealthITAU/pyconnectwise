from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesCountEndpoint import CompanyCommunicationtypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesIdEndpoint import CompanyCommunicationtypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesInfoEndpoint import CompanyCommunicationtypesInfoEndpoint
from pyconnectwise.models.manage import CommunicationType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCommunicationtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communicationTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyCommunicationtypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyCommunicationtypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCommunicationtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCommunicationtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCommunicationtypesIdEndpoint: The initialized CompanyCommunicationtypesIdEndpoint object.
        """
        child = CompanyCommunicationtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CommunicationType]:
        """
        Performs a GET request against the /company/communicationTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommunicationType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CommunicationType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CommunicationType]:
        """
        Performs a GET request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CommunicationType]: The parsed response data.
        """
        return self._parse_many(CommunicationType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CommunicationType:
        """
        Performs a POST request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationType: The parsed response data.
        """
        return self._parse_one(CommunicationType, super()._make_request("POST", data=data, params=params).json())
