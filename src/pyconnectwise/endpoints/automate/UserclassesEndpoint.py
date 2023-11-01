from pyconnectwise.endpoints.automate.UserclassesIdEndpoint import UserclassesIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import AutomateUserClass
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UserclassesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateUserClass], ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateUserClass, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Userclasses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutomateUserClass])
        IPaginateable.__init__(self, AutomateUserClass)

    def id(self, id: int) -> UserclassesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized UserclassesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            UserclassesIdEndpoint: The initialized UserclassesIdEndpoint object.
        """
        child = UserclassesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateUserClass]:
        """
        Performs a GET request against the /Userclasses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateUserClass]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateUserClass,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateUserClass]:
        """
        Performs a GET request against the /Userclasses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateUserClass]: The parsed response data.
        """
        return self._parse_many(
            AutomateUserClass,
            super()._make_request("GET", data=data, params=params).json(),
        )
