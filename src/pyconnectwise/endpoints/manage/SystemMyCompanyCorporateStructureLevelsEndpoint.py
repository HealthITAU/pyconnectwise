from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyCompanyCorporateStructureLevelsIdEndpoint import SystemMyCompanyCorporateStructureLevelsIdEndpoint
from pyconnectwise.endpoints.manage.SystemMyCompanyCorporateStructureLevelsCountEndpoint import SystemMyCompanyCorporateStructureLevelsCountEndpoint
from pyconnectwise.models.manage.CorporateStructureLevelModel import CorporateStructureLevelModel

class SystemMyCompanyCorporateStructureLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "corporateStructureLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyCompanyCorporateStructureLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyCompanyCorporateStructureLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyCompanyCorporateStructureLevelsIdEndpoint: The initialized SystemMyCompanyCorporateStructureLevelsIdEndpoint object.
        """
        child = SystemMyCompanyCorporateStructureLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CorporateStructureLevelModel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructureLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CorporateStructureLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CorporateStructureLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CorporateStructureLevelModel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructureLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CorporateStructureLevelModel]: The parsed response data.
        """
        return self._parse_many(CorporateStructureLevelModel, super().make_request("GET", params=params).json())
        