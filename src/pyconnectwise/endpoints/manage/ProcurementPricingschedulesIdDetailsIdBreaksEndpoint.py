from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint import \
    ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint import \
    ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import PricingBreak
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementPricingschedulesIdDetailsIdBreaksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PricingBreak], ConnectWiseManageRequestParams],
    IPostable[PricingBreak, ConnectWiseManageRequestParams],
    IPaginateable[PricingBreak, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "breaks", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[PricingBreak])
        IPostable.__init__(self, PricingBreak)
        IPaginateable.__init__(self, PricingBreak)

        self.count = self._register_child_endpoint(
            ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint: The initialized ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PricingBreak]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details/{id}/breaks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingBreak]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), PricingBreak, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[PricingBreak]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details/{id}/breaks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingBreak]: The parsed response data.
        """
        return self._parse_many(PricingBreak, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> PricingBreak:
        """
        Performs a POST request against the /procurement/pricingschedules/{id}/details/{id}/breaks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingBreak: The parsed response data.
        """
        return self._parse_one(PricingBreak, super()._make_request("POST", data=data, params=params).json())
