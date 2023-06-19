from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdInfoEndpoint import ProcurementShipmentmethodsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdUsagesEndpoint import ProcurementShipmentmethodsIdUsagesEndpoint
from pyconnectwise.models.manage.ShipmentMethodModel import ShipmentMethodModel

class ProcurementShipmentmethodsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            ProcurementShipmentmethodsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ProcurementShipmentmethodsIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ShipmentMethodModel]:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ShipmentMethodModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ShipmentMethodModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ShipmentMethodModel:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethodModel: The parsed response data.
        """
        return self._parse_one(ShipmentMethodModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ShipmentMethodModel:
        """
        Performs a PUT request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethodModel: The parsed response data.
        """
        return self._parse_one(ShipmentMethodModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ShipmentMethodModel:
        """
        Performs a PATCH request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethodModel: The parsed response data.
        """
        return self._parse_one(ShipmentMethodModel, super().make_request("PATCH", params=params).json())
        