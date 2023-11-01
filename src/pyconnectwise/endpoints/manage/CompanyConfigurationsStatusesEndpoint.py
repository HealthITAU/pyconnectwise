from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesCountEndpoint import (
    CompanyConfigurationsStatusesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesIdEndpoint import (
    CompanyConfigurationsStatusesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesInfoEndpoint import (
    CompanyConfigurationsStatusesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ConfigurationStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyConfigurationsStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationStatus], ConnectWiseManageRequestParams],
    IPostable[ConfigurationStatus, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "statuses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ConfigurationStatus])
        IPostable.__init__(self, ConfigurationStatus)
        IPaginateable.__init__(self, ConfigurationStatus)

        self.count = self._register_child_endpoint(
            CompanyConfigurationsStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyConfigurationsStatusesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyConfigurationsStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsStatusesIdEndpoint: The initialized CompanyConfigurationsStatusesIdEndpoint object.
        """
        child = CompanyConfigurationsStatusesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ConfigurationStatus]:
        """
        Performs a GET request against the /company/configurations/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ConfigurationStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ConfigurationStatus]:
        """
        Performs a GET request against the /company/configurations/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationStatus]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationStatus,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ConfigurationStatus:
        """
        Performs a POST request against the /company/configurations/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationStatus: The parsed response data.
        """
        return self._parse_one(
            ConfigurationStatus,
            super()._make_request("POST", data=data, params=params).json(),
        )
