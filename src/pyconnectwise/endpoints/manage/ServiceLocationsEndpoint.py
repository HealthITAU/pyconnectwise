from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsCountEndpoint import ServiceLocationsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsIdEndpoint import ServiceLocationsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsInfoEndpoint import ServiceLocationsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ServiceLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceLocationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceLocation], ConnectWiseManageRequestParams],
    IPostable[ServiceLocation, ConnectWiseManageRequestParams],
    IPaginateable[ServiceLocation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "locations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceLocation])
        IPostable.__init__(self, ServiceLocation)
        IPaginateable.__init__(self, ServiceLocation)

        self.count = self._register_child_endpoint(ServiceLocationsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceLocationsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceLocationsIdEndpoint: The initialized ServiceLocationsIdEndpoint object.
        """
        child = ServiceLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceLocation]:
        """
        Performs a GET request against the /service/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceLocation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceLocation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ServiceLocation]:
        """
        Performs a GET request against the /service/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceLocation]: The parsed response data.
        """
        return self._parse_many(ServiceLocation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ServiceLocation:
        """
        Performs a POST request against the /service/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceLocation: The parsed response data.
        """
        return self._parse_one(ServiceLocation, super()._make_request("POST", data=data, params=params).json())
