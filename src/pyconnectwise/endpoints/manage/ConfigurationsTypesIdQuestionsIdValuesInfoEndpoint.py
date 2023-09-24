from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint import \
    ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ConfigurationTypeQuestionValueInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ConfigurationsTypesIdQuestionsIdValuesInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationTypeQuestionValueInfo], ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationTypeQuestionValueInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ConfigurationTypeQuestionValueInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/{id}/values/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionValueInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ConfigurationTypeQuestionValueInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ConfigurationTypeQuestionValueInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/{id}/values/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionValueInfo]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationTypeQuestionValueInfo, super()._make_request("GET", data=data, params=params).json()
        )
