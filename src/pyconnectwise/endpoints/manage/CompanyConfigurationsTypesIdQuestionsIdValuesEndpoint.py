from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint import \
    CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint import \
    CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ConfigurationTypeQuestionValue
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyConfigurationsTypesIdQuestionsIdValuesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationTypeQuestionValue], ConnectWiseManageRequestParams],
    IPostable[ConfigurationTypeQuestionValue, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationTypeQuestionValue, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "values", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ConfigurationTypeQuestionValue])
        IPostable.__init__(self, ConfigurationTypeQuestionValue)
        IPaginateable.__init__(self, ConfigurationTypeQuestionValue)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestionValue, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ConfigurationTypeQuestionValue]:
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

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ConfigurationTypeQuestionValue:
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
