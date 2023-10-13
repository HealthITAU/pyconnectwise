from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyNotetypesCountEndpoint import CompanyNotetypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyNotetypesIdEndpoint import CompanyNotetypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyNotetypesInfoEndpoint import CompanyNotetypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyNoteType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyNotetypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyNoteType], ConnectWiseManageRequestParams],
    IPostable[CompanyNoteType, ConnectWiseManageRequestParams],
    IPaginateable[CompanyNoteType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "noteTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyNoteType])
        IPostable.__init__(self, CompanyNoteType)
        IPaginateable.__init__(self, CompanyNoteType)

        self.count = self._register_child_endpoint(CompanyNotetypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyNotetypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyNotetypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyNotetypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyNotetypesIdEndpoint: The initialized CompanyNotetypesIdEndpoint object.
        """
        child = CompanyNotetypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyNoteType]:
        """
        Performs a GET request against the /company/noteTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyNoteType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyNoteType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyNoteType]:
        """
        Performs a GET request against the /company/noteTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyNoteType]: The parsed response data.
        """
        return self._parse_many(CompanyNoteType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyNoteType:
        """
        Performs a POST request against the /company/noteTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyNoteType: The parsed response data.
        """
        return self._parse_one(CompanyNoteType, super()._make_request("POST", data=data, params=params).json())
