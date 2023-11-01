from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksCountEndpoint import (
    CompanyCompaniesIdTracksCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksIdEndpoint import (
    CompanyCompaniesIdTracksIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ContactTrack
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCompaniesIdTracksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactTrack], ConnectWiseManageRequestParams],
    IPostable[ContactTrack, ConnectWiseManageRequestParams],
    IPaginateable[ContactTrack, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "tracks", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ContactTrack])
        IPostable.__init__(self, ContactTrack)
        IPaginateable.__init__(self, ContactTrack)

        self.count = self._register_child_endpoint(
            CompanyCompaniesIdTracksCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesIdTracksIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTracksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTracksIdEndpoint: The initialized CompanyCompaniesIdTracksIdEndpoint object.
        """
        child = CompanyCompaniesIdTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ContactTrack]:
        """
        Performs a GET request against the /company/companies/{id}/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactTrack]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactTrack,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ContactTrack]:
        """
        Performs a GET request against the /company/companies/{id}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactTrack]: The parsed response data.
        """
        return self._parse_many(
            ContactTrack, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactTrack:
        """
        Performs a POST request against the /company/companies/{id}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactTrack: The parsed response data.
        """
        return self._parse_one(
            ContactTrack, super()._make_request("POST", data=data, params=params).json()
        )
