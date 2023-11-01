from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemKpicategoriesCountEndpoint import (
    SystemKpicategoriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemKpicategoriesIdEndpoint import (
    SystemKpicategoriesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import KPICategory
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemKpicategoriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[KPICategory], ConnectWiseManageRequestParams],
    IPaginateable[KPICategory, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "kpiCategories", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[KPICategory])
        IPaginateable.__init__(self, KPICategory)

        self.count = self._register_child_endpoint(
            SystemKpicategoriesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemKpicategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemKpicategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemKpicategoriesIdEndpoint: The initialized SystemKpicategoriesIdEndpoint object.
        """
        child = SystemKpicategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[KPICategory]:
        """
        Performs a GET request against the /system/kpiCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KPICategory]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            KPICategory,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[KPICategory]:
        """
        Performs a GET request against the /system/kpiCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KPICategory]: The parsed response data.
        """
        return self._parse_many(
            KPICategory, super()._make_request("GET", data=data, params=params).json()
        )
