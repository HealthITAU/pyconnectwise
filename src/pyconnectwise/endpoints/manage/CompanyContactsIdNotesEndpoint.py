from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesCountEndpoint import (
    CompanyContactsIdNotesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesIdEndpoint import (
    CompanyContactsIdNotesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ContactNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyContactsIdNotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactNote], ConnectWiseManageRequestParams],
    IPostable[ContactNote, ConnectWiseManageRequestParams],
    IPaginateable[ContactNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "notes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ContactNote])
        IPostable.__init__(self, ContactNote)
        IPaginateable.__init__(self, ContactNote)

        self.count = self._register_child_endpoint(
            CompanyContactsIdNotesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsIdNotesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdNotesIdEndpoint: The initialized CompanyContactsIdNotesIdEndpoint object.
        """
        child = CompanyContactsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ContactNote]:
        """
        Performs a GET request against the /company/contacts/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactNote,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ContactNote]:
        """
        Performs a GET request against the /company/contacts/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactNote]: The parsed response data.
        """
        return self._parse_many(
            ContactNote, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactNote:
        """
        Performs a POST request against the /company/contacts/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactNote: The parsed response data.
        """
        return self._parse_one(
            ContactNote, super()._make_request("POST", data=data, params=params).json()
        )
