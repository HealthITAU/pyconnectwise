from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdScheduledscriptsIdEndpoint import ComputersIdScheduledscriptsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechScheduledScript
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersIdScheduledscriptsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechScheduledScript], ConnectWiseAutomateRequestParams],
    IPostable[LabTechScheduledScript, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechScheduledScript, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Scheduledscripts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechScheduledScript])
        IPostable.__init__(self, LabTechScheduledScript)
        IPaginateable.__init__(self, LabTechScheduledScript)

    def id(self, id: int) -> ComputersIdScheduledscriptsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ComputersIdScheduledscriptsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ComputersIdScheduledscriptsIdEndpoint: The initialized ComputersIdScheduledscriptsIdEndpoint object.
        """
        child = ComputersIdScheduledscriptsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechScheduledScript]:
        """
        Performs a GET request against the /Computers/{id}/Scheduledscripts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechScheduledScript]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechScheduledScript, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechScheduledScript]:
        """
        Performs a GET request against the /Computers/{id}/Scheduledscripts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechScheduledScript]: The parsed response data.
        """
        return self._parse_many(LabTechScheduledScript, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechScheduledScript:
        """
        Performs a POST request against the /Computers/{id}/Scheduledscripts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechScheduledScript: The parsed response data.
        """
        return self._parse_one(LabTechScheduledScript, super()._make_request("POST", data=data, params=params).json())
