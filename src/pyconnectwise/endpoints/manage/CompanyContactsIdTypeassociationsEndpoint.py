from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsCountEndpoint import \
    CompanyContactsIdTypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsIdEndpoint import \
    CompanyContactsIdTypeassociationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ContactContactTypeAssociationContactTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContactsIdTypeassociationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactContactTypeAssociationContactTypeAssociation], ConnectWiseManageRequestParams],
    IPostable[ContactContactTypeAssociationContactTypeAssociation, ConnectWiseManageRequestParams],
    IPaginateable[ContactContactTypeAssociationContactTypeAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "typeAssociations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ContactContactTypeAssociationContactTypeAssociation])
        IPostable.__init__(self, ContactContactTypeAssociationContactTypeAssociation)
        IPaginateable.__init__(self, ContactContactTypeAssociationContactTypeAssociation)

        self.count = self._register_child_endpoint(
            CompanyContactsIdTypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsIdTypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdTypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdTypeassociationsIdEndpoint: The initialized CompanyContactsIdTypeassociationsIdEndpoint object.
        """
        child = CompanyContactsIdTypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ContactContactTypeAssociationContactTypeAssociation]:
        """
        Performs a GET request against the /company/contacts/{id}/typeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactContactTypeAssociationContactTypeAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactContactTypeAssociationContactTypeAssociation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ContactContactTypeAssociationContactTypeAssociation]:
        """
        Performs a GET request against the /company/contacts/{id}/typeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactContactTypeAssociationContactTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            ContactContactTypeAssociationContactTypeAssociation,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ContactContactTypeAssociationContactTypeAssociation:
        """
        Performs a POST request against the /company/contacts/{id}/typeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactContactTypeAssociationContactTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            ContactContactTypeAssociationContactTypeAssociation,
            super()._make_request("POST", data=data, params=params).json(),
        )
