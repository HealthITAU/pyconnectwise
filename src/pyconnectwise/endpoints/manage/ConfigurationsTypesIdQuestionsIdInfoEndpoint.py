from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ConfigurationTypeQuestionInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ConfigurationsTypesIdQuestionsIdInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[ConfigurationTypeQuestionInfo, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationTypeQuestionInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ConfigurationTypeQuestionInfo)
        IPaginateable.__init__(self, ConfigurationTypeQuestionInfo)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ConfigurationTypeQuestionInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/{id}/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestionInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ConfigurationTypeQuestionInfo:
        """
        Performs a GET request against the /configurations/types/{id}/questions/{id}/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeQuestionInfo: The parsed response data.
        """
        return self._parse_one(
            ConfigurationTypeQuestionInfo, super()._make_request("GET", data=data, params=params).json()
        )
