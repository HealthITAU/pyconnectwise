from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresIdConversionsCountEndpoint import (
    ProcurementUnitofmeasuresIdConversionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresIdConversionsIdEndpoint import (
    ProcurementUnitofmeasuresIdConversionsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Conversion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementUnitofmeasuresIdConversionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Conversion], ConnectWiseManageRequestParams],
    IPostable[Conversion, ConnectWiseManageRequestParams],
    IPaginateable[Conversion, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "conversions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Conversion])
        IPostable.__init__(self, Conversion)
        IPaginateable.__init__(self, Conversion)

        self.count = self._register_child_endpoint(
            ProcurementUnitofmeasuresIdConversionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ProcurementUnitofmeasuresIdConversionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementUnitofmeasuresIdConversionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementUnitofmeasuresIdConversionsIdEndpoint: The initialized ProcurementUnitofmeasuresIdConversionsIdEndpoint object.
        """
        child = ProcurementUnitofmeasuresIdConversionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Conversion]:
        """
        Performs a GET request against the /procurement/unitOfMeasures/{id}/conversions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Conversion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Conversion, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Conversion]:
        """
        Performs a GET request against the /procurement/unitOfMeasures/{id}/conversions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Conversion]: The parsed response data.
        """
        return self._parse_many(Conversion, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Conversion:
        """
        Performs a POST request against the /procurement/unitOfMeasures/{id}/conversions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Conversion: The parsed response data.
        """
        return self._parse_one(Conversion, super()._make_request("POST", data=data, params=params).json())
