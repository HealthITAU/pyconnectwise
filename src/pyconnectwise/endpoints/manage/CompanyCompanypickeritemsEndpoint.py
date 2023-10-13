from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanypickeritemsClearEndpoint import CompanyCompanypickeritemsClearEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanypickeritemsCountEndpoint import CompanyCompanypickeritemsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanypickeritemsIdEndpoint import CompanyCompanypickeritemsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyPickerItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompanypickeritemsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyPickerItem], ConnectWiseManageRequestParams],
    IPostable[CompanyPickerItem, ConnectWiseManageRequestParams],
    IPaginateable[CompanyPickerItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "companyPickerItems", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyPickerItem])
        IPostable.__init__(self, CompanyPickerItem)
        IPaginateable.__init__(self, CompanyPickerItem)

        self.count = self._register_child_endpoint(CompanyCompanypickeritemsCountEndpoint(client, parent_endpoint=self))
        self.clear = self._register_child_endpoint(CompanyCompanypickeritemsClearEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompanypickeritemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanypickeritemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompanypickeritemsIdEndpoint: The initialized CompanyCompanypickeritemsIdEndpoint object.
        """
        child = CompanyCompanypickeritemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyPickerItem]:
        """
        Performs a GET request against the /company/companyPickerItems endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyPickerItem]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyPickerItem, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CompanyPickerItem]:
        """
        Performs a GET request against the /company/companyPickerItems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyPickerItem]: The parsed response data.
        """
        return self._parse_many(CompanyPickerItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyPickerItem:
        """
        Performs a POST request against the /company/companyPickerItems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyPickerItem: The parsed response data.
        """
        return self._parse_one(CompanyPickerItem, super()._make_request("POST", data=data, params=params).json())
