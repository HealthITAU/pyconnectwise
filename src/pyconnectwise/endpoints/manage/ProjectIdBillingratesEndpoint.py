from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectIdBillingratesCountEndpoint import ProjectIdBillingratesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectIdBillingratesIdEndpoint import ProjectIdBillingratesIdEndpoint
from pyconnectwise.models.manage import ProjectBillingRate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectIdBillingratesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingRates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectIdBillingratesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectIdBillingratesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectIdBillingratesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectIdBillingratesIdEndpoint: The initialized ProjectIdBillingratesIdEndpoint object.
        """
        child = ProjectIdBillingratesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectBillingRate]:
        """
        Performs a GET request against the /project/{id}/billingRates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBillingRate]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectBillingRate, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectBillingRate]:
        """
        Performs a GET request against the /project/{id}/billingRates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBillingRate]: The parsed response data.
        """
        return self._parse_many(ProjectBillingRate, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBillingRate:
        """
        Performs a POST request against the /project/{id}/billingRates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBillingRate: The parsed response data.
        """
        return self._parse_one(ProjectBillingRate, super()._make_request("POST", data=data, params=params).json())
