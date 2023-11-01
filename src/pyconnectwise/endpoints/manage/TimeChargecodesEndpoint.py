from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesCountEndpoint import (
    TimeChargecodesCountEndpoint,
)
from pyconnectwise.endpoints.manage.TimeChargecodesIdEndpoint import (
    TimeChargecodesIdEndpoint,
)
from pyconnectwise.endpoints.manage.TimeChargecodesInfoEndpoint import (
    TimeChargecodesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ChargeCode
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class TimeChargecodesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ChargeCode], ConnectWiseManageRequestParams],
    IPostable[ChargeCode, ConnectWiseManageRequestParams],
    IPaginateable[ChargeCode, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "chargeCodes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ChargeCode])
        IPostable.__init__(self, ChargeCode)
        IPaginateable.__init__(self, ChargeCode)

        self.count = self._register_child_endpoint(
            TimeChargecodesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            TimeChargecodesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> TimeChargecodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeChargecodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeChargecodesIdEndpoint: The initialized TimeChargecodesIdEndpoint object.
        """
        child = TimeChargecodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ChargeCode]:
        """
        Performs a GET request against the /time/chargeCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCode]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ChargeCode,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ChargeCode]:
        """
        Performs a GET request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCode]: The parsed response data.
        """
        return self._parse_many(
            ChargeCode, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ChargeCode:
        """
        Performs a POST request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChargeCode: The parsed response data.
        """
        return self._parse_one(
            ChargeCode, super()._make_request("POST", data=data, params=params).json()
        )
