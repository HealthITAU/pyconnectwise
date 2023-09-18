from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsCountEndpoint import \
    CompanyConfigurationsTypesIdQuestionsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdEndpoint import \
    CompanyConfigurationsTypesIdQuestionsIdEndpoint
from pyconnectwise.models.manage import ConfigurationTypeQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyConfigurationsTypesIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "questions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyConfigurationsTypesIdQuestionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsTypesIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsTypesIdQuestionsIdEndpoint: The initialized CompanyConfigurationsTypesIdQuestionsIdEndpoint object.
        """
        child = CompanyConfigurationsTypesIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ConfigurationTypeQuestion]:
        """
        Performs a GET request against the /company/configurations/types/{id}/questions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestion]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestion, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationTypeQuestion]:
        """
        Performs a GET request against the /company/configurations/types/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestion]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationTypeQuestion, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeQuestion:
        """
        Performs a POST request against the /company/configurations/types/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeQuestion: The parsed response data.
        """
        return self._parse_one(
            ConfigurationTypeQuestion, super()._make_request("POST", data=data, params=params).json()
        )
