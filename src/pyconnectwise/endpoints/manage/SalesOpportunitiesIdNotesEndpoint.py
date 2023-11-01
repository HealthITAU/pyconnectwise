from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdNotesCountEndpoint import (
    SalesOpportunitiesIdNotesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdNotesIdEndpoint import (
    SalesOpportunitiesIdNotesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import OpportunityNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SalesOpportunitiesIdNotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OpportunityNote], ConnectWiseManageRequestParams],
    IPostable[OpportunityNote, ConnectWiseManageRequestParams],
    IPaginateable[OpportunityNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "notes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[OpportunityNote])
        IPostable.__init__(self, OpportunityNote)
        IPaginateable.__init__(self, OpportunityNote)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesIdNotesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOpportunitiesIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdNotesIdEndpoint: The initialized SalesOpportunitiesIdNotesIdEndpoint object.
        """
        child = SalesOpportunitiesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[OpportunityNote]:
        """
        Performs a GET request against the /sales/opportunities/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OpportunityNote,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[OpportunityNote]:
        """
        Performs a GET request against the /sales/opportunities/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityNote]: The parsed response data.
        """
        return self._parse_many(
            OpportunityNote,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> OpportunityNote:
        """
        Performs a POST request against the /sales/opportunities/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityNote: The parsed response data.
        """
        return self._parse_one(
            OpportunityNote,
            super()._make_request("POST", data=data, params=params).json(),
        )
