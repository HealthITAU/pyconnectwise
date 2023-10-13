from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsCountEndpoint import CompanyTracksIdActionsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsIdEndpoint import CompanyTracksIdActionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TrackAction
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyTracksIdActionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TrackAction], ConnectWiseManageRequestParams],
    IPostable[TrackAction, ConnectWiseManageRequestParams],
    IPaginateable[TrackAction, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "actions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TrackAction])
        IPostable.__init__(self, TrackAction)
        IPaginateable.__init__(self, TrackAction)

        self.count = self._register_child_endpoint(CompanyTracksIdActionsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyTracksIdActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTracksIdActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyTracksIdActionsIdEndpoint: The initialized CompanyTracksIdActionsIdEndpoint object.
        """
        child = CompanyTracksIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TrackAction]:
        """
        Performs a GET request against the /company/tracks/{id}/actions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TrackAction]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TrackAction, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TrackAction]:
        """
        Performs a GET request against the /company/tracks/{id}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TrackAction]: The parsed response data.
        """
        return self._parse_many(TrackAction, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TrackAction:
        """
        Performs a POST request against the /company/tracks/{id}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TrackAction: The parsed response data.
        """
        return self._parse_one(TrackAction, super()._make_request("POST", data=data, params=params).json())
