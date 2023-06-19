from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdEndpoint import ProcurementPricingschedulesIdDetailsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsCountEndpoint import ProcurementPricingschedulesIdDetailsCountEndpoint
from pyconnectwise.models.manage.PricingDetailModel import PricingDetailModel

class ProcurementPricingschedulesIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPricingschedulesIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdDetailsIdEndpoint: The initialized ProcurementPricingschedulesIdDetailsIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PricingDetailModel]:
        """
        Performs a GET request against the /procurement/pricingschedules/{parentId}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingDetailModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PricingDetailModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PricingDetailModel]:
        """
        Performs a GET request against the /procurement/pricingschedules/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingDetailModel]: The parsed response data.
        """
        return self._parse_many(PricingDetailModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PricingDetailModel:
        """
        Performs a POST request against the /procurement/pricingschedules/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingDetailModel: The parsed response data.
        """
        return self._parse_one(PricingDetailModel, super().make_request("POST", params=params).json())
        