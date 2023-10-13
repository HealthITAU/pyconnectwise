from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesCountEndpoint import CompanyCompaniesInfoTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesIdEndpoint import CompanyCompaniesInfoTypesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompaniesInfoTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[CompanyTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyTypeInfo])
        IPaginateable.__init__(self, CompanyTypeInfo)

        self.count = self._register_child_endpoint(CompanyCompaniesInfoTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesInfoTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesInfoTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesInfoTypesIdEndpoint: The initialized CompanyCompaniesInfoTypesIdEndpoint object.
        """
        child = CompanyCompaniesInfoTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyTypeInfo]:
        """
        Performs a GET request against the /company/companies/info/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyTypeInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyTypeInfo]:
        """
        Performs a GET request against the /company/companies/info/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTypeInfo]: The parsed response data.
        """
        return self._parse_many(CompanyTypeInfo, super()._make_request("GET", data=data, params=params).json())
