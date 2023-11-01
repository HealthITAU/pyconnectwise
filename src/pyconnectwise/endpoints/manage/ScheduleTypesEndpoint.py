from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesCountEndpoint import (
    ScheduleTypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleTypesIdEndpoint import (
    ScheduleTypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleTypesInfoEndpoint import (
    ScheduleTypesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ScheduleType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleType], ConnectWiseManageRequestParams],
    IPostable[ScheduleType, ConnectWiseManageRequestParams],
    IPaginateable[ScheduleType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "types", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleType])
        IPostable.__init__(self, ScheduleType)
        IPaginateable.__init__(self, ScheduleType)

        self.count = self._register_child_endpoint(
            ScheduleTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ScheduleTypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScheduleTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleTypesIdEndpoint: The initialized ScheduleTypesIdEndpoint object.
        """
        child = ScheduleTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ScheduleType]:
        """
        Performs a GET request against the /schedule/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleType]:
        """
        Performs a GET request against the /schedule/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleType]: The parsed response data.
        """
        return self._parse_many(
            ScheduleType, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ScheduleType:
        """
        Performs a POST request against the /schedule/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleType: The parsed response data.
        """
        return self._parse_one(
            ScheduleType, super()._make_request("POST", data=data, params=params).json()
        )
