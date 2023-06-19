from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemSurveysIdCopyEndpoint import SystemSurveysIdCopyEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdInfoEndpoint import SystemSurveysIdInfoEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsEndpoint import SystemSurveysIdQuestionsEndpoint
from pyconnectwise.models.manage.SurveyModel import SurveyModel

class SystemSurveysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            SystemSurveysIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemSurveysIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.questions = self.register_child_endpoint(
            SystemSurveysIdQuestionsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SurveyModel]:
        """
        Performs a GET request against the /system/surveys/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SurveyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyModel:
        """
        Performs a GET request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyModel: The parsed response data.
        """
        return self._parse_one(SurveyModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyModel:
        """
        Performs a PUT request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyModel: The parsed response data.
        """
        return self._parse_one(SurveyModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyModel:
        """
        Performs a PATCH request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyModel: The parsed response data.
        """
        return self._parse_one(SurveyModel, super().make_request("PATCH", params=params).json())
        