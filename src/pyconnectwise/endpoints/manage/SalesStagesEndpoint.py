from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesStagesCountEndpoint import SalesStagesCountEndpoint
from pyconnectwise.endpoints.manage.SalesStagesIdEndpoint import SalesStagesIdEndpoint
from pyconnectwise.endpoints.manage.SalesStagesInfoEndpoint import SalesStagesInfoEndpoint
from pyconnectwise.models.manage import OpportunityStage
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesStagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "stages", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesStagesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesStagesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesStagesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesStagesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesStagesIdEndpoint: The initialized SalesStagesIdEndpoint object.
        """
        child = SalesStagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityStage]:
        """
        Performs a GET request against the /sales/stages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityStage]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityStage, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityStage]:
        """
        Performs a GET request against the /sales/stages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityStage]: The parsed response data.
        """
        return self._parse_many(OpportunityStage, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityStage:
        """
        Performs a POST request against the /sales/stages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStage: The parsed response data.
        """
        return self._parse_one(OpportunityStage, super()._make_request("POST", data=data, params=params).json())
