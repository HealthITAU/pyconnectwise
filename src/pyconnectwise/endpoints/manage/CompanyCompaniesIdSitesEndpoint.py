from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesIdEndpoint import CompanyCompaniesIdSitesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesCountEndpoint import CompanyCompaniesIdSitesCountEndpoint
from pyconnectwise.models.manage.CompanySiteModel import CompanySiteModel

class CompanyCompaniesIdSitesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sites", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdSitesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesIdSitesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdSitesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdSitesIdEndpoint: The initialized CompanyCompaniesIdSitesIdEndpoint object.
        """
        child = CompanyCompaniesIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanySiteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/sites endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanySiteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanySiteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanySiteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanySiteModel]: The parsed response data.
        """
        return self._parse_many(CompanySiteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanySiteModel:
        """
        Performs a POST request against the /company/companies/{parentId}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanySiteModel: The parsed response data.
        """
        return self._parse_one(CompanySiteModel, super().make_request("POST", params=params).json())
        