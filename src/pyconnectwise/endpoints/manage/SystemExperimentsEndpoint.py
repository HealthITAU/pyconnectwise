from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemExperimentsIdEndpoint import SystemExperimentsIdEndpoint
from pyconnectwise.endpoints.manage.SystemExperimentsCountEndpoint import SystemExperimentsCountEndpoint
from pyconnectwise.models.manage.ExperimentModel import ExperimentModel

class SystemExperimentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "experiments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemExperimentsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemExperimentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemExperimentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemExperimentsIdEndpoint: The initialized SystemExperimentsIdEndpoint object.
        """
        child = SystemExperimentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExperimentModel]:
        """
        Performs a GET request against the /system/experiments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExperimentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExperimentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExperimentModel]:
        """
        Performs a GET request against the /system/experiments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExperimentModel]: The parsed response data.
        """
        return self._parse_many(ExperimentModel, super().make_request("GET", params=params).json())
        