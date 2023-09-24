from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesCountEndpoint import ServicePrioritiesCountEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesIdEndpoint import ServicePrioritiesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Priority
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServicePrioritiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Priority], ConnectWiseManageRequestParams],
    IPostable[Priority, ConnectWiseManageRequestParams],
    IPaginateable[Priority, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServicePrioritiesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServicePrioritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServicePrioritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServicePrioritiesIdEndpoint: The initialized ServicePrioritiesIdEndpoint object.
        """
        child = ServicePrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Priority]:
        """
        Performs a GET request against the /service/priorities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Priority]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Priority, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Priority]:
        """
        Performs a GET request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Priority]: The parsed response data.
        """
        return self._parse_many(Priority, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Priority:
        """
        Performs a POST request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Priority: The parsed response data.
        """
        return self._parse_one(Priority, super()._make_request("POST", data=data, params=params).json())
