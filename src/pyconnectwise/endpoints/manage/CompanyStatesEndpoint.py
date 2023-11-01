from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyStatesCountEndpoint import (
    CompanyStatesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyStatesIdEndpoint import (
    CompanyStatesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyStatesInfoEndpoint import (
    CompanyStatesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import State
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyStatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[State], ConnectWiseManageRequestParams],
    IPostable[State, ConnectWiseManageRequestParams],
    IPaginateable[State, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "states", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[State])
        IPostable.__init__(self, State)
        IPaginateable.__init__(self, State)

        self.count = self._register_child_endpoint(
            CompanyStatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyStatesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyStatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyStatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyStatesIdEndpoint: The initialized CompanyStatesIdEndpoint object.
        """
        child = CompanyStatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[State]:
        """
        Performs a GET request against the /company/states endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[State]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            State,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[State]:
        """
        Performs a GET request against the /company/states endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[State]: The parsed response data.
        """
        return self._parse_many(
            State, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> State:
        """
        Performs a POST request against the /company/states endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            State: The parsed response data.
        """
        return self._parse_one(
            State, super()._make_request("POST", data=data, params=params).json()
        )
