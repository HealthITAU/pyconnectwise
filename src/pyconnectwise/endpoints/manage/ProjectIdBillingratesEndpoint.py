from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectIdBillingratesCountEndpoint import (
    ProjectIdBillingratesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProjectIdBillingratesIdEndpoint import (
    ProjectIdBillingratesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ProjectBillingRate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProjectIdBillingratesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectBillingRate], ConnectWiseManageRequestParams],
    IPostable[ProjectBillingRate, ConnectWiseManageRequestParams],
    IPaginateable[ProjectBillingRate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "billingRates", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectBillingRate])
        IPostable.__init__(self, ProjectBillingRate)
        IPaginateable.__init__(self, ProjectBillingRate)

        self.count = self._register_child_endpoint(ProjectIdBillingratesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectIdBillingratesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProjectIdBillingratesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectIdBillingratesIdEndpoint: The initialized ProjectIdBillingratesIdEndpoint object.
        """
        child = ProjectIdBillingratesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProjectBillingRate]:
        """
        Performs a GET request against the /project/{id}/billingRates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBillingRate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProjectBillingRate,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProjectBillingRate]:
        """
        Performs a GET request against the /project/{id}/billingRates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBillingRate]: The parsed response data.
        """
        return self._parse_many(
            ProjectBillingRate,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectBillingRate:
        """
        Performs a POST request against the /project/{id}/billingRates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBillingRate: The parsed response data.
        """
        return self._parse_one(
            ProjectBillingRate,
            super()._make_request("POST", data=data, params=params).json(),
        )
