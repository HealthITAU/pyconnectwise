from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesCountEndpoint import (
    ProcurementPricingschedulesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdEndpoint import (
    ProcurementPricingschedulesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import PricingSchedule
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementPricingschedulesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PricingSchedule], ConnectWiseManageRequestParams],
    IPostable[PricingSchedule, ConnectWiseManageRequestParams],
    IPaginateable[PricingSchedule, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "pricingschedules", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PricingSchedule])
        IPostable.__init__(self, PricingSchedule)
        IPaginateable.__init__(self, PricingSchedule)

        self.count = self._register_child_endpoint(
            ProcurementPricingschedulesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPricingschedulesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdEndpoint: The initialized ProcurementPricingschedulesIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PricingSchedule]:
        """
        Performs a GET request against the /procurement/pricingschedules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingSchedule]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PricingSchedule,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PricingSchedule]:
        """
        Performs a GET request against the /procurement/pricingschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingSchedule]: The parsed response data.
        """
        return self._parse_many(
            PricingSchedule,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PricingSchedule:
        """
        Performs a POST request against the /procurement/pricingschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingSchedule: The parsed response data.
        """
        return self._parse_one(
            PricingSchedule,
            super()._make_request("POST", data=data, params=params).json(),
        )
