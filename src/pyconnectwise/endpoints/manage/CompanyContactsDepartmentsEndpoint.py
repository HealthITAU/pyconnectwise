from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsIdEndpoint import CompanyContactsDepartmentsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsCountEndpoint import CompanyContactsDepartmentsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsInfoEndpoint import CompanyContactsDepartmentsInfoEndpoint
from pyconnectwise.models.manage.ContactDepartmentModel import ContactDepartmentModel

class CompanyContactsDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyContactsDepartmentsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyContactsDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsDepartmentsIdEndpoint: The initialized CompanyContactsDepartmentsIdEndpoint object.
        """
        child = CompanyContactsDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactDepartmentModel]:
        """
        Performs a GET request against the /company/contacts/departments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactDepartmentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactDepartmentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactDepartmentModel]:
        """
        Performs a GET request against the /company/contacts/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactDepartmentModel]: The parsed response data.
        """
        return self._parse_many(ContactDepartmentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactDepartmentModel:
        """
        Performs a POST request against the /company/contacts/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactDepartmentModel: The parsed response data.
        """
        return self._parse_one(ContactDepartmentModel, super().make_request("POST", params=params).json())
        