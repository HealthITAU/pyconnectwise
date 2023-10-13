from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CampaignAudit
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class MarketingCampaignsIdAuditsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[CampaignAudit, ConnectWiseManageRequestParams],
    IPuttable[CampaignAudit, ConnectWiseManageRequestParams],
    IPatchable[CampaignAudit, ConnectWiseManageRequestParams],
    IPaginateable[CampaignAudit, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, CampaignAudit)
        IPuttable.__init__(self, CampaignAudit)
        IPatchable.__init__(self, CampaignAudit)
        IPaginateable.__init__(self, CampaignAudit)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CampaignAudit]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/audits/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignAudit]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CampaignAudit, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CampaignAudit:
        """
        Performs a GET request against the /marketing/campaigns/{id}/audits/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignAudit: The parsed response data.
        """
        return self._parse_one(CampaignAudit, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /marketing/campaigns/{id}/audits/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CampaignAudit:
        """
        Performs a PUT request against the /marketing/campaigns/{id}/audits/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignAudit: The parsed response data.
        """
        return self._parse_one(CampaignAudit, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> CampaignAudit:
        """
        Performs a PATCH request against the /marketing/campaigns/{id}/audits/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignAudit: The parsed response data.
        """
        return self._parse_one(CampaignAudit, super()._make_request("PATCH", data=data, params=params).json())
