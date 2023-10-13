from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesCopyEndpoint import CompanyConfigurationsTypesCopyEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesCountEndpoint import \
    CompanyConfigurationsTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdEndpoint import CompanyConfigurationsTypesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ConfigurationType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyConfigurationsTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationType], ConnectWiseManageRequestParams],
    IPostable[ConfigurationType, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ConfigurationType])
        IPostable.__init__(self, ConfigurationType)
        IPaginateable.__init__(self, ConfigurationType)

        self.copy = self._register_child_endpoint(CompanyConfigurationsTypesCopyEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(
            CompanyConfigurationsTypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyConfigurationsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsTypesIdEndpoint: The initialized CompanyConfigurationsTypesIdEndpoint object.
        """
        child = CompanyConfigurationsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ConfigurationType]:
        """
        Performs a GET request against the /company/configurations/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ConfigurationType]:
        """
        Performs a GET request against the /company/configurations/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationType]: The parsed response data.
        """
        return self._parse_many(ConfigurationType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ConfigurationType:
        """
        Performs a POST request against the /company/configurations/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationType: The parsed response data.
        """
        return self._parse_one(ConfigurationType, super()._make_request("POST", data=data, params=params).json())
