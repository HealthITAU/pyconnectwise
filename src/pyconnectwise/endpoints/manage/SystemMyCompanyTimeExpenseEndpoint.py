from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyCompanyTimeExpenseIdEndpoint import SystemMyCompanyTimeExpenseIdEndpoint
from pyconnectwise.endpoints.manage.SystemMyCompanyTimeExpenseCountEndpoint import SystemMyCompanyTimeExpenseCountEndpoint
from pyconnectwise.models.manage.TimeExpenseModel import TimeExpenseModel

class SystemMyCompanyTimeExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeExpense", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyTimeExpenseCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyCompanyTimeExpenseIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyCompanyTimeExpenseIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyCompanyTimeExpenseIdEndpoint: The initialized SystemMyCompanyTimeExpenseIdEndpoint object.
        """
        child = SystemMyCompanyTimeExpenseIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeExpenseModel]:
        """
        Performs a GET request against the /system/myCompany/timeExpense endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeExpenseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeExpenseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeExpenseModel]:
        """
        Performs a GET request against the /system/myCompany/timeExpense endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeExpenseModel]: The parsed response data.
        """
        return self._parse_many(TimeExpenseModel, super().make_request("GET", params=params).json())
        