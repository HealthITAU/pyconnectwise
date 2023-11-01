from typing import Any

from pyconnectwise.endpoints.automate.ComputersChassisEndpoint import (
    ComputersChassisEndpoint,
)
from pyconnectwise.endpoints.automate.ComputersDrivesEndpoint import (
    ComputersDrivesEndpoint,
)
from pyconnectwise.endpoints.automate.ComputersIdEndpoint import ComputersIdEndpoint
from pyconnectwise.endpoints.automate.ComputersMaintenancemodesEndpoint import (
    ComputersMaintenancemodesEndpoint,
)
from pyconnectwise.endpoints.automate.ComputersMemoryslotsEndpoint import (
    ComputersMemoryslotsEndpoint,
)
from pyconnectwise.endpoints.automate.ComputersSoftwareEndpoint import (
    ComputersSoftwareEndpoint,
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
from pyconnectwise.models.automate import LabTechComputer
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ComputersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputer], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputer, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Computers", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechComputer])
        IPaginateable.__init__(self, LabTechComputer)

        self.memoryslots = self._register_child_endpoint(
            ComputersMemoryslotsEndpoint(client, parent_endpoint=self)
        )
        self.software = self._register_child_endpoint(
            ComputersSoftwareEndpoint(client, parent_endpoint=self)
        )
        self.drives = self._register_child_endpoint(
            ComputersDrivesEndpoint(client, parent_endpoint=self)
        )
        self.chassis = self._register_child_endpoint(
            ComputersChassisEndpoint(client, parent_endpoint=self)
        )
        self.maintenancemodes = self._register_child_endpoint(
            ComputersMaintenancemodesEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ComputersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ComputersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ComputersIdEndpoint: The initialized ComputersIdEndpoint object.
        """
        child = ComputersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechComputer]:
        """
        Performs a GET request against the /Computers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputer]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputer,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechComputer]:
        """
        Performs a GET request against the /Computers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputer]: The parsed response data.
        """
        return self._parse_many(
            LabTechComputer,
            super()._make_request("GET", data=data, params=params).json(),
        )
