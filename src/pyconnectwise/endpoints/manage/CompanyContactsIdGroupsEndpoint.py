from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsCountEndpoint import CompanyContactsIdGroupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsIdEndpoint import CompanyContactsIdGroupsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ContactGroup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContactsIdGroupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactGroup], ConnectWiseManageRequestParams],
    IPostable[ContactGroup, ConnectWiseManageRequestParams],
    IPaginateable[ContactGroup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "groups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ContactGroup])
        IPostable.__init__(self, ContactGroup)
        IPaginateable.__init__(self, ContactGroup)

        self.count = self._register_child_endpoint(CompanyContactsIdGroupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsIdGroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdGroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdGroupsIdEndpoint: The initialized CompanyContactsIdGroupsIdEndpoint object.
        """
        child = CompanyContactsIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ContactGroup]:
        """
        Performs a GET request against the /company/contacts/{id}/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactGroup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactGroup, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ContactGroup]:
        """
        Performs a GET request against the /company/contacts/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactGroup]: The parsed response data.
        """
        return self._parse_many(ContactGroup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ContactGroup:
        """
        Performs a POST request against the /company/contacts/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactGroup: The parsed response data.
        """
        return self._parse_one(ContactGroup, super()._make_request("POST", data=data, params=params).json())
