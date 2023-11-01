from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesCountEndpoint import (
    CompanyCompaniesTypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesIdEndpoint import (
    CompanyCompaniesTypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import CompanyType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyCompaniesTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyType], ConnectWiseManageRequestParams],
    IPostable[CompanyType, ConnectWiseManageRequestParams],
    IPaginateable[CompanyType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "types", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[CompanyType])
        IPostable.__init__(self, CompanyType)
        IPaginateable.__init__(self, CompanyType)

        self.count = self._register_child_endpoint(
            CompanyCompaniesTypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesTypesIdEndpoint: The initialized CompanyCompaniesTypesIdEndpoint object.
        """
        child = CompanyCompaniesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CompanyType]:
        """
        Performs a GET request against the /company/companies/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CompanyType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[CompanyType]:
        """
        Performs a GET request against the /company/companies/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyType]: The parsed response data.
        """
        return self._parse_many(
            CompanyType, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CompanyType:
        """
        Performs a POST request against the /company/companies/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyType: The parsed response data.
        """
        return self._parse_one(
            CompanyType, super()._make_request("POST", data=data, params=params).json()
        )
