from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsBulkEndpoint import CompanyConfigurationsBulkEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsCountEndpoint import CompanyConfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsIdEndpoint import CompanyConfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesEndpoint import CompanyConfigurationsStatusesEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesEndpoint import CompanyConfigurationsTypesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyConfigurationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyConfiguration], ConnectWiseManageRequestParams],
    IPostable[CompanyConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[CompanyConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)

        self.types = self._register_child_endpoint(CompanyConfigurationsTypesEndpoint(client, parent_endpoint=self))
        self.bulk = self._register_child_endpoint(CompanyConfigurationsBulkEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(CompanyConfigurationsCountEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(
            CompanyConfigurationsStatusesEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsIdEndpoint: The initialized CompanyConfigurationsIdEndpoint object.
        """
        child = CompanyConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyConfiguration]:
        """
        Performs a GET request against the /company/configurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyConfiguration, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyConfiguration]:
        """
        Performs a GET request against the /company/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyConfiguration]: The parsed response data.
        """
        return self._parse_many(CompanyConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> CompanyConfiguration:
        """
        Performs a POST request against the /company/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyConfiguration: The parsed response data.
        """
        return self._parse_one(CompanyConfiguration, super()._make_request("POST", data=data, params=params).json())
