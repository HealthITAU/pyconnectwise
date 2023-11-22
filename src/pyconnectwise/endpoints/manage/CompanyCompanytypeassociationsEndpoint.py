from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanytypeassociationsCountEndpoint import (
    CompanyCompanytypeassociationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompanytypeassociationsIdEndpoint import (
    CompanyCompanytypeassociationsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import CompanyCompanyTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyCompanytypeassociationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyCompanyTypeAssociation], ConnectWiseManageRequestParams],
    IPostable[CompanyCompanyTypeAssociation, ConnectWiseManageRequestParams],
    IPaginateable[CompanyCompanyTypeAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "companyTypeAssociations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyCompanyTypeAssociation])
        IPostable.__init__(self, CompanyCompanyTypeAssociation)
        IPaginateable.__init__(self, CompanyCompanyTypeAssociation)

        self.count = self._register_child_endpoint(
            CompanyCompanytypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> CompanyCompanytypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanytypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyCompanytypeassociationsIdEndpoint: The initialized CompanyCompanytypeassociationsIdEndpoint object.
        """
        child = CompanyCompanytypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyCompanyTypeAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyCompanyTypeAssociation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyCompanyTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            CompanyCompanyTypeAssociation, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> CompanyCompanyTypeAssociation:
        """
        Performs a POST request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyCompanyTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            CompanyCompanyTypeAssociation, super()._make_request("POST", data=data, params=params).json()
        )
