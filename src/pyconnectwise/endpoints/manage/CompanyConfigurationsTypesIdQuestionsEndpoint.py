from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsCountEndpoint import (
    CompanyConfigurationsTypesIdQuestionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdEndpoint import (
    CompanyConfigurationsTypesIdQuestionsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ConfigurationTypeQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyConfigurationsTypesIdQuestionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationTypeQuestion], ConnectWiseManageRequestParams],
    IPostable[ConfigurationTypeQuestion, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationTypeQuestion, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "questions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ConfigurationTypeQuestion])
        IPostable.__init__(self, ConfigurationTypeQuestion)
        IPaginateable.__init__(self, ConfigurationTypeQuestion)

        self.count = self._register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> CompanyConfigurationsTypesIdQuestionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsTypesIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyConfigurationsTypesIdQuestionsIdEndpoint: The initialized CompanyConfigurationsTypesIdQuestionsIdEndpoint object.
        """
        child = CompanyConfigurationsTypesIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestion, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ConfigurationTypeQuestion]:
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

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ConfigurationTypeQuestion:
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
