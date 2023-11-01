from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import BulkResult, CompanyConfiguration
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyConfigurationsBulkEndpoint(
    ConnectWiseEndpoint,
    IPostable[CompanyConfiguration, ConnectWiseManageRequestParams],
    IDeleteable[ConnectWiseManageRequestParams],
    IPuttable[CompanyConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "bulk", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, CompanyConfiguration)
        IDeleteable.__init__(self, None)
        IPuttable.__init__(self, CompanyConfiguration)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CompanyConfiguration:
        """
        Performs a POST request against the /company/configurations/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyConfiguration: The parsed response data.
        """
        return self._parse_one(
            CompanyConfiguration,
            super()._make_request("POST", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BulkResult:
        """
        Performs a DELETE request against the /company/configurations/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(
            BulkResult, super()._make_request("DELETE", data=data, params=params).json()
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CompanyConfiguration:
        """
        Performs a PUT request against the /company/configurations/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyConfiguration: The parsed response data.
        """
        return self._parse_one(
            CompanyConfiguration,
            super()._make_request("PUT", data=data, params=params).json(),
        )
