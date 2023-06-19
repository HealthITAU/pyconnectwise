from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceSurveysIdCopyEndpoint import ServiceSurveysIdCopyEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdUsagesEndpoint import ServiceSurveysIdUsagesEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsEndpoint import ServiceSurveysIdQuestionsEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsEndpoint import ServiceSurveysIdResultsEndpoint
from pyconnectwise.models.manage.ServiceSurveyModel import ServiceSurveyModel

class ServiceSurveysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            ServiceSurveysIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ServiceSurveysIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.questions = self.register_child_endpoint(
            ServiceSurveysIdQuestionsEndpoint(client, parent_endpoint=self)
        )
        self.results = self.register_child_endpoint(
            ServiceSurveysIdResultsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceSurveyModel]:
        """
        Performs a GET request against the /service/surveys/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurveyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceSurveyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyModel:
        """
        Performs a GET request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyModel: The parsed response data.
        """
        return self._parse_one(ServiceSurveyModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyModel:
        """
        Performs a PUT request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyModel: The parsed response data.
        """
        return self._parse_one(ServiceSurveyModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyModel:
        """
        Performs a PATCH request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyModel: The parsed response data.
        """
        return self._parse_one(ServiceSurveyModel, super().make_request("PATCH", params=params).json())
        