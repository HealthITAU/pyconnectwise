from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesCountEndpoint import SalesActivitiesTypesCountEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesIdEndpoint import SalesActivitiesTypesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ActivityType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesActivitiesTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ActivityType], ConnectWiseManageRequestParams],
    IPostable[ActivityType, ConnectWiseManageRequestParams],
    IPaginateable[ActivityType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ActivityType])
        IPostable.__init__(self, ActivityType)
        IPaginateable.__init__(self, ActivityType)

        self.count = self._register_child_endpoint(SalesActivitiesTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesActivitiesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesActivitiesTypesIdEndpoint: The initialized SalesActivitiesTypesIdEndpoint object.
        """
        child = SalesActivitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ActivityType]:
        """
        Performs a GET request against the /sales/activities/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ActivityType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ActivityType]:
        """
        Performs a GET request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityType]: The parsed response data.
        """
        return self._parse_many(ActivityType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ActivityType:
        """
        Performs a POST request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityType: The parsed response data.
        """
        return self._parse_one(ActivityType, super()._make_request("POST", data=data, params=params).json())
