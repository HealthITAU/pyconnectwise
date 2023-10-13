from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContacttypeassociationsCountEndpoint import \
    CompanyContacttypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContacttypeassociationsIdEndpoint import \
    CompanyContacttypeassociationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyContactTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContacttypeassociationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyContactTypeAssociation], ConnectWiseManageRequestParams],
    IPostable[CompanyContactTypeAssociation, ConnectWiseManageRequestParams],
    IPaginateable[CompanyContactTypeAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "contactTypeAssociations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyContactTypeAssociation])
        IPostable.__init__(self, CompanyContactTypeAssociation)
        IPaginateable.__init__(self, CompanyContactTypeAssociation)

        self.count = self._register_child_endpoint(
            CompanyContacttypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContacttypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContacttypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContacttypeassociationsIdEndpoint: The initialized CompanyContacttypeassociationsIdEndpoint object.
        """
        child = CompanyContacttypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyContactTypeAssociation]:
        """
        Performs a GET request against the /company/contactTypeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyContactTypeAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyContactTypeAssociation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyContactTypeAssociation]:
        """
        Performs a GET request against the /company/contactTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyContactTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            CompanyContactTypeAssociation, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> CompanyContactTypeAssociation:
        """
        Performs a POST request against the /company/contactTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyContactTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            CompanyContactTypeAssociation, super()._make_request("POST", data=data, params=params).json()
        )
