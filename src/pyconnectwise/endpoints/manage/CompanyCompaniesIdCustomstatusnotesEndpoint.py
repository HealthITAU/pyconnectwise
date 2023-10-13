from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdCustomstatusnotesCountEndpoint import \
    CompanyCompaniesIdCustomstatusnotesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdCustomstatusnotesIdEndpoint import \
    CompanyCompaniesIdCustomstatusnotesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyCustomNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompaniesIdCustomstatusnotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyCustomNote], ConnectWiseManageRequestParams],
    IPostable[CompanyCustomNote, ConnectWiseManageRequestParams],
    IPaginateable[CompanyCustomNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "customStatusNotes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyCustomNote])
        IPostable.__init__(self, CompanyCustomNote)
        IPaginateable.__init__(self, CompanyCustomNote)

        self.count = self._register_child_endpoint(
            CompanyCompaniesIdCustomstatusnotesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesIdCustomstatusnotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdCustomstatusnotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdCustomstatusnotesIdEndpoint: The initialized CompanyCompaniesIdCustomstatusnotesIdEndpoint object.
        """
        child = CompanyCompaniesIdCustomstatusnotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyCustomNote]:
        """
        Performs a GET request against the /company/companies/{id}/customStatusNotes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyCustomNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyCustomNote, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyCustomNote]:
        """
        Performs a GET request against the /company/companies/{id}/customStatusNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyCustomNote]: The parsed response data.
        """
        return self._parse_many(CompanyCustomNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyCustomNote:
        """
        Performs a POST request against the /company/companies/{id}/customStatusNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyCustomNote: The parsed response data.
        """
        return self._parse_one(CompanyCustomNote, super()._make_request("POST", data=data, params=params).json())
