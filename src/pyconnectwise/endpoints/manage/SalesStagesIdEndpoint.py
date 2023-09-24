from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesStagesIdInfoEndpoint import SalesStagesIdInfoEndpoint
from pyconnectwise.endpoints.manage.SalesStagesIdUsagesEndpoint import SalesStagesIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import OpportunityStage
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesStagesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[OpportunityStage, ConnectWiseManageRequestParams],
    IPuttable[OpportunityStage, ConnectWiseManageRequestParams],
    IPatchable[OpportunityStage, ConnectWiseManageRequestParams],
    IPaginateable[OpportunityStage, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesStagesIdInfoEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(SalesStagesIdUsagesEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[OpportunityStage]:
        """
        Performs a GET request against the /sales/stages/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityStage]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityStage, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> OpportunityStage:
        """
        Performs a GET request against the /sales/stages/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStage: The parsed response data.
        """
        return self._parse_one(OpportunityStage, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /sales/stages/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> OpportunityStage:
        """
        Performs a PUT request against the /sales/stages/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStage: The parsed response data.
        """
        return self._parse_one(OpportunityStage, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> OpportunityStage:
        """
        Performs a PATCH request against the /sales/stages/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStage: The parsed response data.
        """
        return self._parse_one(OpportunityStage, super()._make_request("PATCH", data=data, params=params).json())
