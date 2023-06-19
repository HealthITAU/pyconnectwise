from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesIdEndpoint import CompanyCompaniesInfoTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesCountEndpoint import CompanyCompaniesInfoTypesCountEndpoint
from pyconnectwise.models.manage.CompanyTypeInfoModel import CompanyTypeInfoModel

class CompanyCompaniesInfoTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesInfoTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesInfoTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesInfoTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesInfoTypesIdEndpoint: The initialized CompanyCompaniesInfoTypesIdEndpoint object.
        """
        child = CompanyCompaniesInfoTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyTypeInfoModel]:
        """
        Performs a GET request against the /company/companies/info/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTypeInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyTypeInfoModel]:
        """
        Performs a GET request against the /company/companies/info/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTypeInfoModel]: The parsed response data.
        """
        return self._parse_many(CompanyTypeInfoModel, super().make_request("GET", params=params).json())
        