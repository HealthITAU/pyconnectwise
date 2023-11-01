from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesCountEndpoint import (
    ProcurementAdjustmentsTypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesIdEndpoint import (
    ProcurementAdjustmentsTypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesInfoEndpoint import (
    ProcurementAdjustmentsTypesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AdjustmentType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementAdjustmentsTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AdjustmentType], ConnectWiseManageRequestParams],
    IPostable[AdjustmentType, ConnectWiseManageRequestParams],
    IPaginateable[AdjustmentType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "types", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AdjustmentType])
        IPostable.__init__(self, AdjustmentType)
        IPaginateable.__init__(self, AdjustmentType)

        self.count = self._register_child_endpoint(
            ProcurementAdjustmentsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementAdjustmentsTypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementAdjustmentsTypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementAdjustmentsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementAdjustmentsTypesIdEndpoint: The initialized ProcurementAdjustmentsTypesIdEndpoint object.
        """
        child = ProcurementAdjustmentsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AdjustmentType]:
        """
        Performs a GET request against the /procurement/adjustments/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AdjustmentType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AdjustmentType]:
        """
        Performs a GET request against the /procurement/adjustments/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentType]: The parsed response data.
        """
        return self._parse_many(
            AdjustmentType,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AdjustmentType:
        """
        Performs a POST request against the /procurement/adjustments/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentType: The parsed response data.
        """
        return self._parse_one(
            AdjustmentType,
            super()._make_request("POST", data=data, params=params).json(),
        )
