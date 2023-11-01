from typing import Any

from pyconnectwise.endpoints.automate.NetworkdevicesIdEndpoint import (
    NetworkdevicesIdEndpoint,
)
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


class NetworkdevicesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechNetworkDevice], ConnectWiseAutomateRequestParams],
    IPostable[LabTechNetworkDevice, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechNetworkDevice, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Networkdevices", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechNetworkDevice])
        IPostable.__init__(self, LabTechNetworkDevice)
        IPaginateable.__init__(self, LabTechNetworkDevice)

    def id(self, id: int) -> NetworkdevicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized NetworkdevicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            NetworkdevicesIdEndpoint: The initialized NetworkdevicesIdEndpoint object.
        """
        child = NetworkdevicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechNetworkDevice]:
        """
        Performs a GET request against the /Networkdevices endpoint and returns an initialized PaginatedResponse object.

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
    ) -> list[LabTechNetworkDevice]:
        """
        Performs a GET request against the /Networkdevices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechNetworkDevice]: The parsed response data.
        """
        return self._parse_many(
            LabTechNetworkDevice,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechNetworkDevice:
        """
        Performs a POST request against the /Networkdevices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechNetworkDevice: The parsed response data.
        """
        return self._parse_one(
            LabTechNetworkDevice,
            super()._make_request("POST", data=data, params=params).json(),
        )
