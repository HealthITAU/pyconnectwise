from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsCountEndpoint import (
    ProcurementWarehousebinsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdEndpoint import (
    ProcurementWarehousebinsIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsInfoEndpoint import (
    ProcurementWarehousebinsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import WarehouseBin
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementWarehousebinsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WarehouseBin], ConnectWiseManageRequestParams],
    IPostable[WarehouseBin, ConnectWiseManageRequestParams],
    IPaginateable[WarehouseBin, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "warehouseBins", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[WarehouseBin])
        IPostable.__init__(self, WarehouseBin)
        IPaginateable.__init__(self, WarehouseBin)

        self.count = self._register_child_endpoint(
            ProcurementWarehousebinsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementWarehousebinsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementWarehousebinsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementWarehousebinsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementWarehousebinsIdEndpoint: The initialized ProcurementWarehousebinsIdEndpoint object.
        """
        child = ProcurementWarehousebinsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WarehouseBin]:
        """
        Performs a GET request against the /procurement/warehouseBins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WarehouseBin]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WarehouseBin,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[WarehouseBin]:
        """
        Performs a GET request against the /procurement/warehouseBins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WarehouseBin]: The parsed response data.
        """
        return self._parse_many(
            WarehouseBin, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WarehouseBin:
        """
        Performs a POST request against the /procurement/warehouseBins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBin: The parsed response data.
        """
        return self._parse_one(
            WarehouseBin, super()._make_request("POST", data=data, params=params).json()
        )
