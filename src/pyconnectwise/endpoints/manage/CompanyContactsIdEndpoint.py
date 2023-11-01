from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsEndpoint import (
    CompanyContactsIdCommunicationsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsEndpoint import (
    CompanyContactsIdGroupsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdImageEndpoint import (
    CompanyContactsIdImageEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesEndpoint import (
    CompanyContactsIdNotesEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdPortalsecurityEndpoint import (
    CompanyContactsIdPortalsecurityEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdTracksEndpoint import (
    CompanyContactsIdTracksEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsEndpoint import (
    CompanyContactsIdTypeassociationsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdUsagesEndpoint import (
    CompanyContactsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import Contact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyContactsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Contact, ConnectWiseManageRequestParams],
    IPuttable[Contact, ConnectWiseManageRequestParams],
    IPatchable[Contact, ConnectWiseManageRequestParams],
    IPaginateable[Contact, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Contact)
        IPuttable.__init__(self, Contact)
        IPatchable.__init__(self, Contact)
        IPaginateable.__init__(self, Contact)

        self.portal_security = self._register_child_endpoint(
            CompanyContactsIdPortalsecurityEndpoint(client, parent_endpoint=self)
        )
        self.type_associations = self._register_child_endpoint(
            CompanyContactsIdTypeassociationsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self._register_child_endpoint(
            CompanyContactsIdGroupsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            CompanyContactsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.communications = self._register_child_endpoint(
            CompanyContactsIdCommunicationsEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self._register_child_endpoint(
            CompanyContactsIdTracksEndpoint(client, parent_endpoint=self)
        )
        self.notes = self._register_child_endpoint(
            CompanyContactsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.image = self._register_child_endpoint(
            CompanyContactsIdImageEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Contact]:
        """
        Performs a GET request against the /company/contacts/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Contact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Contact,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Contact:
        """
        Performs a GET request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(
            Contact, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Contact:
        """
        Performs a PUT request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(
            Contact, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Contact:
        """
        Performs a PATCH request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(
            Contact, super()._make_request("PATCH", data=data, params=params).json()
        )
