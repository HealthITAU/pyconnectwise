from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsInfoCountEndpoint import (
    ConfigurationsTypesIdQuestionsInfoCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ConfigurationTypeQuestionInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ConfigurationsTypesIdQuestionsInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationTypeQuestionInfo], ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationTypeQuestionInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ConfigurationTypeQuestionInfo])
        IPaginateable.__init__(self, ConfigurationTypeQuestionInfo)

        self.count = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsInfoCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ConfigurationTypeQuestionInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/info endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            ConfigurationTypeQuestionInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ConfigurationTypeQuestionInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionInfo]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationTypeQuestionInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
