from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyManagementItSolutionsIdEndpoint import CompanyManagementItSolutionsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementItSolutionsCountEndpoint import CompanyManagementItSolutionsCountEndpoint
from pyconnectwise.models.manage.ManagementItSolutionModel import ManagementItSolutionModel

class CompanyManagementItSolutionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementItSolutions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementItSolutionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyManagementItSolutionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementItSolutionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementItSolutionsIdEndpoint: The initialized CompanyManagementItSolutionsIdEndpoint object.
        """
        child = CompanyManagementItSolutionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagementItSolutionModel]:
        """
        Performs a GET request against the /company/managementItSolutions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementItSolutionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagementItSolutionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementItSolutionModel]:
        """
        Performs a GET request against the /company/managementItSolutions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementItSolutionModel]: The parsed response data.
        """
        return self._parse_many(ManagementItSolutionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementItSolutionModel:
        """
        Performs a POST request against the /company/managementItSolutions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolutionModel: The parsed response data.
        """
        return self._parse_one(ManagementItSolutionModel, super().make_request("POST", params=params).json())
        