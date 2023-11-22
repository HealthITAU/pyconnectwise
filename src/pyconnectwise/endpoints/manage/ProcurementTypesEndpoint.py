from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesCountEndpoint import ProcurementTypesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesIdEndpoint import ProcurementTypesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesInfoEndpoint import ProcurementTypesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ProductType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProductType], ConnectWiseManageRequestParams],
    IPostable[ProductType, ConnectWiseManageRequestParams],
    IPaginateable[ProductType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProductType])
        IPostable.__init__(self, ProductType)
        IPaginateable.__init__(self, ProductType)

        self.count = self._register_child_endpoint(ProcurementTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ProcurementTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementTypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementTypesIdEndpoint: The initialized ProcurementTypesIdEndpoint object.
        """
        child = ProcurementTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProductType]:
        """
        Performs a GET request against the /procurement/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ProductType]:
        """
        Performs a GET request against the /procurement/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductType]: The parsed response data.
        """
        return self._parse_many(ProductType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProductType:
        """
        Performs a POST request against the /procurement/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductType: The parsed response data.
        """
        return self._parse_one(ProductType, super()._make_request("POST", data=data, params=params).json())
