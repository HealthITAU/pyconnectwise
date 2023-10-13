from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesCountEndpoint import CompanyCompaniesIdNotesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesIdEndpoint import CompanyCompaniesIdNotesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompaniesIdNotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyNote], ConnectWiseManageRequestParams],
    IPostable[CompanyNote, ConnectWiseManageRequestParams],
    IPaginateable[CompanyNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyNote])
        IPostable.__init__(self, CompanyNote)
        IPaginateable.__init__(self, CompanyNote)

        self.count = self._register_child_endpoint(CompanyCompaniesIdNotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdNotesIdEndpoint: The initialized CompanyCompaniesIdNotesIdEndpoint object.
        """
        child = CompanyCompaniesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyNote]:
        """
        Performs a GET request against the /company/companies/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyNote, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CompanyNote]:
        """
        Performs a GET request against the /company/companies/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyNote]: The parsed response data.
        """
        return self._parse_many(CompanyNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyNote:
        """
        Performs a POST request against the /company/companies/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyNote: The parsed response data.
        """
        return self._parse_one(CompanyNote, super()._make_request("POST", data=data, params=params).json())
