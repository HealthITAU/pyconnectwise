from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersCountEndpoint import ProcurementManufacturersCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersIdEndpoint import ProcurementManufacturersIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersInfoEndpoint import ProcurementManufacturersInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Manufacturer
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementManufacturersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Manufacturer], ConnectWiseManageRequestParams],
    IPostable[Manufacturer, ConnectWiseManageRequestParams],
    IPaginateable[Manufacturer, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "manufacturers", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Manufacturer])
        IPostable.__init__(self, Manufacturer)
        IPaginateable.__init__(self, Manufacturer)

        self.count = self._register_child_endpoint(ProcurementManufacturersCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementManufacturersInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementManufacturersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementManufacturersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementManufacturersIdEndpoint: The initialized ProcurementManufacturersIdEndpoint object.
        """
        child = ProcurementManufacturersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Manufacturer]:
        """
        Performs a GET request against the /procurement/manufacturers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Manufacturer]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), Manufacturer, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Manufacturer]:
        """
        Performs a GET request against the /procurement/manufacturers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Manufacturer]: The parsed response data.
        """
        return self._parse_many(Manufacturer, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Manufacturer:
        """
        Performs a POST request against the /procurement/manufacturers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Manufacturer: The parsed response data.
        """
        return self._parse_one(Manufacturer, super()._make_request("POST", data=data, params=params).json())
