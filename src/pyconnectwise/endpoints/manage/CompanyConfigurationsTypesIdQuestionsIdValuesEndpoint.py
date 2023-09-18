from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint import \
    CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint import \
    CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint
from pyconnectwise.models.manage import ConfigurationTypeQuestionValue
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyConfigurationsTypesIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "values", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint: The initialized CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint object.
        """
        child = CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ConfigurationTypeQuestionValue]:
        """
        Performs a GET request against the /company/configurations/types/{id}/questions/{id}/values endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionValue]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestionValue, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationTypeQuestionValue]:
        """
        Performs a GET request against the /company/configurations/types/{id}/questions/{id}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionValue]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationTypeQuestionValue, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeQuestionValue:
        """
        Performs a POST request against the /company/configurations/types/{id}/questions/{id}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeQuestionValue: The parsed response data.
        """
        return self._parse_one(
            ConfigurationTypeQuestionValue, super()._make_request("POST", data=data, params=params).json()
        )
