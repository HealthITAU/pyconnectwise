from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsIdDetailsCountEndpoint import (
    ProcurementAdjustmentsIdDetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsIdDetailsIdEndpoint import (
    ProcurementAdjustmentsIdDetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AdjustmentDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementAdjustmentsIdDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AdjustmentDetail], ConnectWiseManageRequestParams],
    IPostable[AdjustmentDetail, ConnectWiseManageRequestParams],
    IPaginateable[AdjustmentDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "details", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AdjustmentDetail])
        IPostable.__init__(self, AdjustmentDetail)
        IPaginateable.__init__(self, AdjustmentDetail)

        self.count = self._register_child_endpoint(
            ProcurementAdjustmentsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementAdjustmentsIdDetailsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementAdjustmentsIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementAdjustmentsIdDetailsIdEndpoint: The initialized ProcurementAdjustmentsIdDetailsIdEndpoint object.
        """
        child = ProcurementAdjustmentsIdDetailsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AdjustmentDetail]:
        """
        Performs a GET request against the /procurement/adjustments/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AdjustmentDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AdjustmentDetail]:
        """
        Performs a GET request against the /procurement/adjustments/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentDetail]: The parsed response data.
        """
        return self._parse_many(
            AdjustmentDetail,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AdjustmentDetail:
        """
        Performs a POST request against the /procurement/adjustments/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentDetail: The parsed response data.
        """
        return self._parse_one(
            AdjustmentDetail,
            super()._make_request("POST", data=data, params=params).json(),
        )
