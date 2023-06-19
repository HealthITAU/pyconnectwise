from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint import SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint
from pyconnectwise.endpoints.manage.SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint import SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint
from pyconnectwise.models.manage.EmailConnectorParsingRuleModel import EmailConnectorParsingRuleModel

class SystemEmailConnectorsIdParsingStylesIdParsingRulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingRules", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint: The initialized SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint object.
        """
        child = SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EmailConnectorParsingRuleModel]:
        """
        Performs a GET request against the /system/emailConnectors/{grandparentId}/parsingStyles/{parentId}/parsingRules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailConnectorParsingRuleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            EmailConnectorParsingRuleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EmailConnectorParsingRuleModel]:
        """
        Performs a GET request against the /system/emailConnectors/{grandparentId}/parsingStyles/{parentId}/parsingRules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailConnectorParsingRuleModel]: The parsed response data.
        """
        return self._parse_many(EmailConnectorParsingRuleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailConnectorParsingRuleModel:
        """
        Performs a POST request against the /system/emailConnectors/{grandparentId}/parsingStyles/{parentId}/parsingRules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnectorParsingRuleModel: The parsed response data.
        """
        return self._parse_one(EmailConnectorParsingRuleModel, super().make_request("POST", params=params).json())
        