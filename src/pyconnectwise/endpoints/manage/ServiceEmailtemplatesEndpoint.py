from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailtemplatesCountEndpoint import ServiceEmailtemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailtemplatesIdEndpoint import ServiceEmailtemplatesIdEndpoint
from pyconnectwise.models.manage import ServiceEmailTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailTemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceEmailtemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceEmailtemplatesIdEndpoint: The initialized ServiceEmailtemplatesIdEndpoint object.
        """
        child = ServiceEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceEmailTemplate]:
        """
        Performs a GET request against the /service/emailTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceEmailTemplate]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceEmailTemplate, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceEmailTemplate]:
        """
        Performs a GET request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceEmailTemplate]: The parsed response data.
        """
        return self._parse_many(ServiceEmailTemplate, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceEmailTemplate:
        """
        Performs a POST request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceEmailTemplate: The parsed response data.
        """
        return self._parse_one(ServiceEmailTemplate, super()._make_request("POST", data=data, params=params).json())
