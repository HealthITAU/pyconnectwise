from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesCountEndpoint import CompanyContactsTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesIdEndpoint import CompanyContactsTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesInfoEndpoint import CompanyContactsTypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ContactType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContactsTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactType], ConnectWiseManageRequestParams],
    IPostable[ContactType, ConnectWiseManageRequestParams],
    IPaginateable[ContactType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ContactType])
        IPostable.__init__(self, ContactType)
        IPaginateable.__init__(self, ContactType)

        self.count = self._register_child_endpoint(CompanyContactsTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyContactsTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsTypesIdEndpoint: The initialized CompanyContactsTypesIdEndpoint object.
        """
        child = CompanyContactsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ContactType]:
        """
        Performs a GET request against the /company/contacts/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ContactType]:
        """
        Performs a GET request against the /company/contacts/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactType]: The parsed response data.
        """
        return self._parse_many(ContactType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ContactType:
        """
        Performs a POST request against the /company/contacts/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactType: The parsed response data.
        """
        return self._parse_one(ContactType, super()._make_request("POST", data=data, params=params).json())
