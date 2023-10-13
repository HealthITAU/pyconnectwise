from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffCountEndpoint import ServiceServicesignoffCountEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffIdEndpoint import ServiceServicesignoffIdEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffInfoEndpoint import ServiceServicesignoffInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ServiceSignoff
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceServicesignoffEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceSignoff], ConnectWiseManageRequestParams],
    IPostable[ServiceSignoff, ConnectWiseManageRequestParams],
    IPaginateable[ServiceSignoff, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "serviceSignoff", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceSignoff])
        IPostable.__init__(self, ServiceSignoff)
        IPaginateable.__init__(self, ServiceSignoff)

        self.count = self._register_child_endpoint(ServiceServicesignoffCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceServicesignoffInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceServicesignoffIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceServicesignoffIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceServicesignoffIdEndpoint: The initialized ServiceServicesignoffIdEndpoint object.
        """
        child = ServiceServicesignoffIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceSignoff]:
        """
        Performs a GET request against the /service/serviceSignoff endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSignoff]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceSignoff, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ServiceSignoff]:
        """
        Performs a GET request against the /service/serviceSignoff endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSignoff]: The parsed response data.
        """
        return self._parse_many(ServiceSignoff, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ServiceSignoff:
        """
        Performs a POST request against the /service/serviceSignoff endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSignoff: The parsed response data.
        """
        return self._parse_one(ServiceSignoff, super()._make_request("POST", data=data, params=params).json())
