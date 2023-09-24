from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsIdManagementproductsEndpoint import \
    CompanyManagementitsolutionsIdManagementproductsEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsIdUsagesEndpoint import \
    CompanyManagementitsolutionsIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ManagementItSolution
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyManagementitsolutionsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ManagementItSolution, ConnectWiseManageRequestParams],
    IPuttable[ManagementItSolution, ConnectWiseManageRequestParams],
    IPatchable[ManagementItSolution, ConnectWiseManageRequestParams],
    IPaginateable[ManagementItSolution, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.management_products = self._register_child_endpoint(
            CompanyManagementitsolutionsIdManagementproductsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            CompanyManagementitsolutionsIdUsagesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ManagementItSolution]:
        """
        Performs a GET request against the /company/managementItSolutions/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementItSolution]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementItSolution, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementItSolution:
        """
        Performs a GET request against the /company/managementItSolutions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolution: The parsed response data.
        """
        return self._parse_one(ManagementItSolution, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /company/managementItSolutions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementItSolution:
        """
        Performs a PUT request against the /company/managementItSolutions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolution: The parsed response data.
        """
        return self._parse_one(ManagementItSolution, super()._make_request("PUT", data=data, params=params).json())

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementItSolution:
        """
        Performs a PATCH request against the /company/managementItSolutions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolution: The parsed response data.
        """
        return self._parse_one(ManagementItSolution, super()._make_request("PATCH", data=data, params=params).json())
