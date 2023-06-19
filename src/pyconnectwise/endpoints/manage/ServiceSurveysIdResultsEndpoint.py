from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsIdEndpoint import ServiceSurveysIdResultsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsCountEndpoint import ServiceSurveysIdResultsCountEndpoint
from pyconnectwise.models.manage.SurveyResultModel import SurveyResultModel

class ServiceSurveysIdResultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "results", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSurveysIdResultsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceSurveysIdResultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSurveysIdResultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSurveysIdResultsIdEndpoint: The initialized ServiceSurveysIdResultsIdEndpoint object.
        """
        child = ServiceSurveysIdResultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SurveyResultModel]:
        """
        Performs a GET request against the /service/surveys/{parentId}/results endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyResultModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SurveyResultModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyResultModel]:
        """
        Performs a GET request against the /service/surveys/{parentId}/results endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyResultModel]: The parsed response data.
        """
        return self._parse_many(SurveyResultModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyResultModel:
        """
        Performs a POST request against the /service/surveys/{parentId}/results endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyResultModel: The parsed response data.
        """
        return self._parse_one(SurveyResultModel, super().make_request("POST", params=params).json())
        