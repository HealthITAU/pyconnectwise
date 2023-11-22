from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import RmaStatusEmailTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementRmastatusesIdEmailtemplatesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[RmaStatusEmailTemplate, ConnectWiseManageRequestParams],
    IPatchable[RmaStatusEmailTemplate, ConnectWiseManageRequestParams],
    IPuttable[RmaStatusEmailTemplate, ConnectWiseManageRequestParams],
    IPaginateable[RmaStatusEmailTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, RmaStatusEmailTemplate)
        IPatchable.__init__(self, RmaStatusEmailTemplate)
        IPuttable.__init__(self, RmaStatusEmailTemplate)
        IPaginateable.__init__(self, RmaStatusEmailTemplate)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[RmaStatusEmailTemplate]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id}/emailtemplates/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatusEmailTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), RmaStatusEmailTemplate, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /procurement/rmaStatuses/{id}/emailtemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> RmaStatusEmailTemplate:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id}/emailtemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatusEmailTemplate: The parsed response data.
        """
        return self._parse_one(RmaStatusEmailTemplate, super()._make_request("GET", data=data, params=params).json())

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> RmaStatusEmailTemplate:
        """
        Performs a PATCH request against the /procurement/rmaStatuses/{id}/emailtemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatusEmailTemplate: The parsed response data.
        """
        return self._parse_one(RmaStatusEmailTemplate, super()._make_request("PATCH", data=data, params=params).json())

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> RmaStatusEmailTemplate:
        """
        Performs a PUT request against the /procurement/rmaStatuses/{id}/emailtemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatusEmailTemplate: The parsed response data.
        """
        return self._parse_one(RmaStatusEmailTemplate, super()._make_request("PUT", data=data, params=params).json())
