from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsInfoCountEndpoint import \
    CompanyContactsDepartmentsInfoCountEndpoint
from pyconnectwise.models.manage import ContactDepartmentInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsDepartmentsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyContactsDepartmentsInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ContactDepartmentInfo]:
        """
        Performs a GET request against the /company/contacts/departments/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactDepartmentInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactDepartmentInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactDepartmentInfo]:
        """
        Performs a GET request against the /company/contacts/departments/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactDepartmentInfo]: The parsed response data.
        """
        return self._parse_many(ContactDepartmentInfo, super()._make_request("GET", data=data, params=params).json())
