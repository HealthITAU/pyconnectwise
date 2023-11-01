from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import ConfigurationType
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyConfigurationsTypesCopyEndpoint(
    ConnectWiseEndpoint, IPostable[ConfigurationType, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, ConfigurationType)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ConfigurationType:
        """
        Performs a POST request against the /company/configurations/types/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationType: The parsed response data.
        """
        return self._parse_one(
            ConfigurationType,
            super()._make_request("POST", data=data, params=params).json(),
        )
