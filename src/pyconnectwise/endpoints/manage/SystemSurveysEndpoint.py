from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysCountEndpoint import (
    SystemSurveysCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSurveysIdEndpoint import (
    SystemSurveysIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSurveysInfoEndpoint import (
    SystemSurveysInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import Survey
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemSurveysEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Survey], ConnectWiseManageRequestParams],
    IPostable[Survey, ConnectWiseManageRequestParams],
    IPaginateable[Survey, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "surveys", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Survey])
        IPostable.__init__(self, Survey)
        IPaginateable.__init__(self, Survey)

        self.count = self._register_child_endpoint(
            SystemSurveysCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemSurveysInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemSurveysIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSurveysIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSurveysIdEndpoint: The initialized SystemSurveysIdEndpoint object.
        """
        child = SystemSurveysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Survey]:
        """
        Performs a GET request against the /system/surveys endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Survey]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Survey,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Survey]:
        """
        Performs a GET request against the /system/surveys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Survey]: The parsed response data.
        """
        return self._parse_many(
            Survey, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Survey:
        """
        Performs a POST request against the /system/surveys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_one(
            Survey, super()._make_request("POST", data=data, params=params).json()
        )
