from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCopyEndpoint import \
    SalesOpportunitiesIdForecastCopyEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCountEndpoint import \
    SalesOpportunitiesIdForecastCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastIdEndpoint import SalesOpportunitiesIdForecastIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Forecast
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesOpportunitiesIdForecastEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Forecast], ConnectWiseManageRequestParams],
    IPostable[Forecast, ConnectWiseManageRequestParams],
    IPaginateable[Forecast, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "forecast", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Forecast])
        IPostable.__init__(self, Forecast)
        IPaginateable.__init__(self, Forecast)

        self.copy = self._register_child_endpoint(
            SalesOpportunitiesIdForecastCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            SalesOpportunitiesIdForecastCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOpportunitiesIdForecastIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdForecastIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdForecastIdEndpoint: The initialized SalesOpportunitiesIdForecastIdEndpoint object.
        """
        child = SalesOpportunitiesIdForecastIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Forecast]:
        """
        Performs a GET request against the /sales/opportunities/{id}/forecast endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Forecast]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Forecast, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Forecast]:
        """
        Performs a GET request against the /sales/opportunities/{id}/forecast endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Forecast]: The parsed response data.
        """
        return self._parse_many(Forecast, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Forecast:
        """
        Performs a POST request against the /sales/opportunities/{id}/forecast endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Forecast: The parsed response data.
        """
        return self._parse_one(Forecast, super()._make_request("POST", data=data, params=params).json())
