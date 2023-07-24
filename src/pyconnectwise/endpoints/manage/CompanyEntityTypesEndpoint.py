from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesCountEndpoint import (
    CompanyEntitytypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdEndpoint import (
    CompanyEntitytypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyEntitytypesInfoEndpoint import (
    CompanyEntitytypesInfoEndpoint,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import EntityType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyEntitytypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entityTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyEntitytypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyEntitytypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyEntitytypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyEntitytypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyEntitytypesIdEndpoint: The initialized CompanyEntitytypesIdEndpoint object.
        """
        child = CompanyEntitytypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[EntityType]:
        """
        Performs a GET request against the /company/entityTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EntityType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            EntityType,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[EntityType]:
        """
        Performs a GET request against the /company/entityTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EntityType]: The parsed response data.
        """
        return self._parse_many(
            EntityType, super()._make_request("GET", data=data, params=params).json()
        )
