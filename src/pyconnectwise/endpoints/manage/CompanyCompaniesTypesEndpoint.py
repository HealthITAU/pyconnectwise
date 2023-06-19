from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesIdEndpoint import CompanyCompaniesTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesCountEndpoint import CompanyCompaniesTypesCountEndpoint
from pyconnectwise.models.manage.CompanyTypeModel import CompanyTypeModel

class CompanyCompaniesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesTypesIdEndpoint: The initialized CompanyCompaniesTypesIdEndpoint object.
        """
        child = CompanyCompaniesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyTypeModel]:
        """
        Performs a GET request against the /company/companies/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyTypeModel]:
        """
        Performs a GET request against the /company/companies/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTypeModel]: The parsed response data.
        """
        return self._parse_many(CompanyTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyTypeModel:
        """
        Performs a POST request against the /company/companies/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyTypeModel: The parsed response data.
        """
        return self._parse_one(CompanyTypeModel, super().make_request("POST", params=params).json())
        