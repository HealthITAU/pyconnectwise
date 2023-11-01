from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsIdManagementproductsCountEndpoint import (
    CompanyManagementitsolutionsIdManagementproductsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsIdManagementproductsIdEndpoint import (
    CompanyManagementitsolutionsIdManagementproductsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ManagementItSolutionAgreementInterfaceParameter
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyManagementitsolutionsIdManagementproductsEndpoint(
    ConnectWiseEndpoint,
    IGettable[
        list[ManagementItSolutionAgreementInterfaceParameter],
        ConnectWiseManageRequestParams,
    ],
    IPostable[
        ManagementItSolutionAgreementInterfaceParameter, ConnectWiseManageRequestParams
    ],
    IPaginateable[
        ManagementItSolutionAgreementInterfaceParameter, ConnectWiseManageRequestParams
    ],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "managementProducts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ManagementItSolutionAgreementInterfaceParameter])
        IPostable.__init__(self, ManagementItSolutionAgreementInterfaceParameter)
        IPaginateable.__init__(self, ManagementItSolutionAgreementInterfaceParameter)

        self.count = self._register_child_endpoint(
            CompanyManagementitsolutionsIdManagementproductsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> CompanyManagementitsolutionsIdManagementproductsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementitsolutionsIdManagementproductsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementitsolutionsIdManagementproductsIdEndpoint: The initialized CompanyManagementitsolutionsIdManagementproductsIdEndpoint object.
        """
        child = CompanyManagementitsolutionsIdManagementproductsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ManagementItSolutionAgreementInterfaceParameter]:
        """
        Performs a GET request against the /company/managementItSolutions/{id}/managementProducts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementItSolutionAgreementInterfaceParameter]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagementItSolutionAgreementInterfaceParameter,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ManagementItSolutionAgreementInterfaceParameter]:
        """
        Performs a GET request against the /company/managementItSolutions/{id}/managementProducts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementItSolutionAgreementInterfaceParameter]: The parsed response data.
        """
        return self._parse_many(
            ManagementItSolutionAgreementInterfaceParameter,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagementItSolutionAgreementInterfaceParameter:
        """
        Performs a POST request against the /company/managementItSolutions/{id}/managementProducts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolutionAgreementInterfaceParameter: The parsed response data.
        """
        return self._parse_one(
            ManagementItSolutionAgreementInterfaceParameter,
            super()._make_request("POST", data=data, params=params).json(),
        )
