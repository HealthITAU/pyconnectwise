from pyconnectwise.endpoints.automate.ContactsIdEndpoint import ContactsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import AutomateContact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ContactsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateContact], ConnectWiseAutomateRequestParams],
    IPostable[AutomateContact, ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateContact, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Contacts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutomateContact])
        IPostable.__init__(self, AutomateContact)
        IPaginateable.__init__(self, AutomateContact)

    def id(self, id: int) -> ContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ContactsIdEndpoint: The initialized ContactsIdEndpoint object.
        """
        child = ContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateContact]:
        """
        Performs a GET request against the /Contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateContact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateContact,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateContact]:
        """
        Performs a GET request against the /Contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateContact]: The parsed response data.
        """
        return self._parse_many(
            AutomateContact,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateContact:
        """
        Performs a POST request against the /Contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateContact: The parsed response data.
        """
        return self._parse_one(
            AutomateContact,
            super()._make_request("POST", data=data, params=params).json(),
        )
