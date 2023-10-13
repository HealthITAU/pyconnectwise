from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesQuotasCountEndpoint import SalesQuotasCountEndpoint
from pyconnectwise.endpoints.manage.SalesQuotasIdEndpoint import SalesQuotasIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import SalesQuota
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesQuotasEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SalesQuota], ConnectWiseManageRequestParams],
    IPostable[SalesQuota, ConnectWiseManageRequestParams],
    IPaginateable[SalesQuota, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "quotas", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SalesQuota])
        IPostable.__init__(self, SalesQuota)
        IPaginateable.__init__(self, SalesQuota)

        self.count = self._register_child_endpoint(SalesQuotasCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesQuotasIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesQuotasIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesQuotasIdEndpoint: The initialized SalesQuotasIdEndpoint object.
        """
        child = SalesQuotasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SalesQuota]:
        """
        Performs a GET request against the /sales/quotas endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesQuota]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), SalesQuota, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[SalesQuota]:
        """
        Performs a GET request against the /sales/quotas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesQuota]: The parsed response data.
        """
        return self._parse_many(SalesQuota, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SalesQuota:
        """
        Performs a POST request against the /sales/quotas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesQuota: The parsed response data.
        """
        return self._parse_one(SalesQuota, super()._make_request("POST", data=data, params=params).json())
