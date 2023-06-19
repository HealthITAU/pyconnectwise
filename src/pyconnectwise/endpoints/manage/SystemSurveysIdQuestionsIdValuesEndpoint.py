from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsIdValuesIdEndpoint import SystemSurveysIdQuestionsIdValuesIdEndpoint
from pyconnectwise.models.manage.SurveyQuestionValueModel import SurveyQuestionValueModel

class SystemSurveysIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "values", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> SystemSurveysIdQuestionsIdValuesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSurveysIdQuestionsIdValuesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSurveysIdQuestionsIdValuesIdEndpoint: The initialized SystemSurveysIdQuestionsIdValuesIdEndpoint object.
        """
        child = SystemSurveysIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SurveyQuestionValueModel]:
        """
        Performs a GET request against the /system/surveys/{grandparentId}/questions/{parentId}/values endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyQuestionValueModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SurveyQuestionValueModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyQuestionValueModel]:
        """
        Performs a GET request against the /system/surveys/{grandparentId}/questions/{parentId}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyQuestionValueModel]: The parsed response data.
        """
        return self._parse_many(SurveyQuestionValueModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestionValueModel:
        """
        Performs a POST request against the /system/surveys/{grandparentId}/questions/{parentId}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestionValueModel: The parsed response data.
        """
        return self._parse_one(SurveyQuestionValueModel, super().make_request("POST", params=params).json())
        