from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesIdInfoEndpoint import (
    ProcurementSubcategoriesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesIdUsagesEndpoint import (
    ProcurementSubcategoriesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import SubCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementSubcategoriesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[SubCategory, ConnectWiseManageRequestParams],
    IPuttable[SubCategory, ConnectWiseManageRequestParams],
    IPatchable[SubCategory, ConnectWiseManageRequestParams],
    IPaginateable[SubCategory, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, SubCategory)
        IPuttable.__init__(self, SubCategory)
        IPatchable.__init__(self, SubCategory)
        IPaginateable.__init__(self, SubCategory)

        self.usages = self._register_child_endpoint(
            ProcurementSubcategoriesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementSubcategoriesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SubCategory]:
        """
        Performs a GET request against the /procurement/subcategories/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SubCategory]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SubCategory,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SubCategory:
        """
        Performs a GET request against the /procurement/subcategories/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SubCategory: The parsed response data.
        """
        return self._parse_one(
            SubCategory, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /procurement/subcategories/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SubCategory:
        """
        Performs a PUT request against the /procurement/subcategories/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SubCategory: The parsed response data.
        """
        return self._parse_one(
            SubCategory, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SubCategory:
        """
        Performs a PATCH request against the /procurement/subcategories/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SubCategory: The parsed response data.
        """
        return self._parse_one(
            SubCategory, super()._make_request("PATCH", data=data, params=params).json()
        )
