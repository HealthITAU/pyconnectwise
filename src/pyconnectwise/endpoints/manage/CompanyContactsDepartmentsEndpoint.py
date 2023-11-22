from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsCountEndpoint import (
    CompanyContactsDepartmentsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsIdEndpoint import CompanyContactsDepartmentsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsInfoEndpoint import CompanyContactsDepartmentsInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ContactDepartment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyContactsDepartmentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactDepartment], ConnectWiseManageRequestParams],
    IPostable[ContactDepartment, ConnectWiseManageRequestParams],
    IPaginateable[ContactDepartment, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "departments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ContactDepartment])
        IPostable.__init__(self, ContactDepartment)
        IPaginateable.__init__(self, ContactDepartment)

        self.count = self._register_child_endpoint(
            CompanyContactsDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(CompanyContactsDepartmentsInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> CompanyContactsDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyContactsDepartmentsIdEndpoint: The initialized CompanyContactsDepartmentsIdEndpoint object.
        """
        child = CompanyContactsDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ContactDepartment]:
        """
        Performs a GET request against the /company/contacts/departments endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params), ContactDepartment, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ContactDepartment]:
        """
        Performs a GET request against the /company/contacts/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactDepartment]: The parsed response data.
        """
        return self._parse_many(ContactDepartment, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ContactDepartment:
        """
        Performs a POST request against the /company/contacts/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactDepartment: The parsed response data.
        """
        return self._parse_one(ContactDepartment, super()._make_request("POST", data=data, params=params).json())
