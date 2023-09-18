from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsCountEndpoint import \
    CompanyContactsIdTypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsIdEndpoint import \
    CompanyContactsIdTypeassociationsIdEndpoint
from pyconnectwise.models.manage import ContactContactTypeAssociationContactTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdTypeassociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "typeAssociations", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactContactTypeAssociationContactTypeAssociation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
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
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
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
