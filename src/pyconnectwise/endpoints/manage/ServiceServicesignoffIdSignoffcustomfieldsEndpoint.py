from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffIdSignoffcustomfieldsCountEndpoint import \
    ServiceServicesignoffIdSignoffcustomfieldsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint import \
    ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint
from pyconnectwise.models.manage import ServiceSignoffCustomField
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceServicesignoffIdSignoffcustomfieldsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "signoffcustomfields", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceServicesignoffIdSignoffcustomfieldsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint: The initialized ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint object.
        """
        child = ServiceServicesignoffIdSignoffcustomfieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceSignoffCustomField]:
        """
        Performs a GET request against the /service/serviceSignoff/{id}/signoffcustomfields endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSignoffCustomField]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceSignoffCustomField, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceSignoffCustomField]:
        """
        Performs a GET request against the /service/serviceSignoff/{id}/signoffcustomfields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSignoffCustomField]: The parsed response data.
        """
        return self._parse_many(
            ServiceSignoffCustomField, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSignoffCustomField:
        """
        Performs a POST request against the /service/serviceSignoff/{id}/signoffcustomfields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSignoffCustomField: The parsed response data.
        """
        return self._parse_one(
            ServiceSignoffCustomField, super()._make_request("POST", data=data, params=params).json()
        )
