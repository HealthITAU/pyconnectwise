from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsCountEndpoint import (
    ProcurementPricingschedulesIdDetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdEndpoint import (
    ProcurementPricingschedulesIdDetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import PricingDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementPricingschedulesIdDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PricingDetail], ConnectWiseManageRequestParams],
    IPostable[PricingDetail, ConnectWiseManageRequestParams],
    IPaginateable[PricingDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "details", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PricingDetail])
        IPostable.__init__(self, PricingDetail)
        IPaginateable.__init__(self, PricingDetail)

        self.count = self._register_child_endpoint(
            ProcurementPricingschedulesIdDetailsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> ProcurementPricingschedulesIdDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdDetailsIdEndpoint: The initialized ProcurementPricingschedulesIdDetailsIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdDetailsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PricingDetail]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PricingDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PricingDetail]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingDetail]: The parsed response data.
        """
        return self._parse_many(
            PricingDetail, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PricingDetail:
        """
        Performs a POST request against the /procurement/pricingschedules/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingDetail: The parsed response data.
        """
        return self._parse_one(
            PricingDetail,
            super()._make_request("POST", data=data, params=params).json(),
        )
