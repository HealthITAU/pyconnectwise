from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesCountEndpoint import ServiceSourcesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesIdEndpoint import ServiceSourcesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesInfoEndpoint import ServiceSourcesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Source
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceSourcesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Source], ConnectWiseManageRequestParams],
    IPostable[Source, ConnectWiseManageRequestParams],
    IPaginateable[Source, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sources", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceSourcesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceSourcesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSourcesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSourcesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSourcesIdEndpoint: The initialized ServiceSourcesIdEndpoint object.
        """
        child = ServiceSourcesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Source]:
        """
        Performs a GET request against the /service/sources endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Source]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Source, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Source]:
        """
        Performs a GET request against the /service/sources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Source]: The parsed response data.
        """
        return self._parse_many(Source, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Source:
        """
        Performs a POST request against the /service/sources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Source: The parsed response data.
        """
        return self._parse_one(Source, super()._make_request("POST", data=data, params=params).json())
