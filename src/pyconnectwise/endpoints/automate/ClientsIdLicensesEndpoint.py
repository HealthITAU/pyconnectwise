from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechManagedLicense
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ClientsIdLicensesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechManagedLicense], ConnectWiseAutomateRequestParams],
    IPostable[LabTechManagedLicense, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechManagedLicense, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Licenses", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechManagedLicense])
        IPostable.__init__(self, LabTechManagedLicense)
        IPaginateable.__init__(self, LabTechManagedLicense)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechManagedLicense]:
        """
        Performs a GET request against the /Clients/{id}/Licenses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechManagedLicense]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechManagedLicense, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechManagedLicense]:
        """
        Performs a GET request against the /Clients/{id}/Licenses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechManagedLicense]: The parsed response data.
        """
        return self._parse_many(LabTechManagedLicense, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechManagedLicense:
        """
        Performs a POST request against the /Clients/{id}/Licenses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechManagedLicense: The parsed response data.
        """
        return self._parse_one(LabTechManagedLicense, super()._make_request("POST", data=data, params=params).json())
