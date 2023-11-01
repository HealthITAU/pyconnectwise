from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsIdInfoEndpoint import (
    CompanyContactsDepartmentsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsIdUsagesEndpoint import (
    CompanyContactsDepartmentsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ContactDepartment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyContactsDepartmentsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ContactDepartment, ConnectWiseManageRequestParams],
    IPuttable[ContactDepartment, ConnectWiseManageRequestParams],
    IPatchable[ContactDepartment, ConnectWiseManageRequestParams],
    IPaginateable[ContactDepartment, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ContactDepartment)
        IPuttable.__init__(self, ContactDepartment)
        IPatchable.__init__(self, ContactDepartment)
        IPaginateable.__init__(self, ContactDepartment)

        self.usages = self._register_child_endpoint(
            CompanyContactsDepartmentsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyContactsDepartmentsIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ContactDepartment]:
        """
        Performs a GET request against the /company/contacts/departments/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactDepartment]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactDepartment,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactDepartment:
        """
        Performs a GET request against the /company/contacts/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactDepartment: The parsed response data.
        """
        return self._parse_one(
            ContactDepartment,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /company/contacts/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactDepartment:
        """
        Performs a PUT request against the /company/contacts/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactDepartment: The parsed response data.
        """
        return self._parse_one(
            ContactDepartment,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactDepartment:
        """
        Performs a PATCH request against the /company/contacts/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactDepartment: The parsed response data.
        """
        return self._parse_one(
            ContactDepartment,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
