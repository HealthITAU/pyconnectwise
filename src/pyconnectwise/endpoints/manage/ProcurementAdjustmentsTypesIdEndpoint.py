from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesIdInfoEndpoint import (
    ProcurementAdjustmentsTypesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesIdUsagesEndpoint import (
    ProcurementAdjustmentsTypesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import AdjustmentType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementAdjustmentsTypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[AdjustmentType, ConnectWiseManageRequestParams],
    IPuttable[AdjustmentType, ConnectWiseManageRequestParams],
    IPatchable[AdjustmentType, ConnectWiseManageRequestParams],
    IPaginateable[AdjustmentType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, AdjustmentType)
        IPuttable.__init__(self, AdjustmentType)
        IPatchable.__init__(self, AdjustmentType)
        IPaginateable.__init__(self, AdjustmentType)

        self.usages = self._register_child_endpoint(
            ProcurementAdjustmentsTypesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementAdjustmentsTypesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AdjustmentType]:
        """
        Performs a GET request against the /procurement/adjustments/types/{id} endpoint and returns an initialized PaginatedResponse object.

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
    ) -> AdjustmentType:
        """
        Performs a GET request against the /procurement/adjustments/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentType: The parsed response data.
        """
        return self._parse_one(
            AdjustmentType,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /procurement/adjustments/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AdjustmentType:
        """
        Performs a PUT request against the /procurement/adjustments/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentType: The parsed response data.
        """
        return self._parse_one(
            AdjustmentType,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AdjustmentType:
        """
        Performs a PATCH request against the /procurement/adjustments/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentType: The parsed response data.
        """
        return self._parse_one(
            AdjustmentType,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
