from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContacttypeassociationsCountEndpoint import \
    CompanyContacttypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContacttypeassociationsIdEndpoint import \
    CompanyContacttypeassociationsIdEndpoint
from pyconnectwise.models.manage import CompanyContactTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContacttypeassociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contactTypeAssociations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyContacttypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContacttypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContacttypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContacttypeassociationsIdEndpoint: The initialized CompanyContacttypeassociationsIdEndpoint object.
        """
        child = CompanyContacttypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CompanyContactTypeAssociation]:
        """
        Performs a GET request against the /company/contactTypeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyContactTypeAssociation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyContactTypeAssociation, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyContactTypeAssociation]:
        """
        Performs a GET request against the /company/contactTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyContactTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            CompanyContactTypeAssociation, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyContactTypeAssociation:
        """
        Performs a POST request against the /company/contactTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyContactTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            CompanyContactTypeAssociation, super()._make_request("POST", data=data, params=params).json()
        )
