from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechNetworkDevice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class NetworkdevicesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechNetworkDevice, ConnectWiseAutomateRequestParams],
    IPatchable[LabTechNetworkDevice, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechNetworkDevice, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, LabTechNetworkDevice)
        IPatchable.__init__(self, LabTechNetworkDevice)
        IPaginateable.__init__(self, LabTechNetworkDevice)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechNetworkDevice]:
        """
        Performs a GET request against the /Networkdevices/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechNetworkDevice]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechNetworkDevice,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechNetworkDevice:
        """
        Performs a GET request against the /Networkdevices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechNetworkDevice: The parsed response data.
        """
        return self._parse_one(
            LabTechNetworkDevice,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechNetworkDevice:
        """
        Performs a PATCH request against the /Networkdevices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechNetworkDevice: The parsed response data.
        """
        return self._parse_one(
            LabTechNetworkDevice,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
